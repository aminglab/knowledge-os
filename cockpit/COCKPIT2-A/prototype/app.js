const lenses = {
  focus: {
    label: 'Focus',
    description: 'Foreground the active object and its nearest governed neighborhood.'
  },
  pressure: {
    label: 'Pressure',
    description: 'Foreground support, challenge, or route pressure around the active object.'
  },
  route: {
    label: 'Route',
    description: 'Foreground continuation paths, route plurality, and public-surface placement.'
  },
  boundary: {
    label: 'Boundary',
    description: 'Foreground retained holds, non-upgrade honesty, and visible verdict limits.'
  }
};

const triggerLabels = [
  'scan missing evidence',
  'draft dissent response',
  'check upgrade conditions',
  'suggest canonical continuation',
  'prepare progress summary'
];

const states = {
  landing: {
    label: 'Landing',
    case: 'shared',
    subtitle: 'Shared cockpit landing state for the two currently bound pilot cases.',
    status: { text: 'Two bound cases visible', tone: 'good' },
    objects: [
      {
        key: 'sharedRoute',
        label: 'Shared route frame',
        type: 'route anchor',
        focus: 'One cockpit frame holds both currently bound cases without flattening their governed identities.',
        pressure: [
          'sidecar must remain subordinate',
          'state switching must stay object-centered'
        ],
        route: [
          'landing → h-pylori claim focus',
          'landing → h-pylori verdict boundary',
          'landing → power-posing dissent pressure',
          'landing → power-posing route map'
        ],
        boundary: [
          'HOLD_NO_LIVE_RUNTIME_COCKPIT',
          'HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND'
        ]
      },
      {
        key: 'hpEntry',
        label: 'H. pylori entry',
        type: 'claim anchor',
        focus: 'Second case with a cleaner current threshold and stronger verdict-boundary readability.',
        pressure: [
          'causality-direction objection',
          'over-generalization risk'
        ],
        route: [
          'claim focus path',
          'verdict boundary path'
        ],
        boundary: [
          'no full public release claim',
          'no page-emission upgrade'
        ]
      },
      {
        key: 'ppEntry',
        label: 'Power-posing entry',
        type: 'route anchor',
        focus: 'First case with richer public-layer ecology, route plurality, and dissent density.',
        pressure: [
          'replication failure pressure',
          'methodological attack pressure'
        ],
        route: [
          'dissent pressure path',
          'route map path'
        ],
        boundary: [
          'cockpit reads from the public layer',
          'cockpit does not replace the public layer'
        ]
      }
    ],
    right: [
      {
        title: 'Current objective',
        body: 'Prove stronger interaction without opening runtime or write-capable mutation.'
      },
      {
        title: 'Interaction upgrade',
        body: 'COCKPIT2-A adds a bounded lens switch, bounded object browse, and suggestion-layer triggers.'
      }
    ]
  },
  hpClaim: {
    label: 'H. pylori / Claim focus',
    case: 'h-pylori-ulcer',
    subtitle: 'Claim-centered state anchored on the stronger causal claim and its nearest governed neighborhood.',
    status: { text: 'Interactive focus lift active', tone: 'good' },
    objects: [
      {
        key: 'hpClaimCore',
        label: 'C-0001 stronger claim',
        type: 'claim anchor',
        focus: 'Helicobacter pylori is a major cause of chronic gastritis and many peptic ulcers.',
        pressure: [
          'biological plausibility resistance',
          'causality-direction objection'
        ],
        route: [
          'stronger claim → narrower descendant path',
          'claim surface → verdict surface'
        ],
        boundary: [
          'accepted current threshold only',
          'no full public release claim'
        ]
      },
      {
        key: 'hpEvidenceTreatment',
        label: 'Treatment response evidence',
        type: 'evidence anchor',
        focus: 'Treatment response and recurrence change strengthen the causal reading rather than mere co-presence.',
        pressure: [
          'requires careful causal wording',
          'must not over-generalize to all stomach disease'
        ],
        route: [
          'evidence anchor → claim support',
          'evidence anchor → consensus uptake'
        ],
        boundary: [
          'frontend may foreground evidence',
          'frontend may not create authoritative evidence objects'
        ]
      },
      {
        key: 'hpVerdictCurrent',
        label: 'Current verdict floor',
        type: 'verdict anchor',
        focus: 'The second case currently stands at an accepted first governed public layer with explicit orchestration boundary.',
        pressure: [
          'do not pretend first-case equivalence',
          'do not over-extend the orchestration layer'
        ],
        route: [
          'claim focus → verdict boundary',
          'verdict boundary → stage closeout'
        ],
        boundary: [
          'HOLD_NO_FULL_PUBLIC_RELEASE',
          'HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY'
        ]
      }
    ],
    right: [
      {
        title: 'Current pressure',
        bullets: [
          'causality-direction objection',
          'over-generalization risk',
          'current-threshold honesty'
        ]
      },
      {
        title: 'Why this state matters',
        body: 'It proves that stronger claim navigation can remain object-centered and boundary-aware.'
      }
    ]
  },
  hpVerdict: {
    label: 'H. pylori / Verdict boundary',
    case: 'h-pylori-ulcer',
    subtitle: 'Verdict-boundary state anchored on current-stage honesty and retained holds.',
    status: { text: 'Boundary honesty active', tone: 'warn' },
    objects: [
      {
        key: 'hpStageVerdict',
        label: 'Stage verdict object',
        type: 'verdict anchor',
        focus: 'Accepted first governed public layer with explicit orchestration boundary.',
        pressure: [
          'resist momentum-driven expansion',
          'keep non-upgrade honesty visible'
        ],
        route: [
          'acceptance pass → richer hardening lifts',
          'hardening lifts → stage closeout'
        ],
        boundary: [
          'HOLD_NO_FULL_PUBLIC_RELEASE',
          'HOLD_NO_PAGE_EMISSION_LAYER',
          'HOLD_NO_REPOSITORY_WIDE_PUBLIC_LAYER_GENERALIZATION'
        ]
      },
      {
        key: 'hpDissentCausality',
        label: 'Causality objection',
        type: 'dissent anchor',
        focus: 'Even if bacteria are present, causality and not mere association must be defended.',
        pressure: [
          'demands careful response drafting',
          'demands bounded evidence reading'
        ],
        route: [
          'dissent object → response draft posture',
          'response draft posture → basis check'
        ],
        boundary: [
          'draft only',
          'no frontend resolution'
        ]
      }
    ],
    right: [
      {
        title: 'Retained holds',
        bullets: [
          'HOLD_NO_FULL_PUBLIC_RELEASE',
          'HOLD_NO_PAGE_EMISSION_LAYER',
          'HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY'
        ]
      },
      {
        title: 'Lawful movement rule',
        body: 'Wait for real forcing conditions rather than expanding by symmetry or optimism.'
      }
    ]
  },
  ppDissent: {
    label: 'Power posing / Dissent pressure',
    case: 'power-posing',
    subtitle: 'Dissent-centered state anchored on replication failure and downstream weakening.',
    status: { text: 'Dissent-rich claim neighborhood', tone: 'warn' },
    objects: [
      {
        key: 'ppClaimOriginal',
        label: 'Original strong claim',
        type: 'claim anchor',
        focus: 'Original strong-form power-posing claim under replication and methodological pressure.',
        pressure: [
          'replication failure and null effect pressure',
          'internal withdrawal-of-support pressure'
        ],
        route: [
          'original claim → weaker descendant claim',
          'claim pressure → route plurality'
        ],
        boundary: [
          'do not fake verdict rescue',
          'keep lineage split visible'
        ]
      },
      {
        key: 'ppDissentReplication',
        label: 'Replication challenge',
        type: 'dissent anchor',
        focus: 'Replication pressure is central, visible, and not reducible to a comment thread.',
        pressure: [
          'null effect replication',
          'public over-amplification hangover'
        ],
        route: [
          'dissent → response posture',
          'dissent → weakened verdict reading'
        ],
        boundary: [
          'draft only',
          'no claim rewriting from the frontend'
        ]
      },
      {
        key: 'ppDescendant',
        label: 'Weaker descendant route',
        type: 'route anchor',
        focus: 'A weaker surviving descendant remains visible as lineage rather than fake verdict repair.',
        pressure: [
          'must not collapse descendant into original claim',
          'must keep route plurality readable'
        ],
        route: [
          'claim split → descendant route',
          'descendant route → current visible judgment'
        ],
        boundary: [
          'lineage not verdict camouflage',
          'cockpit may foreground but not rewrite lineage'
        ]
      }
    ],
    right: [
      {
        title: 'Pressure profile',
        bullets: [
          'replication failure',
          'internal withdrawal of support',
          'methodological / p-curve attack'
        ]
      },
      {
        title: 'Why this state matters',
        body: 'It proves stronger pressure browsing without replacing the dissent ledger with generic chat.'
      }
    ]
  },
  ppRoute: {
    label: 'Power posing / Route map',
    case: 'power-posing',
    subtitle: 'Route-centered state anchored on the richer public-layer and seam ecology.',
    status: { text: 'Richer public-layer ecology', tone: 'good' },
    objects: [
      {
        key: 'ppPublicRoute',
        label: 'Public-layer route',
        type: 'route anchor',
        focus: 'Snapshot, claim pages, source pages, metadata, and seam documents form a richer route ecology.',
        pressure: [
          'route plurality is harder to browse cleanly',
          'must not flatten surfaces into one page'
        ],
        route: [
          'snapshot-v2 public homepage',
          'claim-page index',
          'source-page index',
          'template seam governance path'
        ],
        boundary: [
          'cockpit binds to the public layer',
          'cockpit does not substitute for the public layer'
        ]
      },
      {
        key: 'ppSourceRoute',
        label: 'Source-page route',
        type: 'source anchor',
        focus: 'Source surfaces help pressure-test route switching across richer public ecology.',
        pressure: [
          'reader path and governance path must stay distinct',
          'source semantics must stay case-scoped'
        ],
        route: [
          'source page → case usage',
          'source page → object usage',
          'source page → public reading routes'
        ],
        boundary: [
          'no repo-wide generalization claim',
          'no production frontend claim'
        ]
      }
    ],
    right: [
      {
        title: 'Route complexity',
        body: 'This case remains the richer route / map reference for cockpit navigation.'
      },
      {
        title: 'Boundary reminder',
        body: 'The cockpit reads across route surfaces; it does not replace them.'
      }
    ]
  }
};

let currentStateKey = 'landing';
let currentLensKey = 'focus';
let currentObjectKey = states[currentStateKey].objects[0].key;
let auditLog = [
  'COCKPIT2-A entered: stronger interaction under stricter honesty.',
  'Current holds remain active: HOLD_NO_LIVE_RUNTIME_COCKPIT and HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND.'
];

const stateNav = document.getElementById('state-nav');
const objectNav = document.getElementById('object-nav');
const lensNav = document.getElementById('lens-nav');
const titleEl = document.getElementById('screen-title');
const subtitleEl = document.getElementById('screen-subtitle');
const mainContent = document.getElementById('main-content');
const rightContent = document.getElementById('right-content');
const triggerPanel = document.getElementById('trigger-panel');
const sidecarContent = document.getElementById('sidecar-content');

function getCurrentState() {
  return states[currentStateKey];
}

function getCurrentObject() {
  return getCurrentState().objects.find((obj) => obj.key === currentObjectKey) || getCurrentState().objects[0];
}

function pushAudit(note) {
  auditLog = [note, ...auditLog].slice(0, 6);
}

function renderInfoCard(title, body, bullets = []) {
  return `
    <article class="info-card">
      <h3>${title}</h3>
      ${body ? `<p>${body}</p>` : ''}
      ${bullets.length ? `<ul>${bullets.map((item) => `<li>${item}</li>`).join('')}</ul>` : ''}
    </article>
  `;
}

function renderStackCard(card) {
  return renderInfoCard(card.title, card.body || '', card.bullets || []);
}

function renderTriggerCard(label) {
  return `
    <article class="trigger-card">
      <h3>${label}</h3>
      <p>Suggestion-layer only. No governed object mutation is committed from this surface.</p>
      <button class="trigger-button" data-trigger="${label}">Run draft-only trigger</button>
    </article>
  `;
}

function renderAuditLog() {
  sidecarContent.innerHTML = auditLog
    .map(
      (entry, index) => `
        <article class="audit-card">
          <h3>${index === 0 ? 'Current audit note' : 'Recent audit note'}</h3>
          <p><strong>Draft-only:</strong> ${entry}</p>
        </article>
      `
    )
    .join('');
}

function buildLensCards(state, object) {
  const lens = currentLensKey;
  const cards = [
    renderInfoCard('Active object', `${object.label} · ${object.type}`),
    renderInfoCard('Lens posture', lenses[lens].description),
  ];

  if (lens === 'focus') {
    cards.push(renderInfoCard('Focus surface', object.focus));
    cards.push(renderInfoCard('Bounded route reminder', 'Foreground may change. Governed object state does not mutate.'));
  }

  if (lens === 'pressure') {
    cards.push(renderInfoCard('Pressure surface', '', object.pressure));
    cards.push(renderInfoCard('Pressure discipline', 'Pressure is surfaced as governed challenge/support context, not as generic comment flow.'));
  }

  if (lens === 'route') {
    cards.push(renderInfoCard('Route surface', '', object.route));
    cards.push(renderInfoCard('Route discipline', `Current case: ${state.case}. The cockpit may foreground route plurality without claiming repository-wide cockpit generality.`));
  }

  if (lens === 'boundary') {
    cards.push(renderInfoCard('Boundary surface', '', object.boundary));
    cards.push(renderInfoCard('Retained honesty', 'No live runtime. No write-capable cockpit surface. No object mutation from the frontend.'));
  }

  return cards.join('');
}

function renderObjects() {
  const state = getCurrentState();
  objectNav.innerHTML = state.objects
    .map(
      (object) => `
        <button class="object-button ${object.key === currentObjectKey ? 'active' : ''}" data-object="${object.key}">
          <strong>${object.label}</strong>
          <small>${object.type}</small>
        </button>
      `
    )
    .join('');

  document.querySelectorAll('.object-button').forEach((button) => {
    button.addEventListener('click', () => {
      currentObjectKey = button.dataset.object;
      pushAudit(`Object anchor switched to ${button.dataset.object} under ${currentLensKey} lens.`);
      render();
    });
  });
}

function renderStates() {
  stateNav.innerHTML = Object.entries(states)
    .map(
      ([key, state]) => `
        <button class="state-button ${key === currentStateKey ? 'active' : ''}" data-state="${key}">
          <strong>${state.label}</strong>
          <small>${state.case}</small>
        </button>
      `
    )
    .join('');

  document.querySelectorAll('.state-button').forEach((button) => {
    button.addEventListener('click', () => {
      currentStateKey = button.dataset.state;
      currentObjectKey = getCurrentState().objects[0].key;
      pushAudit(`State switched to ${button.dataset.state}; active object anchor reset to first case-scoped object.`);
      render();
    });
  });
}

function renderLenses() {
  lensNav.innerHTML = Object.entries(lenses)
    .map(
      ([key, lens]) => `
        <button class="lens-button ${key === currentLensKey ? 'active' : ''}" data-lens="${key}">${lens.label}</button>
      `
    )
    .join('');

  document.querySelectorAll('.lens-button').forEach((button) => {
    button.addEventListener('click', () => {
      currentLensKey = button.dataset.lens;
      pushAudit(`Lens switched to ${button.dataset.lens}; active object anchor preserved.`);
      render();
    });
  });
}

function renderTriggers() {
  triggerPanel.innerHTML = triggerLabels.map(renderTriggerCard).join('');
  document.querySelectorAll('.trigger-button').forEach((button) => {
    button.addEventListener('click', () => {
      const object = getCurrentObject();
      pushAudit(`${button.dataset.trigger} prepared for ${object.label}. Output class remains draft-only / suggestion-layer.`);
      renderAuditLog();
    });
  });
}

function renderMain() {
  const state = getCurrentState();
  const object = getCurrentObject();
  titleEl.textContent = state.label;
  subtitleEl.textContent = state.subtitle;
  mainContent.innerHTML = `
    <div class="status-line ${state.status.tone}">${state.status.text}</div>
    <div class="info-grid">
      ${buildLensCards(state, object)}
    </div>
  `;
}

function renderRight() {
  const state = getCurrentState();
  rightContent.innerHTML = state.right.map(renderStackCard).join('');
}

function render() {
  renderStates();
  renderObjects();
  renderLenses();
  renderMain();
  renderRight();
  renderTriggers();
  renderAuditLog();
}

render();
