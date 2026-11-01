#!/usr/bin/env python3
"""
ioc_enrich.py — Enrich a list of IOCs via VirusTotal + abuseIPDB
Output: structured Markdown report
Usage: python ioc_enrich.py iocs.txt
"""

import requests
import json
import sys
from datetime import datetime

VT_API_KEY = "a877c40ec40f9d8b09ff39ab61733e4a973e19fd4b30e927ce3109edcbe31476"
ABUSEIP_KEY = "7f2608c515bd29d76fff78fe867b8b41b8c6be635cc1afe90ac836f9e7b0766e3b706e9334679dcd"
VT_API = "https://api.vt.com/v3"
ABUSEIP_API = "https://api.abuseipdb.com/api/v2"

def enrich_ip(ip):
    """Enrich a single IP via VirusTotal + abuseIPDB"""
    result = {"ip": ip, "vt": {}, "abuseip": {}}

    # VirusTotal — IP report
    try:
        r = requests.get(
            f"{VT_API}/ip_addresses/{ip}",
            headers={"x-apikey": VT_API_KEY}
        )
        if r.status_code == 200:
            d = r.json().get("data", {})
            result["vt"]["last_seen"] = d.get("attributes", {}).get("last_seen_geolocation", {}).get("country")
            result["vt"]["network"] = d.get("attributes", {}).get("network")
            result["vt"]["total_votes"] = d.get("attributes", {}).get("total_votes")
            result["vt"]["reputation"] = d.get("attributes", {}).get("reputation")
    except Exception as e:
        result["vt"]["error"] = str(e)

    # abuseIPDB
    try:
        r = requests.get(
            f"{ABUSEIP_API}/check",
            params={"ipAddress": ip, "maxLength": 10},
            headers={"Key": ABUSEIP_KEY, "Accept": "application/json"}
        )
        if r.status_code == 200:
            d = r.json().get("data", {})
            result["abuseip"]["score"] = d.get("abuseConfidenceScore")
            result["abuseip"]["reports"] = d.get("totalReports")
            result["abuseip"]["last_seen"] = d.get("lastReportedAt")
            result["abuseip"]["country"] = d.get("countryCode")
            result["abuseip"]["isp"] = d.get("isp")
    except Exception as e:
        result["abuseip"]["error"] = str(e)

    return result

def enrich_domain(domain):
    """Enrich a domain via VirusTotal"""
    result = {"domain": domain, "vt": {}}
    try:
        r = requests.get(
            f"{VT_API}/domains/{domain}",
            headers={"x-apikey": VT_API_KEY}
        )
        if r.status_code == 200:
            d = r.json().get("data", {})
            attrs = d.get("attributes", {})
            result["vt"]["registrar"] = attrs.get("registrar")
            result["vt"]["creation_date"] = attrs.get("date_created")
            result["vt"]["total_votes"] = attrs.get("total_votes")
            result["vt"]["reputation"] = attrs.get("reputation")
    except Exception as e:
        result["vt"]["error"] = str(e)
    return result

def generate_report(results):
    """Output a Markdown report"""
    lines = [
        f"# IOC Enrichment Report",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*  ",
        f"*Analyst: WardCraft*  ",
        f"*Source: Manual collection (NextDNS logs, phishing samples)*",
        "",
        "## Summary",
        f"- **Total IOCs analysed:** {len(results)}",
        f"- **Flagged (VT votes > 0 or abuseIP score > 50):** "
        f"{sum(1 for r in results if flagged(r))}",
        "",
        "## Findings",
        "",
    ]

    for r in results:
        kind = "IP" if "ip" in r else "Domain"
        lines.append(f"### {r.get('ip', r.get('domain'))} ({kind})")
        lines.append("")
        lines.append("| Source | Field | Value |")
        lines.append("|--------|-------|-------|")
        for src in ("vt", "abuseip"):
            if src in r and r[src]:
                for k, v in r[src].items():
                    lines.append(f"| {src.upper()} | {k} | {v} |")
        lines.append("")

        # Verdict
        if flagged(r):
            lines.append("**⚠️ Flagged — recommended action: block / investigate further**")
        else:
            lines.append("**✅ No significant threat indicators found**")
        lines.append("")

    lines.append("---")
    lines.append("*Methodology: VirusTotal API v3 + abuseIPDB API v2. "
                 "All IOCs sanitised where required.*")

    return "\n".join(lines)

def flagged(r):
    vt_votes = r.get("vt", {}).get("total_votes", 0) or 0
    abuse_score = r.get("abuseip", {}).get("score", 0) or 0
    return vt_votes > 0 or abuse_score > 50

def main():
    if len(sys.argv) < 2:
        print("Usage: python ioc_enrich.py iocs.txt")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        iocs = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    results = []
    for ioc in iocs:
        if ":" in ioc or "." in ioc and not ioc.replace(".","").isdigit():
            results.append(enrich_domain(ioc))
        else:
            results.append(enrich_ip(ioc))
        print(f"  ✓ {ioc}")

    report = generate_report(results)
    print("\n" + report)

    with open("report.md", "w") as f:
        f.write(report)
    print(f"\n→ Saved to report.md")

if __name__ == "__main__":
    main()   
