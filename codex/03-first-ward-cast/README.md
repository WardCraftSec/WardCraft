# Codex Entry 03 — First Ward Cast

*The first time the hammer actually hit something.*

**Date:** 2026-10-27
**Tags:** python, abuseipdb, ioc, first-script

## What I set out to do

I'd spotted a Tor exit node (185.220.101.1) in my NextDNS logs the previous day. I wanted a script that takes an IP, checks it against AbuseIPDB, and tells me: block or clean. One command, one answer.

## ward_cast.py

Takes an IP, queries AbuseIPDB v2, returns score + country + report count. Writes to `ward_log.json`. Threshold: score >= 50 → BLOCK.

## What broke

| Problem | Cause | Fix |
|---|---|---|
| 404 on first run | Used `/api/v2/ip/{ip}` instead of `/api/v2/check?ipAddress={ip}` | Corrected endpoint |
| Key not recognised | `.env` value had a trailing space (copied from a wrapped line in browser) | Trimmed the value |
| `python: command not found` | Termux doesn't ship Python by default | `pkg install python` (96 MB, 19 packages) |

## First run
   ```
185.220.101.1 | score=100 | DE | reports=194 | BLOCK
```


Tor exit node. Expected result. Log written to `ward_log.json`.

## Lesson

Always test with a known-bad IP before trusting the script. The endpoint I initially used was from stale docs. If the first run returns a 404, the script is wrong, not the IP.

## What's next

`ioc_enrich.py` — same pattern, three sources (AbuseIPDB + VirusTotal + ipinfo), structured JSON output.   
