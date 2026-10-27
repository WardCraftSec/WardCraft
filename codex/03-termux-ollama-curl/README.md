# Termux Ollama via curl

## Problem
ollama CLI not in PATH, but server already running on port 11434.

## Solution
Hit the REST API with curl — no extra packages needed.

### Check server
curl http://127.0.0.1:11434/api/tags

### One-shot prompt
curl -s http://127.0.0.1:11434/api/generate -d '{"model":"qwen3:1.7b","prompt":"hello","stream":false}'

### Interactive REPL
while read -p "you> " prompt; do curl -s http://127.0.0.1:11434/api/generate -d "{\"model\":\"qwen3:1.7b\",\"prompt\":\"$prompt\",\"stream\":false}" | grep -o '"response":"[^"]*"' | cut -d'"' -f4; echo; done

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
- Pager missing (git config --global core.pager cat)
- nano continuation prompt (>) swallowed commands after broken echo

### What worked
- First run: 185.220.101.1 → score=100, DE, 194 reports, BLOCK
- Log written to ward_log.json

### Lesson
The endpoint I initially used was wrong. Always test with a known-bad IP
before trusting the script. The docs I read were stale.   
