# 02 — NextDNS Log Reading

**Date:** Nov 2026
**Tags:** dns, nextdns, log-analysis, triage
**Source:** NextDNS dashboard → Logs (Pixel 7, GrapheneOS, DoT)

---

## Scope

Single device (Pixel 7, GrapheneOS) connected via DNS-over-TLS to NextDNS.
Sample: ~200 queries over a short window. Not a full 30-day export yet —
this is the first structured read.

---

## Volume

~200 queries in the sample window. Dominated by two services:
- **Facebook/Messenger** (~55% of total)
- **Brave browser + GitHub** (~30%)
- **GrapheneOS system checks** (~10%)
- **Everything else** (~5%)

No spike. No burst pattern. Steady background traffic consistent with
normal phone use (messaging, browsing, dev work).

---

## Top Domains

| Domain | Count (approx) | Purpose |
|--------|---------------|---------|
| `chat-e2ee-mini.facebook.com` | ~35 | Messenger E2EE messaging |
| `gateway.facebook.com` | ~25 | Messenger API gateway |
| `graph.facebook.com` | ~20 | Facebook Graph API |
| `edge-mqtt.facebook.com` | ~15 | Messenger MQTT (real-time) |
| `z-m-gateway.facebook.com` | ~12 | Messenger gateway (regional) |
| `search.brave.com` | ~15 | Brave search |
| `api.github.com` | ~15 | GitHub API (dev work) |
| `github.com` | ~12 | GitHub web |
| `mtalk.google.com` | ~10 | Google push notifications |
| `*-dnsotls-ds.dnscheck.grapheneos.org` | ~20 (unique) | GrapheneOS DoT health check |
| `scontent.xx.fbcdn.net` | ~8 | Facebook CDN (images/media) |
| `alive.github.com` | ~8 | GitHub liveness ping |
| `usage-ping.brave.com` | ~6 | Brave telemetry |
| `collector.github.com` | ~6 | GitHub telemetry |

---

## Telemetry / Tracking Identified

These are **allowed** (not blocked by filters) but worth noting:

| Domain | What it does | Risk |
|--------|-------------|------|
| `usage-ping.brave.com` | Brave usage stats | Low — opt-out available |
| `variations.brave.com` | Brave A/B test assignment | Low |
| `star-randsrv.bsg.brave.com` | Brave crash/stats | Low |
| `googleads.g.doubleclick.net` | Google ad tracking pixel | Medium — ad network |
| `app-measurement.com` | Firebase analytics | Low |
| `firebaselogging.googleapis.com` | Firebase event logging | Low |
| `firebase-settings.crashlytics.com` | Crashlytics crash reports | Low |

**Action:** Consider adding `googleads.g.doubleclick.net` and `app-measurement.com`
to the NextDNS denylist. No operational impact, removes two tracking beacons.

---

## GrapheneOS DNS Check Pattern

`*-dnsotls-ds.dnscheck.grapheneos.org` — each query uses a **unique random
subdomain prefix** (e.g. `07709484-`, `f2brwf-`, `1q2jr5-`).

**First-pass reaction:** Random subdomains = DGA? Flag it.

**Actual:** This is GrapheneOS's built-in DoT health check. It generates a
random subdomain per check to prevent caching and confirm the full path
is working. Documented behaviour, not an anomaly.

**Lesson:** Always check OS-level documented behaviour before flagging.
A DGA alert on a GrapheneOS device that ignores this pattern is a false positive.

---

## Anomalies

**None found in this sample.**

- No DGA patterns (after excluding GrapheneOS checks)
- No C2 beaconing (no regular-interval single-domain hits)
- No suspicious TLDs
- No unexpected domain registrations
- No lateral movement indicators (single device, no internal IPs)

---

## What I'd Do Next (SOC Frame)

If this were a real SOC log feed:

1. **Enrich top-talkers** — Run `api.github.com`, `gateway.facebook.com`,
   `mtalk.google.com` through `ioc_enrich.py` to confirm they resolve to
   expected ASN/IP ranges. (They will. This is the baseline.)

2. **Baseline** — This sample becomes the "normal" for this device.
   Future alerts fire on *deviation* from this, not on absolute volume.

3. **Denylist additions** — `googleads.g.doubleclick.net`, `app-measurement.com`.
   Low effort, removes noise.

4. **Alert rule (Sigma)** — "New domain with random subdomain pattern on
   GrapheneOS device" → suppress `*.dnscheck.grapheneos.org` in the filter,
   alert on anything else matching the pattern. (This is what `log_anomaly.py`
   will eventually do.)

5. **Handover note** — Device is clean. No action required. Next review:
   30 days. Watch for: new TLDs, volume spike >2x baseline, any domain
   resolving to a residential IP when it should be datacenter.

---

## Status

- [x] First structured read
- [ ] Full 30-day export + volume graph
- [ ] `log_anomaly.py` integration (auto-flag spikes)
- [ ] Baseline documented for alerting

---

*Written same-day. Next review: Dec 2026 (30-day mark).*   
