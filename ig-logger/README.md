# IG tick logger

Records live bid/ask tick data from IG's streaming API to Parquet, so that
intraday history exists to analyse later.

The reason this comes before any analysis: IG's REST history allowance is
**10,000 price points per week**, which is roughly one week of 1-minute bars
for a single instrument. You cannot go back and buy intraday history at that
rate. The Lightstreamer feed, by contrast, costs nothing to consume. Every day
this runs is a day of data you will otherwise never have.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env      # then fill it in
```

Get an API key from **My IG → Settings → API keys**. Demo and live are separate
keys on separate accounts. Start on demo — the tick stream is real either way,
and there is no reason to point a brand-new recorder at a funded account.

## Run it

```bash
python run_logger.py                      # record until stopped (Ctrl-C)
python run_logger.py --replay             # synthetic feed, no credentials
python run_logger.py --duration 3600      # stop after an hour
```

`--replay` generates realistic synthetic ticks. Use it to check the plumbing,
disk layout and permissions before trusting it with a session you cannot
repeat.

To leave it running properly, use systemd (`Restart=always`) or a `tmux`
session. It handles `SIGTERM` cleanly and flushes what it has buffered.

Nightly, once the market is closed:

```bash
python -m ig_logger.compact data
```

## Reading the data

```python
import pandas as pd
df = pd.read_parquet("data")                       # everything
df = pd.read_parquet("data/CS.D.EURUSD.MINI.IP")   # one instrument
df["spread"] = df["ofr"] - df["bid"]
```

Layout is `data/<EPIC>/<YYYY-MM-DD>/part-*.parquet`, with a `compacted.parquet`
once compaction has run.

| column | meaning |
|---|---|
| `recv_ts` | when *we* received it (UTC) — always present |
| `utm` | IG's own tick timestamp (UTC) — can be null |
| `bid`, `ofr` | the two sides of the book. `ofr - bid` is the spread you pay |
| `ltp`, `ltv` | last traded price and volume |
| `ttv` | incremental volume |
| `day_*` | daily open/high/low and change, as IG reports them |

Both timestamps are kept deliberately. `utm` is the better clock but is
sometimes missing, and it cannot tell you the order things actually arrived in.

## How it works

```
Lightstreamer thread(s) ──► bounded Queue ──► writer thread ──► Parquet
                                  ▲
                          supervisor restarts a dead feed
```

Four decisions worth knowing about, because each one is a way this could have
quietly lost data:

**Disk I/O never happens on a Lightstreamer callback.** If a write blocks, the
client's internal buffers back up and ticks vanish with no error. The queue is
bounded so that a stalled disk drops rows *with a counter you can see* rather
than growing until the process is OOM-killed.

**Silence is treated as failure.** A stream that connects and then delivers
nothing looks exactly like a quiet market. After `IG_STALE_SECONDS` with no
ticks the session is torn down and rebuilt. Out of hours that means a reconnect
every few minutes, which is harmless and means the recorder is already live the
moment the market opens.

**Shutdown stops the feed before it stops the writer.** The other order looks
fine and loses the last few seconds of every session.

**Every file is written to `.tmp` and renamed.** `os.replace` is atomic, so a
crash mid-write leaves a stray `.tmp`, never a corrupt part that poisons every
later read of that directory.

One gotcha worth recording, since it costs an afternoon to find: trading-ig's
`IGStreamService` sets `acc_number = None` in `__init__` and never populates it,
but `create_session()` passes it straight to Lightstreamer's `setUser()`. Unless
you set it yourself you authenticate as `None`. Hence `IG_ACC_NUMBER` being
required rather than optional.

## Capacity

Measured on this machine, single writer thread:

| | |
|---|---|
| throughput | ~190,000 ticks/sec |
| on disk | ~10 bytes/tick (zstd) |
| a busy instrument | well under 1 MB/day |

Storage is a non-issue; a year of several instruments fits comfortably in a
few hundred MB. The bottleneck will be IG's feed, not this.

## Tests

```bash
python -m pytest tests/ -q
```

28 tests, no credentials and no network needed. They cover the storage layer
(partitioning, schema stability, atomic writes, concurrent access), the tick
parser (including the junk values IG really sends), compaction, and the whole
pipeline against the synthetic feed — including that a failing feed is retried,
a silent feed is rebuilt, and shutdown strands nothing.

What they cannot cover is the live IG connection itself. That part is only
proven by running `python run_logger.py` against a demo account and confirming
rows appear.

## Status

Not yet run against a live IG account — no credentials were available when this
was written. Everything up to the socket is tested; the first demo run is the
real acceptance test.
