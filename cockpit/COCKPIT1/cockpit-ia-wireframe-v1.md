# COCKPIT1 IA Wireframe v1

## Status

Drafted for construction.

## Main screen layout

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Project / Route Switcher | Mode: Cockpit | Export | Search | Model Status  │
├───────────────┬───────────────────────────────────────┬──────────────────────┤
│ LEFT RAIL     │ MAIN PANEL                            │ RIGHT RAIL           │
│               │                                       │                      │
│ Project Map   │ Current Focus Object                  │ Open Dissents        │
│ Route Tree    │ - title / type / state               │ Current Verdict      │
│ Object Index  │ - dependencies / pressure            │ Recent Activity      │
│ Filters       │ - key evidence / key dissent         │ Attention Items      │
│               │ - next actions                        │                      │
├───────────────┴───────────────────────────────────────┴──────────────────────┤
│ SIDECAR CONSOLE: temporary analysis, brainstorming, drafting, debug         │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Region notes

- The left rail owns navigation.
- The main panel owns the current object.
- The right rail owns judgment pressure and recent movement.
- The sidecar console is available but subordinate.

## Non-goal reminder

This screen is not a team dashboard, not a page-emission surface, and not a repo-wide product homepage.
