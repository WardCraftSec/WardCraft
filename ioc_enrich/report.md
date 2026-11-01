# IOC Enrichment Report
*Generated: 2026-11-01 19:20*  
*Analyst: WardCraft*  
*Source: Manual collection (NextDNS logs, phishing samples)*

## Summary
- **Total IOCs analysed:** 9
- **Flagged (VT votes > 0 or abuseIP score > 50):** 1

## Findings

### 185.220.101.34 (IP)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/ip_addresses/185.220.101.34 (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |
| ABUSEIP | score | 100 |
| ABUSEIP | reports | 136 |
| ABUSEIP | last_seen | 2026-11-01T18:00:14+00:00 |
| ABUSEIP | country | DE |
| ABUSEIP | isp | Network for Tor-Exit traffic. |

**⚠️ Flagged — recommended action: block / investigate further**

### 45.155.205.233 (IP)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/ip_addresses/45.155.205.233 (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |
| ABUSEIP | score | 0 |
| ABUSEIP | reports | 0 |
| ABUSEIP | last_seen | 2026-08-13T21:12:47+00:00 |
| ABUSEIP | country | RU |
| ABUSEIP | isp | Cloud Technologies LLC trading as Cloud.ru |

**✅ No significant threat indicators found**

### 103.215.31.12 (IP)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/ip_addresses/103.215.31.12 (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |
| ABUSEIP | score | 0 |
| ABUSEIP | reports | 0 |
| ABUSEIP | last_seen | None |
| ABUSEIP | country | CN |
| ABUSEIP | isp | Shenyang Huaxing communication engineering limited liability company |

**✅ No significant threat indicators found**

### 23.94.188.227 (IP)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/ip_addresses/23.94.188.227 (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |
| ABUSEIP | score | 0 |
| ABUSEIP | reports | 0 |
| ABUSEIP | last_seen | None |
| ABUSEIP | country | US |
| ABUSEIP | isp | HostPapa |

**✅ No significant threat indicators found**

### xmr-stak-pool.example-mining.com (Domain)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/domains/xmr-stak-pool.example-mining.com (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |

**✅ No significant threat indicators found**

### 8.8.8.8 (IP)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/ip_addresses/8.8.8.8 (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |
| ABUSEIP | score | 0 |
| ABUSEIP | reports | 65 |
| ABUSEIP | last_seen | 2026-11-01T18:53:21+00:00 |
| ABUSEIP | country | US |
| ABUSEIP | isp | Google LLC |

**✅ No significant threat indicators found**

### 1.1.1.1 (IP)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/ip_addresses/1.1.1.1 (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |
| ABUSEIP | score | 0 |
| ABUSEIP | reports | 116 |
| ABUSEIP | last_seen | 2026-11-01T13:01:09+00:00 |
| ABUSEIP | country | AU |
| ABUSEIP | isp | APNIC and Cloudflare DNS Resolver project |

**✅ No significant threat indicators found**

### pypi.org (Domain)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/domains/pypi.org (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |

**✅ No significant threat indicators found**

### github.com (Domain)

| Source | Field | Value |
|--------|-------|-------|
| VT | error | HTTPSConnectionPool(host='api.vt.com', port=443): Max retries exceeded with url: /v3/domains/github.com (Caused by NameResolutionError("HTTPSConnection(host='api.vt.com', port=443): Failed to resolve 'api.vt.com' ([Errno 7] No address associated with hostname)")) |

**✅ No significant threat indicators found**

---
*Methodology: VirusTotal API v3 + abuseIPDB API v2. All IOCs sanitised where required.*