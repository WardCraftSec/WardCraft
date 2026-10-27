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

