const states = {
  landing: {
    label: 'Landing',
    case: 'shared',
    subtitle: 'Shared cockpit landing state for the two currently bound pilot cases.',
    status: { text: 'Two bound cases visible', tone: 'good' },
    cards: [
      {
        title: 'power-posing',
        body: 'First public-facing living case. Stronger seam, richer public-layer ecology, and clearer route plurality.'
      },
      {
        title: 'h-pylori-ulcer',
        body: 'Second case. Accepted first governed public layer, explicit orchestration boundary, and clean current-stage closeout.'
      },
      {
        title: 'Phase 1 demo rule',
        body: 'The prototype proves lawful case binding and state mapping, not production UI completeness.'
      }
    ],
    right: [
      {
        title: 'Current objective',
        body: 'Bind both cases into one cockpit frame without flattening their governed identities.'
      },
      {
        title: 'Visible pressure',
        body: 'Keep the sidecar subordinate and keep object-centered navigation in the foreground.'
      }
    ],
    sidecar: [
      'Choose a case and route.',
      'Do not start from blank chat.',
      'Founding-style exploration remains possible, but only as a sidecar workbench.'
    ]
  },
  hpClaim: {
    label: 'H. pylori / Claim focus',
    case: 'h-pylori-ulcer',
    subtitle: 'Claim-centered cockpit state anchored on the stronger causal claim.',
    status: { text: 'Current stage: accepted first governed public layer', tone: 'good' },
    cards: [
      {
        title: 'Claim focus',
        body: 'Helicobacter pylori is a major cause of chronic gastritis and many peptic ulcers.'
      },
      {
        title: 'Current judgment',
        body: 'The second case has an accepted current threshold with explicit orchestration boundary and six richer hardening lifts.'
      },
      {
        title: 'Next actions',
        bullets: [
          'scan missing evidence',
          'draft dissent response',
          'export progress summary'
        ]
      }
    ],
    right: [
      {
        title: 'Current pressure',
        bullets: [
          'biological plausibility resistance',
          'causality-direction objection',
          'over-generalization risk'
        ]
      },
      {
        title: 'Evidence anchors',
        bullets: [
          'early observation / cultivation breakthrough',
          'treatment response and recurrence change',
          'consensus and guideline-level uptake'
        ]
      }
    ],
    sidecar: [
      'Compare stronger claim and narrower descendant route.',
      'Draft focused response to causality objections.',
      'Keep full public release and page emission out of scope.'
    ]
  },
  hpVerdict: {
    label: 'H. pylori / Verdict boundary',
    case: 'h-pylori-ulcer',
    subtitle: 'Verdict-boundary state anchored on the current stage closeout and retained holds.',
    status: { text: 'Boundary honesty active', tone: 'warn' },
    cards: [
      {
        title: 'Current verdict floor',
        body: 'Accepted first governed public layer with explicit orchestration boundary.'
      },
      {
        title: 'Retained holds',
        bullets: [
          'HOLD_NO_FULL_PUBLIC_RELEASE',
          'HOLD_NO_PAGE_EMISSION_LAYER',
          'HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY',
          'HOLD_NO_REPOSITORY_WIDE_PUBLIC_LAYER_GENERALIZATION'
        ]
      },
      {
        title: 'Lawful movement rule',
        body: 'Wait for real forcing conditions rather than expanding by momentum or symmetry alone.'
      }
    ],
    right: [
      {
        title: 'What changed',
        body: 'Authorization is no longer the point. The current public layer is real, executable, and governed.'
      },
      {
        title: 'What is not claimed',
        bullets: [
          'not first-case equivalence',
          'not page emission',
          'not larger orchestration expansion',
          'not repo-wide generality'
        ]
      }
    ],
    sidecar: [
      'This is a verdict-boundary screen, not a hype screen.',
      'Keep non-upgrade honesty visible in the main object state.'
    ]
  },
  ppDissent: {
    label: 'Power posing / Dissent pressure',
    case: 'power-posing',
    subtitle: 'Dissent-centered cockpit state anchored on replication failure and downstream weakening.',
    status: { text: 'Dissent-rich claim neighborhood', tone: 'warn' },
    cards: [
      {
        title: 'Claim pressure center',
        body: 'Original strong-form power-posing claim under replication and methodological pressure.'
      },
      {
        title: 'Open dissent surfaces',
        bullets: [
          'replication failure and null effect pressure',
          'internal withdrawal-of-support pressure',
          'methodological / p-curve criticism'
        ]
      },
      {
        title: 'Descendant route',
        body: 'A weaker surviving descendant claim remains visible as a separate route rather than a fake verdict rescue.'
      }
    ],
    right: [
      {
        title: 'Why this case matters',
        body: 'It shows false elevation moving toward weakening, with visible claim splitting and dissent accumulation.'
      },
      {
        title: 'Candidate actions',
        bullets: [
          'draft dissent response',
          'compare original and descendant claims',
          'export route pressure summary'
        ]
      }
    ],
    sidecar: [
      'Use the sidecar to compare attack surfaces, not to replace the dissent ledger.',
      'The cockpit remains centered on the governed claim neighborhood.'
    ]
  },
  ppRoute: {
    label: 'Power posing / Route map',
    case: 'power-posing',
    subtitle: 'Route-centered state anchored on the richer public-layer and seam ecology.',
    status: { text: 'Richer public-layer ecology', tone: 'good' },
    cards: [
      {
        title: 'Public-layer route',
        bullets: [
          'snapshot-v2 public homepage',
          'claim-page index',
          'source-page index',
          'references and metadata surfaces',
          'template seam governance path'
        ]
      },
      {
        title: 'Why this route is valuable',
        body: 'It stress-tests navigation across claim, source, snapshot, and seam governance without collapsing into one flat page.'
      },
      {
        title: 'Cockpit role',
        body: 'This case provides the richer route / map reference for COCKPIT1-B and beyond.'
      }
    ],
    right: [
      {
        title: 'Route complexity',
        body: 'More route plurality and richer surface ecology than the second case.'
      },
      {
        title: 'Boundary reminder',
        body: 'The cockpit must not replace the existing public layer; it binds to it and reads from it.'
      }
    ],
    sidecar: [
      'Use this state to test route switching and object entry logic.',
      'Do not over-interpret this as generic multi-case readiness.'
    ]
  }
};

const stateOrder = ['landing', 'hpClaim', 'hpVerdict', 'ppDissent', 'ppRoute'];
const nav = document.getElementById('state-nav');
const titleEl = document.getElementById('screen-title');
const subtitleEl = document.getElementById('screen-subtitle');
const mainContent = document.getElementById('main-content');
const rightContent = document.getElementById('right-content');
const sidecarContent = document.getElementById('sidecar-content');

function renderCard(card) {
  const bullets = card.bullets
    ? `<ul>${card.bullets.map((item) => `<li>${item}</li>`).join('')}</ul>`
    : '';
  return `
    <article class="info-card">
      <h3>${card.title}</h3>
      ${card.body ? `<p>${card.body}</p>` : ''}
      ${bullets}
    </article>
  `;
}

function renderStack(card) {
  const bullets = card.bullets
    ? `<ul>${card.bullets.map((item) => `<li>${item}</li>`).join('')}</ul>`
    : '';
  return `
    <article class="stack-card">
      <h3>${card.title}</h3>
      ${card.body ? `<p>${card.body}</p>` : ''}
      ${bullets}
    </article>
  `;
}

function setState(key) {
  const state = states[key];
  titleEl.textContent = `${state.label}`;
  subtitleEl.textContent = `${state.subtitle}`;

  mainContent.innerHTML = `
    <div class="status-line ${state.status.tone}">${state.status.text}</div>
    <div class="info-grid">
      ${state.cards.map(renderCard).join('')}
    </div>
  `;

  rightContent.innerHTML = state.right.map(renderStack).join('');
  sidecarContent.innerHTML = `
    <div class="sidecar-note">
      <strong>Sidecar discipline</strong>
      <ul>${state.sidecar.map((item) => `<li>${item}</li>`).join('')}</ul>
    </div>
  `;

  document.querySelectorAll('.state-button').forEach((button) => {
    button.classList.toggle('active', button.dataset.state === key);
  });
}

stateOrder.forEach((key) => {
  const state = states[key];
  const button = document.createElement('button');
  button.className = 'state-button';
  button.dataset.state = key;
  button.innerHTML = `<strong>${state.label}</strong><small>${state.case}</small>`;
  button.addEventListener('click', () => setState(key));
  nav.appendChild(button);
});

setState('landing');
