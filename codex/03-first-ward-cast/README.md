ward_cast.py takes an IP, queries AbuseIPDB v2, returns score + country + report count, writes to ward_log.json. Threshold: score >= 50 → BLOCK.   

### Exit
Ctrl+C

## Notes
- Model: qwen3:1.7b, Q4_K_M, 40960 ctx
- Pattern: API -> curl -> parse JSON   


## ward_cast.py — First Run (27 Oct 2026)

### What broke
- URL endpoint was /api/v2/ip/{ip} → 404. Correct: /api/v2/check?ipAddress={ip}
- .env key had a space (copied from a wrapped line in browser)
- Python not installed (pkg install python, 96MB, 19 packages)

### What worked
- First run: 185.220.101.1 → score=100, DE, 194 reports, BLOCK
- Log written to ward_log.json
The IP came from a NextDNS log review (Tor exit node observed in traffic).   

### Lesson
The endpoint I initially used was wrong. Always test with a known-bad IP
before trusting the script. The docs I read were stale.   
