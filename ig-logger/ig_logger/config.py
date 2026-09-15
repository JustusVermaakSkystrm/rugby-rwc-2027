"""Settings, loaded from the environment.

Credentials never appear in code or in a committed file. Put them in `.env`
(which .gitignore excludes) or export them in your shell.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path


def load_dotenv(path=".env"):
    """Minimal .env reader, so there is no dependency just for this.

    Existing environment variables win, which is what you want when running
    under systemd or in a container that sets them properly.
    """
    p = Path(path)
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


class ConfigError(SystemExit):
    pass


def _require(name):
    value = os.environ.get(name)
    if not value:
        raise ConfigError(
            f"Missing required environment variable {name}. "
            "Copy .env.example to .env and fill it in."
        )
    return value


@dataclass
class Settings:
    username: str
    password: str = field(repr=False)   # keep secrets out of tracebacks and logs
    api_key: str = field(repr=False)
    acc_type: str
    acc_number: str
    epics: list
    data_dir: Path

    # how long rows may sit in memory before hitting disk. Small enough that a
    # crash costs seconds of data, large enough that we are not writing tiny
    # Parquet files hundreds of times a minute.
    flush_rows: int = 5_000
    flush_seconds: float = 30.0

    # if no tick arrives for this long while a market should be open, assume the
    # stream is dead and rebuild the session rather than sitting there happily
    # recording nothing
    stale_seconds: float = 300.0

    # bounded so a disk stall cannot grow the queue until the process is OOM-killed
    queue_size: int = 200_000

    @classmethod
    def from_env(cls):
        epics = [e.strip() for e in os.environ.get("IG_EPICS", "").split(",") if e.strip()]
        if not epics:
            raise ConfigError(
                "IG_EPICS is empty. Set it to a comma-separated list of epics, "
                "e.g. IG_EPICS=CS.D.EURUSD.MINI.IP,IX.D.FTSE.DAILY.IP"
            )
        acc_type = os.environ.get("IG_ACC_TYPE", "DEMO").upper()
        if acc_type not in {"DEMO", "LIVE"}:
            raise ConfigError(f"IG_ACC_TYPE must be DEMO or LIVE, got {acc_type!r}")

        return cls(
            username=_require("IG_USERNAME"),
            password=_require("IG_PASSWORD"),
            api_key=_require("IG_API_KEY"),
            acc_type=acc_type,
            # Required, not optional: IGStreamService.create_session() passes
            # self.acc_number straight to Lightstreamer setUser() and never
            # populates it itself, so leaving it unset authenticates as None.
            acc_number=_require("IG_ACC_NUMBER"),
            epics=epics,
            data_dir=Path(os.environ.get("IG_DATA_DIR", "data")),
            flush_rows=int(os.environ.get("IG_FLUSH_ROWS", 5_000)),
            flush_seconds=float(os.environ.get("IG_FLUSH_SECONDS", 30.0)),
            stale_seconds=float(os.environ.get("IG_STALE_SECONDS", 300.0)),
            queue_size=int(os.environ.get("IG_QUEUE_SIZE", 200_000)),
        )
