# IOC Sources

Quick reference. API keys in `.env`, never here.

## AbuseIPDB
- Endpoint: `https://api.abuseipdb.com/api/v2/check?ipAddress={ip}`
- Header: `Key: $ABUSEIPDB_KEY`
- Rate: 1000 req/day (free)
- Returns: abuse confidence score (0–100), country, ASN, total reports
- Use: "Is this IP known bad?"

## VirusTotal
- Endpoints:
  - `https://www.virustotal.com/api/v3/ip_addresses/{ip}`
  - `https://www.virustotal.com/api/v3/domains/{domain}`
  - `https://www.virustotal.com/api/v3/urls/{url}`
  - `https://www.virustotal.com/api/v3/files/{hash}`
- Header: `x-apikey: $VT_KEY`
- Rate: 4 req/min, 500 req/day (free)
- Note: add `time.sleep(15)` between calls in batch scripts
- Returns: engine detection counts (malicious/suspicious/harmless/undetected), country, ASN, reputation, tags
- Use: "Do any engines flag this?"

## ipinfo
- Endpoint: `https://ipinfo.io/{ip}/json`
- No key needed (free: 50k lookups/month)
- Returns: city, country, org, ASN
- Use: "Who runs this IP and where is it?"

## NextDNS (local)
- Dashboard: `app.nextdns.io`
- Export: CSV, last 30 days
- Use: "What did my phone actually query?"

## OTX (AlienVault) — add when relevant
- Endpoint: `https://otx.alienvault.com/api/v1/indicators/{type}/{value}/general`
- Types: `ipAddress`, `domain`, `url`, `hostname`
- No key needed (rate limited)
- Use: "Is this in AlienVault's threat intel?"

## MISP — add when relevant
- Self-hosted or instance-based
- Use: "What does our internal threat intel say?"   
