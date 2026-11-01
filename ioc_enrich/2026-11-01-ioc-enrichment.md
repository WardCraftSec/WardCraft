# Codex Entry: IOC Enrichment — First Run
**Date:** 2026-11-01
**Tool:** ioc_enrich.py (abuseIPDB API v2)
**Source:** Public threat intel + control set

## What I fed it
- 9 IOCs: 5 IPs, 4 domains
- Mix of known-malicious and known-clean (control set)
- Note: VirusTotal API unavailable (DNS resolution failure on local network). Findings below are abuseIPDB-only.

## Key findings

### 185.220.101.34
- abuseIPDB: **score 100**, 136 reports, last seen 2026-11-01 18:00 UTC
- ISP: "Network for Tor-Exit traffic" (DE)
- **Verdict: ⚠️ Confirmed malicious infrastructure. Known Tor exit node.**
- **Action: Block. Add to NextDNS denylist. Cross-reference with threat actor TTPs if seen in traffic.**

### 45.155.205.233
- abuseIPDB: score 0, 0 reports, RU, Cloud.ru
- **Verdict: ✅ Clean. No reports on file.**
- **Action: No action. Monitor if reappears in unusual context.**

### 8.8.8.8 (control)
- abuseIPDB: score 0, 65 reports (likely port scans hitting it, not malicious use)
- ISP: Google LLC
- **Verdict: ✅ Clean. Control behaved as expected.**

### 1.1.1.1 (control)
- abuseIPDB: score 0, 116 reports
- ISP: Cloudflare DNS Resolver
- **Verdict: ✅ Clean. Control behaved as expected.**

## Observations
- High report counts on clean IPs (8.8.8.8, 1.1.1.1) show that **report volume ≠ maliciousness**. The abuse confidence score is the reliable signal, not raw report count.
- The Tor exit node (185.220.101.34) was the only true positive — consistent with its known use as anonymisation infrastructure.
- VT integration pending DNS fix; will re-run with full enrichment once resolved.

## What I'd do next
- Fix VT DNS resolution, re-run for full dual-source enrichment
- Automate daily enrichment of new NextDNS anomalies
- Map confirmed malicious activity to MITRE ATT&CK
- Build a local blocklist from flagged results

## Tools used
- Python 3.14, requests
- abuseIPDB API v2 (free tier)
- VirusTotal API v3 (pending DNS fix)   
