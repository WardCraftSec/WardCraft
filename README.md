| 03  | Termux Ollama via curl | Oct 2026 | api curl local-llm |   | 03  | Termux Ollama via curl | Oct 2026 | api curl local-llm |   # WardCraft
ᚹᚫᚱᛞᚲᚱᚫᚠᛏ — Blue team scripts, codex entries &amp; detection rules :: blue-team  threat-intel  python  sigma  yara  home-lab  defensive-security  nextdns   

## Recent Work

| Date | What | Where |
|------|------|-------|
| Oct 2026 | GrapheneOS home stack write-up | [codex/01](./codex/01-grapheneos-stack/) |
| Oct 2026 | `ward_cast.py` — IP reputation ward | [ward-scripts/](./ward-scripts/) |

- [x] ward_cast.py (IP reputation, AbuseIPDB)
- [ ] IOC enrichment script (ioc_enrich.py)   
| Script | What it does | Status |
|--------|-------------|--------|
| `ward_cast.py` | Check IP vs AbuseIPDB, log block/clean | ✅ Working |
| `ioc_enrich.py` | Bulk IOC enrichment (IPs, domains, hashes) | 🔜 Week 2 |
| `log_anomaly.py` | Parse NextDNS export, flag query spikes | 🔜 Week 4 |

## Codex Entries

| # | Title | Date | Tags |
|---|-------|------|------|
| 01 | [GrapheneOS Home Stack](./codex/01-grapheneos-stack/) | Oct 2026 | `defensive` `os-hardening` `dns` |
| 02 | [NextDNS Log Reading](./codex/02-nextdns-log-reading) | Oct 2026 | `dns` `nextdns` |
| 03 | [Termux Ollama via curl](./codex/03-termux-ollama-curl/) | Oct 2026 | `api` `curl` `local-llm` |    
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
