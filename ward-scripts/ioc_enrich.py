#!/usr/bin/env python3
"""ioc_enrich.py — Enrich an IOC (IP or domain) from multiple sources.

Usage: python ioc_enrich.py <ip_or_domain>
"""

import sys
import json
import os
import re
import urllib.request
import urllib.error
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_key(name):
    env_path = os.path.join(BASE_DIR, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith(name + "="):
                    return line.split("=", 1)[1]
    return None

def is_ip(value):
    parts = value.split(".")
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

def is_domain(value):
    return bool(re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$', value))

def check_abuseipdb(ip):
    key = get_key("ABUSEIPDB_KEY")
    if not key:
        return {"source": "AbuseIPDB", "error": "no key"}

    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    req = urllib.request.Request(url, headers={
        "Key": key,
        "Accept": "application/json"
    })

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"source": "AbuseIPDB", "error": f"HTTP {e.code}"}
    except urllib.error.URLError as e:
        return {"source": "AbuseIPDB", "error": f"network: {e.reason}"}

    d = data.get("data", {})
    score = d.get("abuseConfidenceScore", 0)
    return {
        "source": "AbuseIPDB",
        "score": score,
        "country": d.get("countryCode", "unknown"),
        "asn": d.get("asn", "unknown"),
        "total_reports": d.get("totalReports", 0),
        "status": "BLOCK" if score >= 50 else "CLEAN"
    }

def check_virustotal(ioc):
    key = get_key("VT_KEY")
    if not key:
        return {"source": "VirusTotal", "error": "no key (add VT_KEY to .env)"}

    if is_ip(ioc):
        endpoint = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"
    else:
        endpoint = f"https://www.virustotal.com/api/v3/domains/{ioc}"

    req = urllib.request.Request(endpoint, headers={
        "x-apikey": key,
        "Accept": "application/json"
    })

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"source": "VirusTotal", "error": "IOC not found in VT database"}
        if e.code == 429:
            return {"source": "VirusTotal", "error": "rate limited (4 req/min)"}
        return {"source": "VirusTotal", "error": f"HTTP {e.code}"}
    except urllib.error.URLError as e:
        return {"source": "VirusTotal", "error": f"network: {e.reason}"}

    d = data.get("data", {}).get("attributes", {})
    stats = d.get("last_analysis_stats", {})
    return {
        "source": "VirusTotal",
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "harmless": stats.get("harmless", 0),
        "reputation": d.get("reputation", 0),
        "country": d.get("country", "unknown"),
        "tags": d.get("tags", [])
    }

def check_ipinfo(ip):
    url = f"https://ipinfo.io/{ip}/json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            d = json.loads(resp.read())
        return {
            "source": "ipinfo",
            "city": d.get("city", "unknown"),
            "country": d.get("country", "unknown"),
            "org": d.get("org", "unknown"),
            "asn": d.get("asn", "unknown")
        }
    except urllib.error.HTTPError as e:
        return {"source": "ipinfo", "error": f"HTTP {e.code}"}
    except urllib.error.URLError as e:
        return {"source": "ipinfo", "error": f"network: {e.reason}"}

def main():
    if len(sys.argv) != 2:
        print("Usage: python ioc_enrich.py <ip_or_domain>")
        sys.exit(1)

    ioc = sys.argv[1].strip()

    if not is_ip(ioc) and not is_domain(ioc):
        print(f"Error: '{ioc}' is not a valid IP address or domain.")
        sys.exit(1)

    result = {
        "timestamp": datetime.now().isoformat(),
        "ioc": ioc,
        "type": "ip" if is_ip(ioc) else "domain",
        "sources": []
    }

    if is_ip(ioc):
        result["sources"].append(check_abuseipdb(ioc))
        result["sources"].append(check_ipinfo(ioc))

    result["sources"].append(check_virustotal(ioc))

    # Log to file (cap at 100 entries)
    log_path = os.path.join(BASE_DIR, "enrichment_log.json")
    log = []
    if os.path.exists(log_path):
        try:
            with open(log_path) as f:
                log = json.load(f)
        except (json.JSONDecodeError, IOError):
            log = []
    log.append(result)
    if len(log) > 100:
        log = log[-100:]
    tmp_path = log_path + ".tmp"
    with open(tmp_path, "w") as f:
        json.dump(log, f, indent=2)
    os.replace(tmp_path, log_path)

    # Print summary
    print(f"\nIOC: {ioc} ({result['type']})")
    print(f"Time: {result['timestamp']}")
    print()
    for s in result["sources"]:
        print(f"  [{s['source']}]")
        if "error" in s:
            print(f"    {s['error']}")
        else:
            for k, v in s.items():
                if k != "source":
                    print(f"    {k}: {v}")
        print()

if __name__ == "__main__":
    main()   
