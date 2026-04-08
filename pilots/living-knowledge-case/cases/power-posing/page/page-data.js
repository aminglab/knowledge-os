window.POWER_POSING_PAGE_DATA = {
  title: "Power Posing",
  subtitle: "A living knowledge page prototype for a disputed scientific claim.",
  description:
    "This page is a renderer prototype built from the current power-posing case, its snapshot layer, and its governed objects. It is meant to feel like a public reading surface rather than a markdown directory.",
  links: [
    { label: "Snapshot v2", href: "../snapshots/snapshot-v2.md" },
    { label: "Case overview", href: "../case.md" },
    { label: "References", href: "../references.md" },
    { label: "Timeline", href: "../timeline/events.md" }
  ],
  statusCards: [
    {
      title: "Original claim",
      status: "Contested and significantly weakened",
      summary:
        "The original strong-form claim says that brief expansive posture can change hormone levels and affect risk-taking behavior.",
      badges: ["claim", "C-0001", "V-0001"],
      links: [
        { label: "View claim C-0001", href: "../objects/claims/C-0001.md" },
        { label: "View verdict V-0001", href: "../objects/verdicts/V-0001.md" },
        { label: "View evidence E-0001", href: "../objects/evidence/E-0001.md" }
      ]
    },
    {
      title: "Descendant claim",
      status: "Contested but still surviving as a weaker path",
      summary:
        "A narrower descendant claim remains in play: posture may affect subjective feelings of power or confidence even if the stronger hormone-and-risk-taking claim does not hold.",
      badges: ["claim", "C-0002", "V-0002"],
      links: [
        { label: "View claim C-0002", href: "../objects/claims/C-0002.md" },
        { label: "View verdict V-0002", href: "../objects/verdicts/V-0002.md" }
      ]
    }
  ],
  sections: [
    {
      title: "Why this case matters",
      intro:
        "The original paper still exists as a stable publication artifact. But the knowledge status of its core claim did not stay still. It was amplified, challenged, weakened, and then partially re-read through a narrower descendant path.",
      cards: [
        {
          title: "The structural problem",
          kind: "status",
          body:
            "In a static publication system, later changes are scattered across papers, public statements, corrections, and memory. In a living knowledge system, those later changes should remain attached to the claim lineage itself."
        },
        {
          title: "What this prototype proves",
          kind: "support",
          body:
            "The same case can now exist in three layers at once: governed objects, snapshot markdown, and a reader-facing page. That is the first real step from repository structure toward product surface."
        }
      ]
    },
    {
      title: "Object neighborhoods",
      intro:
        "The page keeps the object model visible. It does not flatten the case into anonymous prose. Each neighborhood below points back to governed objects.",
      cards: [
        {
          title: "Original claim neighborhood",
          kind: "status",
          body:
            "The original 2010 paper reported higher testosterone, lower cortisol, greater feelings of power, and more tolerance for risk.",
          badges: ["C-0001", "E-0001"],
          links: [
            { label: "C-0001", href: "../objects/claims/C-0001.md" },
            { label: "E-0001", href: "../objects/evidence/E-0001.md" }
          ]
        },
        {
          title: "Empirical challenge",
          kind: "dissent",
          body:
            "A later large-sample replication challenge directly attacked the core effect and found no significant effect on the emphasized hormone and behavioral outcomes.",
          badges: ["D-0001", "Ranehill_et_al_2015"],
          links: [
            { label: "D-0001", href: "../objects/dissents/D-0001.md" }
          ]
        },
        {
          title: "Internal collapse of support",
          kind: "dissent",
          body:
            "The first author later publicly stated that she no longer believed the effect was real. That is not just outside criticism; it is a break inside the original support structure.",
          badges: ["D-0002", "Dana_Carney_2016_statement"],
          links: [
            { label: "D-0002", href: "../objects/dissents/D-0002.md" }
          ]
        },
        {
          title: "Methodological attack",
          kind: "dissent",
          body:
            "The literature profile itself came under p-curve attack, challenging the evidentiary profile of the broader support environment rather than only one replication outcome.",
          badges: ["D-0003", "Simmons_Simonsohn_2016"],
          links: [
            { label: "D-0003", href: "../objects/dissents/D-0003.md" }
          ]
        },
        {
          title: "Lineage split",
          kind: "support",
          body:
            "The case does not behave like a clean live-or-die dispute. Instead, the pilot models a weaker surviving path as a separate descendant claim with its own verdict.",
          badges: ["C-0002", "V-0002"],
          links: [
            { label: "C-0002", href: "../objects/claims/C-0002.md" },
            { label: "V-0002", href: "../objects/verdicts/V-0002.md" }
          ]
        },
        {
          title: "Current verdict pair",
          kind: "status",
          body:
            "The current pilot reading does not canonize the original claim or the descendant claim. It renders a visible split: the original strong form is weakened; the weaker path remains contested but more viable.",
          badges: ["V-0001", "V-0002"],
          links: [
            { label: "V-0001", href: "../objects/verdicts/V-0001.md" },
            { label: "V-0002", href: "../objects/verdicts/V-0002.md" }
          ]
        }
      ]
    }
  ],
  timeline: [
    {
      year: "2010",
      title: "Original claim and publication context",
      body:
        "C-0001 and E-0001 mark the original strong-form claim, the original 2010 study context, and the first phase of public legitimacy."
    },
    {
      year: "2010–2012",
      title: "Amplification phase",
      body:
        "The claim moved from publication into wide public circulation. That amplification shaped the authority of the original result."
    },
    {
      year: "2015",
      title: "Large-sample empirical challenge",
      body:
        "D-0001 captures the later replication challenge associated with Ranehill et al. and the failure to recover the emphasized effect."
    },
    {
      year: "2016",
      title: "Internal collapse of support",
      body:
        "D-0002 records the public withdrawal of support by Dana Carney, marking a break inside the original support chain."
    },
    {
      year: "2016",
      title: "Methodological challenge",
      body:
        "D-0003 captures the p-curve attack on the surrounding literature profile."
    },
    {
      year: "Later",
      title: "Claim splitting",
      body:
        "C-0002 represents the weaker descendant claim, and V-0002 gives it its own institutional judgment."
    }
  ],
  sources: [
    {
      id: "Carney_Cuddy_Yap_2010",
      role: "Original strong-form claim source",
      usage: "C-0001, E-0001"
    },
    {
      id: "Ranehill_et_al_2015",
      role: "Major empirical replication challenge",
      usage: "D-0001"
    },
    {
      id: "Dana_Carney_2016_statement",
      role: "Internal withdrawal of support",
      usage: "D-0002, C-0002"
    },
    {
      id: "Simmons_Simonsohn_2016",
      role: "Methodological / meta-evidential attack",
      usage: "D-0003"
    },
    {
      id: "Early_public_amplification_context",
      role: "Public amplification context",
      usage: "E-0001"
    },
    {
      id: "TED_Corrections_2017",
      role: "Public-facing correction / reframing context",
      usage: "C-0002"
    }
  ],
  readingPath: [
    { label: "Snapshot v2", href: "../snapshots/snapshot-v2.md" },
    { label: "Verdict V-0001", href: "../objects/verdicts/V-0001.md" },
    { label: "Verdict V-0002", href: "../objects/verdicts/V-0002.md" },
    { label: "Claim C-0001", href: "../objects/claims/C-0001.md" },
    { label: "Claim C-0002", href: "../objects/claims/C-0002.md" },
    { label: "Timeline", href: "../timeline/events.md" },
    { label: "References", href: "../references.md" }
  ]
};
