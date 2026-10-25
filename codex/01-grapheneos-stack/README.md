> *Codex Entry 01 — The First Ward*
> Before I could cast wards for others, I had to ward my own house.   > *Codex Entry 01 — The First Ward*
> Before I could cast wards for others, I had to ward my own house.

# Home Security Stack — GrapheneOS + NextDNS + Local LLM

**Platform:** Personal (Pixel 7)
**Date:** 2026-10-25
**Duration:** 3 months active use, ~6 months total learning
**Tags:** `defensive` `os-hardening` `dns` `privacy` `local-llm` `home-lab`

---

## Objective

Build a personal mobile + network security stack that:
1. Eliminates unnecessary data collection from my phone
2. Gives me visibility into what my home network is actually talking to
3. Lets me run a local AI model without sending prompts to a third party
4. Serves as a practical foundation for a blue team career

This isn't a "paranoid hacker setup." It started with blocking adult content
at home, got curious about DNS, and snowballed from there.

---

## The Origin

| Stage | What happened |
|-------|--------------|
| 1 | Needed to block adult content at home → set up a DNS filter |
| 2 | Realised DNS is where *everything* tunnels through → got obsessed |
| 3 | Found **@lizthedeveloper** (Multiverse School) → guided recon into how apps tunnel through DNS, how trackers work, how to actually *see* the traffic |
| 4 | Decided my phone needed to match the network-level controls → researched alternatives to stock Android |
| 5 | Flashed **GrapheneOS** on my Pixel 7 (unlocked bootloader) |
| 6 | Added **NextDNS Pro** as system-level DoT resolver on all home devices |
| 7 | Wanted a local LLM for prompt testing → got **Qwen 3 1.7B** running in Termux via Ollama |
| 8 | Now: reviewing NextDNS logs daily, sandboxing apps into profiles, building toward a blue team job |

---

## The Stack

Pixel 7 (128GB, 8GB RAM)
├── OS: GrapheneOS 2026102101 (Android 17)
│   ├── Bootloader: Unlocked
│   ├── Updates: Auto (manual approval per release)
│   └── 5 Sandbox Profiles:
│       ├── Owner    — personal, Proton Mail, F-Droid apps
│       ├── Banking  — banking apps only (isolation from everything else)
│       ├── Social   — social media (sandboxed from banking/owner data)
│       ├── Google   — Google services (de-googled from main profile)
│       └── AI       — Termux, Ollama, Qwen 3 1.7B
│
├── Network:
│   ├── NextDNS (Pro plan) — system-level DoT (Private DNS)
│   │   ├── Blocks: malicious, ads, trackers, crypto miners, adult
│   │   ├── Custom rules: extensive + wildcard blocks
│   │   └── Log review: DAILY (this is the fun part, not boring)
│   └── All home devices pointed at same NextDNS profile
│
├── Apps:
│   ├── Proton Mail (email)
│   ├── Proton Storage (files)
│   ├── F-Droid (app source, no Play Store)
│   └── Termux → Ollama → Qwen 3 1.7B (local inference)
│
└── No:
    ├── Google Play / Play Services (except sandboxed Google profile)
    ├── Play Protect
    ├── Stock Android telemetry
    └── Any app I can't name the developer of

---

## Key Decisions

### Why GrapheneOS over stock Android or /e/OS

| Factor | GrapheneOS | Stock Android | /e/OS |
|--------|-----------|---------------|-------|
| Security model | Hardened kernel, secure spawning, hardened_malloc, no Play Services by default | Standard AOSP + Google telemetry | AOSP + F-Droid, less hardening |
| Update cadence | Monthly security patches, security preview channel available | Varies by OEM | Slower, community-maintained |
| App compatibility | Full (Vanadium browser, sandboxed Google Play available) | Full | Good, but some apps break |
| Community/docs | Large, active, well-documented | N/A | Smaller |
| My use case | Best fit — I want the hardening, not just "no Google" | Telemetry everywhere | Fine, but less hardened |

The decision was easy. Pixel 7 + GrapheneOS is the most well-supported
combination. The bootloader unlock was the only scary step.

### Why NextDNS over Pi-hole / AdGuard Home

I already had a DNS filter for content blocking. NextDNS Pro gave me:
- DoT built-in (no extra hardware needed on the phone)
- Per-device profiles (different rules for my phone vs. other devices)
- Log UI that's actually pleasant to use daily
- Wildcard blocking (e.g., block all *.tracking-domain.com subdomains)
- No extra hardware — a Pi-hole requires a Raspberry Pi I don't have

I'm not running a local resolver. NextDNS is cloud-based, but the *queries*
are encrypted (DoT) and the logs are mine. For my threat model (home
surveillance, data collection, not a nation-state), this is the right trade.

### Why Qwen 3 1.7B specifically

- Smallest model in the Qwen 3 line that still produces coherent output
- Fits in 128GB storage alongside everything else (it's tight, but so is cash)
- I wanted to see how my prompts actually work on a small model
- The setup process (Termux → Ollama → model download) was the real lesson
- I hit every issue in the community docs. That's the point.

### Why 5 profiles (not 3, not 7)

| Profile | Rationale |
|---------|-----------|
| Owner | My "real" identity. Proton, F-Droid, personal stuff. |
| Banking | Non-negotiable isolation. If a banking app is compromised, it can't see my social, my AI experiments, or my owner data. |
| Social | Social apps are tracking machines. Keeping them in their own profile means their data collection is walled off. |
| Google | I still need some Google services (maps, translate). Sandboxing them means they can't see my banking or social data. |
| AI | Termux + Ollama + model weights. Keeping this separate means if I mess up a command in Termux, it doesn't touch my banking profile. |

Five is the sweet spot. Three would mean banking and social share a profile.
Seven would mean I'm switching profiles 40 times a day and hating my life.

---

## Daily Workflow

| Time | Action |
|------|--------|
| Morning | Check NextDNS log for overnight anomalies (new domains, spikes in query volume from a specific device) |
| Throughout day | Switch profiles as needed (Owner → Banking → back). This is the pain point — it's friction by design. |
| Evening | Review the day's log. Note anything new. Adjust block rules if I spot a tracker I missed. |
| Weekly | Check GrapheneOS for updates. Approve when ready. |
| Monthly | Review which apps are actually being used. Kill any profile I haven't touched in 30 days. |

---

## Pain Points (honest)

| Issue | Impact | Workaround |
|-------|--------|-----------|
| Profile switching | Constant context-switching. Want to check a banking notification while in the AI profile? Switch. Want to use a F-Droid app from Owner while in Social? Switch. | No good fix. It's the price of isolation. |
| 128GB is tight | Qwen 3 1.7B + Termux + Ollama + 5 profiles + apps = ~100GB used. Can't install large games or video apps. | I don't need those. But it limits flexibility. |
| No Play Store | Some apps simply don't exist on F-Droid. I've lost access to a few niche apps I used on stock Android. | Ungoogled APKs from GitHub, or just live without them. |
| Ollama on mobile is slow | 1.7B is small, but inference on a phone CPU is still 2-4 tokens/sec. Not for real work. | It's for learning and prompt testing, not production. Fine. |

---

## What This Taught Me (that maps to blue team)

| What I did at home | Blue team equivalent |
|--------------------|---------------------|
| Reviewing NextDNS logs daily | SIEM monitoring — looking for anomalies in a stream of data |
| Adding wildcard block rules | Detection engineering — writing rules to catch a *class* of threat, not just one instance |
| Isolating banking into its own profile | Network segmentation — limiting blast radius if one segment is compromised |
| Choosing DoT over plain DNS | Encryption in transit — understanding why protocol choice matters |
| Hitting every Ollama setup error and fixing it | Incident response — reading error logs, forming a hypothesis, testing, iterating |
| Deciding *what* to sandbox and *why* | Risk assessment — you can't protect everything, so you prioritise based on threat |

The NextDNS log review is the closest thing to a SOC shift I've done.
You're watching a stream of thousands of DNS queries and your brain is
constantly asking "is that domain supposed to be there?" That's exactly
what a Tier 1 analyst does with a SIEM.

---

## MITRE ATT&CK Mapping (Defensive)

| What I'm doing | Mitigates | ID |
|---------------|-----------|-----|
| NextDNS malicious domain block | Ingress Tool Transfer, Command & Control | T1105, T1071 |
| DoT encryption | Defence Evasion (DNS tunnelling) | T1572 |
| Profile isolation | Credential Access, Lateral Movement | T1552, T1021 |
| No Play Services | Collection, Exfiltration (telemetry) | T1119, T1041 |
| F-Droid only | Supply Chain Compromise | T1195.002 |
| Manual update approval | Defence Evasion (malicious update) | T1583.004 |

---

## Next Steps

| When | What |
|------|------|
| This month | Add Suricata or Zeek on a cheap Pi (when I can afford one) for full packet-level visibility on the home network |
| Next month | Write a second write-up: "NextDNS Log Analysis — 30 Days of Anomalies" (document actual findings from my daily reviews) |
| Q1 2027 | Sit Security+ exam. This stack is my practical evidence for the "I actually do this" part of the cert |
| Q2 2027 | SOC Tier 1 application. This write-up + the NextDNS log analysis + my THM portfolio = the package |

---

## Tools & Links

| Tool | Role |
|------|------|
| GrapheneOS (grapheneos.org) | Hardened Android OS |
| NextDNS (nextdns.io) | DNS filtering + logging (Pro) |
| Ollama (ollama.com) | Local LLM runtime (via Termux) |
| Qwen 3 1.7B (huggingface.co) | Local model for prompt testing |
| F-Droid (f-droid.org) | Open-source app store |
| Proton (proton.me) | Mail + Storage |
| @lizthedeveloper | Multiverse School — DNS recon learning |

---

## Lessons Learned

1. Start with the problem, not the tool. I didn't "decide to be a security person." I needed to block content, got curious, and the stack built itself.
2. 128GB is enough if you're intentional. I almost bought a 256GB Pixel. Didn't need to.
3. The log review is the skill. Setting up NextDNS took 10 minutes. Reviewing the logs daily for 3 months is what actually trained my eye for anomalies. That's the blue team muscle.
4. Profile switching is the tax you pay for isolation. Accept it. You'll hate it for 2 weeks, then it becomes automatic.
5. A local LLM on a phone is a learning tool, not a product. 2-4 tokens/sec is not "AI." But understanding how it works (model loading, context window, token generation) is worth more than using ChatGPT.   
