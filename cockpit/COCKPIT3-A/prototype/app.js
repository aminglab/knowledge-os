const style = document.createElement('style');
style.textContent = `
body { margin:0; font-family:Inter,system-ui,sans-serif; background:#0d1324; color:#eef2ff; }
.app-shell { max-width:1360px; margin:0 auto; padding:20px; }
.topbar { display:flex; justify-content:space-between; gap:16px; margin-bottom:16px; }
.eyebrow { color:#8fb3ff; font-size:12px; text-transform:uppercase; letter-spacing:.08em; margin-bottom:6px; }
.topbar-meta,.result-meta { display:flex; gap:8px; flex-wrap:wrap; }
.pill,.badge { padding:6px 10px; border-radius:999px; border:1px solid #283252; background:#10162a; font-size:12px; }
.grid { display:grid; grid-template-columns:260px minmax(0,1fr) 320px; gap:16px; }
.panel { background:#131a2e; border:1px solid #283252; border-radius:18px; padding:16px; }
.anchor-nav,.trigger-panel,.result-surface,.governance-surface,.audit-log { display:grid; gap:12px; }
.anchor-button,.trigger-button { border:1px solid #283252; border-radius:14px; background:#18213a; color:#eef2ff; padding:12px; cursor:pointer; text-align:left; }
.anchor-button.active { border-color:#8fb3ff; }
.card,.result-card,.governance-card,.audit-card { background:#18213a; border:1px solid #283252; border-radius:14px; padding:12px; }
.result-block { background:#10162a; border:1px solid #283252; border-radius:12px; padding:10px; }
ul { margin:8px 0 0; padding-left:18px; }
@media (max-width:1180px){ .grid{grid-template-columns:1fr;} }
`;
document.head.appendChild(style);

const anchors = [
  { key: 'hpClaimCore', label: 'C-0001 stronger claim', type: 'claim anchor' },
  { key: 'hpStageVerdict', label: 'Stage verdict object', type: 'verdict anchor' },
  { key: 'ppPublicRoute', label: 'Public-layer route', type: 'route anchor' },
];
const triggerLabels = ['scan missing evidence','draft dissent response','check upgrade conditions','suggest canonical continuation','prepare progress summary'];
let currentAnchorKey = anchors[0].key;
let resultCard = null;
let auditLog = [
  'COCKPIT3-A entered: governance sidecar lift.',
  'Current holds remain active: HOLD_NO_LIVE_RUNTIME_COCKPIT and HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND.'
];

const app = document.getElementById('app');
app.innerHTML = `<div class="app-shell"><header class="topbar"><div><div class="eyebrow">Knowledge OS / COCKPIT3-A</div><h1>Governance Sidecar Lift</h1></div><div class="topbar-meta"><span class="pill">Execution boundary visible</span><span class="pill">All current results remain draft_only</span><span class="pill">Non-executable at current stage</span></div></header><main class="grid"><aside class="panel"><h2>Current anchors</h2><p>Bounded result surfaces remain tied to named anchors.</p><div id="anchor-nav" class="anchor-nav"></div></aside><section class="panel"><h2>Result surface</h2><p>Structured draft result cards remain visible, but now carry governance context.</p><div id="trigger-panel" class="trigger-panel"></div><div id="result-surface" class="result-surface"></div></section><aside class="panel"><h2>Governance sidecar</h2><p>Execution-boundary fields are visible, but no execution is authorized.</p><div id="governance-surface" class="governance-surface"></div></aside></main><section class="panel" style="margin-top:16px;"><h2>Audit log</h2><div id="audit-log" class="audit-log"></div></section></div>`;

const anchorNav = document.getElementById('anchor-nav');
const triggerPanel = document.getElementById('trigger-panel');
const resultSurface = document.getElementById('result-surface');
const governanceSurface = document.getElementById('governance-surface');
const auditEl = document.getElementById('audit-log');

const getCurrentAnchor = () => anchors.find(a => a.key === currentAnchorKey) || anchors[0];
const pushAudit = (note) => { auditLog = [note, ...auditLog].slice(0, 8); };

function buildResultCard(trigger, anchor) {
  const base = { anchor: anchor.label, draft: 'Draft-only', basis: ['current result surface is bounded', 'governance sidecar remains visible'], unresolved: ['no governed mutation is authorized', 'runtime remains unopened'], nextStep: ['surface for human review only', 'do not treat the card as execution authority'] };
  if (trigger === 'scan missing evidence') return { ...base, title: 'Missing-evidence scan', outputClass: 'scan_result', summary: 'A bounded missing-evidence scan remains visible as a governed result surface.', audit: 'Generated from a bounded scan trigger. No evidence object was created.' };
  if (trigger === 'draft dissent response') return { ...base, title: 'Dissent-response draft', outputClass: 'draft_response', summary: 'A bounded response draft remains visible without resolving the dissent.', audit: 'Generated from a bounded response-draft trigger. No dissent object was resolved.' };
  if (trigger === 'check upgrade conditions') return { ...base, title: 'Upgrade-condition check', outputClass: 'condition_check', summary: 'A bounded inspection result remains visible without upgrading claim or verdict state.', audit: 'Generated from a bounded inspection trigger. No claim or verdict was changed.' };
  if (trigger === 'suggest canonical continuation') return { ...base, title: 'Canonical continuation suggestion', outputClass: 'continuation_suggestion', summary: 'A bounded next-step ordering suggestion remains visible without executing anything.', audit: 'Generated from a bounded continuation trigger. No task was executed and no route was committed.' };
  return { ...base, title: 'Progress summary draft', outputClass: 'summary_draft', summary: 'A bounded recap remains visible without publication or export authority.', audit: 'Prepared as a draft-only recap. No publication or export occurred.' };
}

function renderAnchors() {
  anchorNav.innerHTML = anchors.map(a => `<button class="anchor-button ${a.key === currentAnchorKey ? 'active' : ''}" data-anchor="${a.key}"><strong>${a.label}</strong><div>${a.type}</div></button>`).join('');
  document.querySelectorAll('.anchor-button').forEach(btn => btn.addEventListener('click', () => { currentAnchorKey = btn.dataset.anchor; pushAudit(`Anchor switched to ${btn.dataset.anchor}. Governance sidecar remains draft_only.`); render(); }));
}

function renderTriggers() {
  triggerPanel.innerHTML = triggerLabels.map(label => `<button class="trigger-button" data-trigger="${label}">${label}</button>`).join('');
  document.querySelectorAll('.trigger-button').forEach(btn => btn.addEventListener('click', () => {
    const anchor = getCurrentAnchor();
    resultCard = buildResultCard(btn.dataset.trigger, anchor);
    pushAudit(`${btn.dataset.trigger} produced a governed result surface for ${anchor.label}. execution_boundary_class remains draft_only.`);
    renderResult();
    renderGovernance();
    renderAudit();
  }));
}

function renderResult() {
  if (!resultCard) {
    resultSurface.innerHTML = `<div class="card"><strong>No governed result selected yet.</strong><p>Run any trigger to render a structured result card and its governance sidecar.</p></div>`;
    return;
  }
  resultSurface.innerHTML = `<article class="result-card" data-governed-result="true"><h3>${resultCard.title}</h3><div class="result-meta"><span class="badge">Output class: ${resultCard.outputClass}</span><span class="badge">Anchor: ${resultCard.anchor}</span><span class="badge">${resultCard.draft}</span></div><div class="result-block"><strong>Summary</strong><p>${resultCard.summary}</p></div><div class="result-block"><strong>Basis hints</strong><ul>${resultCard.basis.map(i => `<li>${i}</li>`).join('')}</ul></div><div class="result-block"><strong>Unresolved remainder</strong><ul>${resultCard.unresolved.map(i => `<li>${i}</li>`).join('')}</ul></div><div class="result-block"><strong>Next-step hint</strong><ul>${resultCard.nextStep.map(i => `<li>${i}</li>`).join('')}</ul></div><div class="result-block"><strong>Audit trace note</strong><p>${resultCard.audit}</p></div></article>`;
}

function renderGovernance() {
  const anchor = getCurrentAnchor();
  governanceSurface.innerHTML = `<article class="governance-card" data-governance-sidecar="true"><h3>Governance sidecar</h3><div class="result-meta"><span class="badge">execution_boundary_class: draft_only</span><span class="badge">action_posture: surface_only</span></div><div class="result-block"><strong>Current default status</strong><p>non-executable at current stage</p></div><div class="result-block"><strong>Anchor context</strong><p>${anchor.label}</p></div><div class="result-block"><strong>Future classes not opened yet</strong><ul><li>operator_review_required</li><li>execution_forbidden</li></ul></div><div class="result-block"><strong>Anti-overclaim</strong><p>No execute, commit, apply, resolve, or publish authority is opened here.</p></div></article>`;
}

function renderAudit() {
  auditEl.innerHTML = auditLog.map((entry, i) => `<article class="audit-card"><h3>${i === 0 ? 'Current audit note' : 'Recent audit note'}</h3><p>${entry}</p></article>`).join('');
}

function render() { renderAnchors(); renderTriggers(); renderResult(); renderGovernance(); renderAudit(); }
render();
