# Hourly trigger via macOS launchd

GitHub's own cron throttles scheduled workflows to roughly every 2-3 hours
with occasional gaps. This launchd agent reliably triggers the
`rwc-hourly.yml` workflow every hour while your Mac is awake (and once on
wake if it slept through a fire time). The workflow itself still does all the
work in the cloud — this only kicks it off.

## One-time setup (~5 minutes)

### 1. Create a GitHub token

Create a **fine-grained personal access token**
(https://github.com/settings/tokens?type=beta):

- Repository access: **Only select repositories** → `rugby-rwc-2027`
- Permissions → **Actions: Read and write**

Copy the token (starts with `github_pat_`).

### 2. Store the token in the Keychain (not on disk)

```bash
security add-generic-password -a "$USER" -s rwc-gh-token -w 'github_pat_PASTE_HERE'
```

### 3. Install the script and agent

```bash
# from your local clone of the repo:
mkdir -p ~/Library/Scripts
# set your GitHub owner in the trigger first:
sed "s#REPLACE_WITH_OWNER#$(gh api user --jq .login)#" \
    rugby/scheduling/rwc-trigger.sh > ~/Library/Scripts/rwc-trigger.sh
chmod +x ~/Library/Scripts/rwc-trigger.sh

sed -e "s#REPLACE_WITH_SCRIPT_PATH#$HOME/Library/Scripts/rwc-trigger.sh#" \
    -e "s#REPLACE_WITH_HOME#$HOME#g" \
    rugby/scheduling/com.rugby.rwc2027.hourly.plist \
    > ~/Library/LaunchAgents/com.rugby.rwc2027.hourly.plist

launchctl load ~/Library/LaunchAgents/com.rugby.rwc2027.hourly.plist
```

`RunAtLoad` fires it immediately, so you can verify right away.

## Verify

```bash
tail ~/Library/Logs/rwc-trigger.log        # should show "OK: workflow dispatched"
```

## Manage

```bash
# stop
launchctl unload ~/Library/LaunchAgents/com.rugby.rwc2027.hourly.plist
# rotate the token later
security delete-generic-password -s rwc-gh-token
security add-generic-password -a "$USER" -s rwc-gh-token -w 'github_pat_NEW'
```

## Notes

- While the Mac is asleep the hour is skipped, then self-heals on wake. For
  true 24/7 coverage, an external cron service is the only option, at the cost
  of storing the token off-device.
- The token only grants Actions read/write on this one repo.
