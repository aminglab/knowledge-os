const style = document.createElement('style');
style.textContent = `
body { margin:0; font-family:Inter,system-ui,sans-serif; background:#0d1324; color:#eef2ff; }
.app-shell { max-width:1280px; margin:0 auto; padding:20px; }
.topbar { display:flex; justify-content:space-between; gap:16px; margin-bottom:16px; }
.pill,.badge { padding:6px 10px; border-radius:999px; border:1px solid #283252; background:#10162a; font-size:12px; }
.grid { display:grid; grid-template-columns:minmax(0,1fr) 340px; gap:16px; }
.panel { background:#131a2e; border:1px solid #283252; border-radius:18px; padding:16px; }
.result-card,.boundary-card,.audit-card { background:#18213a; border:1px solid #283252; border-radius:14px; padding:12px; margin-top:12px; }
.block { background:#10162a; border:1px solid #283252; border-radius:12px; padding:10px; margin-top:10px; }
ul { margin:8px 0 0; padding-left:18px; }
button { border:1px solid #283252; border-radius:12px; background:#18213a; color:#eef2ff; padding:10px 12px; cursor:pointer; }
@media (max-width:1100px){ .grid{grid-template-columns:1fr;} }
`;
document.head.appendChild(style);

const app = document.getElementById('app');
let mode = 'summary_review';
let auditLog = [
  'COCKPIT3-B-A entered: bounded review-boundary prototype lift.',
  'All current surfaces remain draft_only, surface_only, and non-executable at current stage.',
  'No current governed result surface is yet lawfully classified as operator_review_required.'
];

const candidates = {
  summary_review: {
    title: 'Progress summary draft',
    outputClass: 'summary_draft',
    summary: 'A bounded progress summary remains visible as a governed result surface.',
    review_trigger: 'handoff pressure is visible because the draft is likely to be reviewed for wording and bounded next-step framing',
    review_scope: ['wording only', 'bounded next-step suggestion only'],
    review_act: 'mark as review candidate for manual follow-up',
    review_trigger_family: 'export_surface_pressure',
    review_scope_family: 'export_only',
  },
  continuation_review: {
    title: 'Canonical continuation draft',
    outputClass: 'continuation_draft',
    summary: 'A bounded continuation suggestion remains visible without route commitment or execution.',
    review_trigger: 'route-ordering pressure is visible because the draft proposes a stronger next-step ordering',
    review_scope: ['routing only', 'bounded continuation wording only'],
    review_act: 'freeze for later handoff to a human operator',
    review_trigger_family: 'routing_handoff_pressure',
    review_scope_family: 'routing_only',
  }
};

function pushAudit(note) {
  auditLog = [note, ...auditLog].slice(0, 6);
}

function currentCandidate() {
  return candidates[mode];
}

function render() {
  const c = currentCandidate();
  app.innerHTML = `
  <div class="app-shell">
    <header class="topbar">
      <div>
        <div style="font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#8fb3ff;">Knowledge OS / COCKPIT3-B-A</div>
        <h1>Review Boundary Prototype Lift</h1>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <span class="pill">execution_boundary_class: draft_only</span>
        <span class="pill">action_posture: surface_only</span>
        <span class="pill">non-executable at current stage</span>
      </div>
    </header>

    <main class="grid">
      <section class="panel">
        <h2>Governed result surface</h2>
        <p>Current prototype target: make the review boundary visible without upgrading current result surfaces.</p>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button data-mode="summary_review">summary review candidate</button>
          <button data-mode="continuation_review">continuation review candidate</button>
        </div>
        <article class="result-card" data-governed-result="true">
          <h3>${c.title}</h3>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge">Output class: ${c.outputClass}</span>
            <span class="badge">Draft-only governed result</span>
            <span class="badge">review_trigger_family: ${c.review_trigger_family}</span>
            <span class="badge">review_scope_family: ${c.review_scope_family}</span>
          </div>
          <div class="block"><strong>Summary</strong><p>${c.summary}</p></div>
          <div class="block"><strong>Boundary honesty</strong><p>operator review is still not execution authority.</p></div>
          <div class="block"><strong>Current non-upgrade clause</strong><p>No current governed result surface is yet lawfully classified as operator_review_required.</p></div>
          <div class="block"><strong>Anti-overclaim</strong><p>No execute, commit, apply, resolve, or publish authority is opened here.</p></div>
        </article>
      </section>

      <aside class="panel">
        <h2>Review boundary sidecar</h2>
        <p>This sidecar names what a lawful review posture would have to contain.</p>
        <article class="boundary-card" data-review-boundary-sidecar="true">
          <div class="block"><strong>review_trigger</strong><p>${c.review_trigger}</p></div>
          <div class="block"><strong>review_trigger_family</strong><p>${c.review_trigger_family}</p></div>
          <div class="block"><strong>review_scope</strong><ul>${c.review_scope.map(i => `<li>${i}</li>`).join('')}</ul></div>
          <div class="block"><strong>review_scope_family</strong><p>${c.review_scope_family}</p></div>
          <div class="block"><strong>review_act</strong><p>${c.review_act}</p></div>
          <div class="block"><strong>retained_holds</strong><ul><li>HOLD_NO_LIVE_RUNTIME_COCKPIT</li><li>HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE</li><li>HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND</li></ul></div>
          <div class="block"><strong>Future class not yet opened</strong><p>No current governed result surface is yet lawfully classified as operator_review_required.</p></div>
        </article>
      </aside>
    </main>

    <section class="panel" style="margin-top:16px;">
      <h2>Audit log</h2>
      ${auditLog.map((entry, i) => `<article class="audit-card"><strong>${i === 0 ? 'Current audit note' : 'Recent audit note'}</strong><p>${entry}</p></article>`).join('')}
    </section>
  </div>`;

  document.querySelectorAll('button[data-mode]').forEach(btn => {
    btn.addEventListener('click', () => {
      mode = btn.dataset.mode;
      pushAudit(`${mode} surfaced a bounded review candidate with emitted family labels. operator review is still not execution authority. No current governed result surface is yet lawfully classified as operator_review_required.`);
      render();
    });
  });
}

render();
