#!/usr/bin/env python3
"""ward_cast.py — Check IP reputation via AbuseIPDB."""

import sys
import json
import os
import urllib.request
import urllib.error
from datetime import datetime

def get_key():
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("ABUSEIPDB_KEY="):
                    return line.strip().split("=", 1)[1]
    return None

def check_ip(ip):
    key = get_key()
    if not key:
        print("ERROR: ABUSEIPDB_KEY not found in .env")
        sys.exit(1)

    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    req = urllib.request.Request(url, headers={
        "Key": key,
        "Accept": "application/json"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code}")
        sys.exit(1)

    result = data.get("data", {})
    score = result.get("abuseConfidenceScore", 0)
    country = result.get("countryCode", "unknown")
    total_reports = result.get("totalReports", 0)

    status = "BLOCK" if score >= 50 else "CLEAN"
    entry = {
        "timestamp": datetime.now().isoformat(),
        "ip": ip,
        "score": score,
        "country": country,
        "total_reports": total_reports,
        "status": status
    }

    log_path = os.path.join(os.path.dirname(__file__), "..", "ward_log.json")
    log = []
    if os.path.exists(log_path):
        with open(log_path) as f:
            log = json.load(f)
    log.append(entry)
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)

    print(f"{ip} | score={score} | {country} | reports={total_reports} | {status}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ward_cast.py <ip>")
        sys.exit(1)
    check_ip(sys.argv[1])   
