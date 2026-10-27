# IOC Sources

Quick reference. API keys in .env, never here.

## AbuseIPDB
- Endpoint: https://api.abuseipdb.com/api/v2/ip/{ip}
- Header: Key: $ABUSEIPDB_KEY
- Rate: 1000 req/day (free)
- Returns: abuse confidence score (0-100), country, ASN, reports
- Use: "Is this IP known bad?"

## VirusTotal
- Endpoint: https://www.virustotal.com/api/v3/ip_addresses/{ip}
- Also: /domains/{domain}, /urls/{url}, /files/{hash}
- Header: x-apikey: $VT_KEY
- Rate: 4 req/min, 500 req/day (free)
- Returns: engine detection counts, country, ASN, reputation, tags
- Use: "Do any engines flag this?"

## NextDNS (local)
- Dashboard: app.nextdns.io
- Export: CSV, last 30 days
- Use: "What did my phone actually query?"

## OTX (AlienVault) — add when relevant
- Endpoint: https://otx.alienvault.com/api/v1/indicators/{type}/{value}/general
- No key needed (rate limited)
- Use: "Is this in AlienVault's threat intel?"

## MISP — add when relevant
- Self-hosted or instance-based
- Use: "What does our internal threat intel say?"   
