ᚹᚫᚱᛞᚲᚱᚫᚠᛏ — Blue team scripts, codex entries & detection rules :: blue-team threat-intel python sigma yara home-lab defensive-security nextdns

# ᚹᚫᚱᛞᚲᚱᚫᚠᛏ
Blue team scripts, codex entries & detection rules.

## Recent Work

| Date | What | Where |
|------|------|-------|
| Oct 2026 | `ioc_enrich.py` — multi-source IOC enrichment | [ward-scripts/](./ward-scripts/) |
| Oct 2026 | First Sigma rule (SSH brute force) | [rune-sigmas/](./rune-sigmas/) |
| Oct 2026 | `ward_cast.py` fixed + first run | [ward-scripts/](./ward-scripts/) |
| Oct 2026 | NextDNS log reading (3 entries) | [codex/02](./codex/02-nextdns-log-reading/) |

## Scripts

| Script | What it does | Status |
|--------|-------------|--------|
| `ward_cast.py` | Check IP vs AbuseIPDB, log block/clean | ✅ Working |
| `ioc_enrich.py` | Multi-source IOC enrichment (IP, domain) | ✅ Working |
| `log_anomaly.py` | Parse NextDNS export, flag query spikes | 🔜 |

## Codex Entries

| # | Title | Date | Tags |
|---|-------|------|------|
| 00 | [Day One: The Forge](./codex/00-day-one-the-forge/) | Oct 2026 | `git` `termux` `secrets` |
| 01 | [GrapheneOS Home Stack](./codex/01-grapheneos-stack/) | Oct 2026 | `defensive` `os-hardening` `dns` |
| 02 | [NextDNS Log Reading](./codex/02-nextdns-log-reading/) | Oct 2026 | `dns` `nextdns` |
| 03 | [First Ward Cast](./codex/03-first-ward-cast/) | Oct 2026 | `api` `python` `ioc` |
| 04 | Home Lab SIEM (Wazuh) | Dec 2026 | `siem` `wazuh` `sigma` |

## Conventions
- Write-ups: numbered `NN-slug/README.md`, written same-day
- Scripts: run on Termux (Pixel 7) or any Linux box, Python 3.11+
- Sigma rules: follow [Sigma spec](https://github.com/SigmaHQ/sigma)
- No real IPs, creds, or tokens in any file. Ever.

## Status

| Item | Target |
|------|--------|
| Security+ (SY0-701) | Q1 2027 |
| PT1 | Q1 2027 |
| SOC Tier 1 application | Q2 2027 |   
