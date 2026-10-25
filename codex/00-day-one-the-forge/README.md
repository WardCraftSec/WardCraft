# Codex Entry 00 — Day One: The Forge

**Date:** 2026-10-25
**Duration:** ~4 hours (evening)
**Tags:** `git` `termux` `secrets-management` `workflow` `foundation`

> *Before you can cast wards, you need a hand to hold the hammer.*

---

## What I set out to do

Get a working GitHub portfolio live from my Pixel 7, using only Termux.
No laptop. No IDE. No browser-based editing. Just the terminal.

## What I actually did

| Time | Action | Result |
|------|--------|--------|
| ~18:00 | Created GitHub account `WardCraftSec` | ✅ |
| ~18:15 | Created profile repo + main repo | ✅ |
| ~18:30 | Wrote profile README (ᚹᚫᚱᛞᚲᚱᚫᚠᛏ ᛋᛖᚲ) | ✅ Pushed |
| ~18:45 | Tried to clone repo in Termux | ❌ `git: command not found` |
| ~18:50 | `pkg install git` | ✅ |
| ~19:00 | `git clone` | ✅ |
| ~19:10 | Tried to create `.gitignore` with heredoc | ❌ Nothing happened |
| ~19:15 | Tried `nano .gitignore` | ❌ Nothing happened |
| ~19:20 | Termux froze entirely | ❌ Black screen |
| ~19:25 | Killed Termux, reopened | ✅ Back |
| ~19:30 | Used `printf` one-liner instead | ✅ `.gitignore` created |
| ~19:40 | `git commit` | ❌ "unable to auto-detect email" |
| ~19:45 | Set `git config --global user.name` | ✅ |
| ~19:47 | Set `git config --global user.email` (first attempt malformed) | ❌ |
| ~19:48 | Fixed the command (added space + `=`) | ✅ |
| ~19:50 | `git push` | ❌ "Authentication failed" |
| ~19:55 | Learned GitHub requires a PAT, not a password | — |
| ~20:00 | Generated Personal Access Token in browser | ✅ |
| ~20:05 | `git remote set-url origin https://user:token@github.com/...` | ✅ |
| ~20:10 | `git push -u origin main` | ✅ **Pushed** |
| ~20:20 | Wrote `ward_cast.py` | ✅ |
| ~20:30 | `git add . && git commit && git push` | ✅ **First ward shipped** |

## What broke and why

| Problem | Cause | Fix |
|---------|-------|-----|
| `git: command not found` | Termux is a minimal Linux. Nothing is pre-installed. | `pkg install git` |
| Heredoc (`<< 'EOF'`) did nothing | Phone keyboard + Termux's line handling. The `EOF` terminator didn't register properly. | Use `printf '...\n...' > file` instead |
| `nano` appeared to do nothing | Terminal was frozen (accidental Ctrl+S pauses output) | Ctrl+Q to unfreeze, or kill/reopen Termux |
| `git commit` failed | No identity configured. Git needs a name + email for every commit. | `git config --global user.name "..."` + `user.email "..."` |
| `git push` auth failed | GitHub disabled password auth in 2021. You need a Personal Access Token. | Generate PAT → embed in remote URL |
| Token in `git remote -v` output | I pasted the output into a chat | **Rotate the token.** Assume it's public. |
| AbuseIPDB key pasted in chat | Same mistake, different key | **Rotate the key.** Same rule. |

## What I learned (the actual lessons)

### 1. Termux is not a desktop terminal

It's a minimal Linux environment on Android. No `git`, no `nano` working reliably, no heredoc reliability. The workarounds are:
- `pkg install <thing>` for anything missing
- `printf` over heredoc for file creation
- `nano` is fine *if* the terminal isn't frozen
git add .
git commit -m "dayone"
git push   
- Ctrl+S freezes output. Ctrl+Q unfreezes. This will happen again.

### 2. Git is a 3-step loop

### 3. A secret that's been typed is a secret that's gone

I pasted two API keys into a chat this evening. Both are now compromised by definition. The rule:

> If a secret appears anywhere it shouldn't (chat, screenshot, commit, URL bar), rotate it. Don't "remember to do it later." Do it now, before you do the next thing.

This is the first real blue team habit. In a SOC, you'll see this in incident response: a key leaked in a Slack message → rotate it before you investigate what it was used for. Contain first, investigate second.

### 4. .gitignore is your first line of defence

Without it, one `git add .` and your `.env` (with API keys) is on GitHub forever. Even after you delete the file, it's in the git history. The `.gitignore` is the ward that prevents the breach from happening in the first place.

| File | Why it's ignored |
|------|-----------------|
| `.env` | Contains API keys |
| `ward_log.json` | Contains real IPs I've checked |
| `*.pem` / `*.key` | Private keys |
| `__pycache__/` | Python junk |

### 5. The "malformed command" pattern

I made the same type of mistake 3 times today:
- `git config --global user.emailsilmarillimum@proton.me` (missing space + =)
- `git config --global user.name "WardCraftSec"   WardCraftSec` (trailing junk)
- Heredoc that didn't close properly

The pattern: typing fast on a phone keyboard, losing track of where a command ends. The fix: type one command, press Enter, read the output, then type the next. Don't batch.

### 6. "Nothing happened" usually means the terminal is frozen

Not the command. Not the file. The terminal. Ctrl+S pauses all output. It looks identical to "the command did nothing." The fix is always Ctrl+Q first, then retry.

## What this maps to (blue team)

| What I did today | Blue team equivalent |
|-----------------|---------------------|
| Setting up git + GitHub from scratch | Onboarding a new analyst: getting their tools configured |
| Hitting "command not found" and fixing it | First day in a SOC: "where's the SIEM access?" |
| Creating .gitignore before committing secrets | Writing a detection rule before the incident, not after |
| Rotating keys after exposure | Containment in IR: revoke the compromised credential first |
| The 3-step loop (add/commit/push) | PICERL: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned |
| "Nothing happened" → Ctrl+Q | Alert fired but no output → check if the pipeline is stuck, not the data |

## What's next

| When | What |
|------|------|
| Tonight | Create .env, run ward_cast.py against a real IP |
| Tomorrow | Paste the GrapheneOS write-up into codex/01 |
| This week | ioc_enrich.py (bulk IOC enrichment) |
| Next week | First Sigma rule (SSH brute force detection) |

## The honest summary

I spent 4 hours tonight doing what takes a developer 10 minutes. I froze my terminal, typed malformed commands, pasted secrets into a chat, and fought with a phone keyboard. But at the end, I have a working git workflow on a Pixel 7, a branded GitHub presence, and a first script that's live.

That's the difference between "I watched a tutorial" and "I built it and it broke and I fixed it." The breaking is the learning.

---

*Codex Entry 00 — The Forge. Where the hand learns to hold the hammer.*   
