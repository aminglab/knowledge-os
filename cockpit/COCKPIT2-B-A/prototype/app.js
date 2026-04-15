const style = document.createElement('style');
style.textContent = `
body { margin:0; font-family:Inter,system-ui,sans-serif; background:#0d1324; color:#eef2ff; }
.app-shell { max-width:1440px; margin:0 auto; padding:20px; }
.topbar { display:flex; justify-content:space-between; gap:16px; margin-bottom:16px; }
.eyebrow { color:#8fb3ff; font-size:12px; text-transform:uppercase; letter-spacing:.08em; margin-bottom:6px; }
.topbar-meta,.lens-nav,.result-meta { display:flex; gap:8px; flex-wrap:wrap; }
.pill,.badge { padding:6px 10px; border-radius:999px; border:1px solid #283252; background:#10162a; font-size:12px; }
.cockpit-grid { display:grid; grid-template-columns:280px minmax(0,1fr) 340px; gap:16px; }
.panel,.panel-subsection { background:#131a2e; border:1px solid #283252; border-radius:18px; padding:16px; }
.panel-subsection{ margin-top:16px; }
.state-nav,.object-nav,.trigger-panel,.stack-list,.main-content,.result-surface,.sidecar-content { display:grid; gap:12px; }
.state-button,.object-button,.lens-button,.trigger-button { border:1px solid #283252; border-radius:14px; background:#18213a; color:#eef2ff; cursor:pointer; }
.state-button,.object-button { width:100%; text-align:left; padding:12px; }
.state-button.active,.object-button.active,.lens-button.active { border-color:#8fb3ff; }
.lens-bar { display:flex; justify-content:space-between; gap:16px; margin-bottom:16px; padding:12px; border:1px solid #283252; border-radius:16px; background:#10162a; }
.lens-button,.trigger-button { padding:10px 12px; }
.info-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:12px; }
.info-card,.stack-card,.trigger-card,.result-card,.audit-card,.result-block,.result-empty { background:#18213a; border:1px solid #283252; border-radius:14px; padding:12px; }
.status-line { display:inline-flex; padding:8px 10px; border-radius:12px; border:1px solid #283252; background:#10162a; margin-bottom:12px; }
ul { margin:8px 0 0; padding-left:18px; }
@media (max-width:1180px){ .cockpit-grid{grid-template-columns:1fr;} .lens-bar{flex-direction:column;} }
`;
document.head.appendChild(style);

const lenses={focus:{label:'Focus',description:'Foreground the active object and its nearest governed neighborhood.'},pressure:{label:'Pressure',description:'Foreground support, challenge, or route pressure around the active object.'},route:{label:'Route',description:'Foreground continuation paths, route plurality, and public-surface placement.'},boundary:{label:'Boundary',description:'Foreground retained holds, non-upgrade honesty, and visible verdict limits.'}};
const triggerLabels=['scan missing evidence','draft dissent response','check upgrade conditions','suggest canonical continuation','prepare progress summary'];
const states={landing:{label:'Landing',case:'shared',subtitle:'Shared cockpit landing state for the two currently bound pilot cases.',status:{text:'Two bound cases visible',tone:'good'},objects:[{key:'sharedRoute',label:'Shared route frame',type:'route anchor',focus:'One cockpit frame holds both currently bound cases without flattening their governed identities.',pressure:['sidecar must remain subordinate','state switching must stay object-centered'],route:['landing → h-pylori claim focus','landing → h-pylori verdict boundary','landing → power-posing dissent pressure'],boundary:['HOLD_NO_LIVE_RUNTIME_COCKPIT','HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND']},{key:'hpEntry',label:'H. pylori entry',type:'claim anchor',focus:'Second case with a cleaner current threshold and stronger verdict-boundary readability.',pressure:['causality-direction objection','over-generalization risk'],route:['claim focus path','verdict boundary path'],boundary:['no full public release claim','no page-emission upgrade']}] ,right:[{title:'Current objective',body:'Prove stronger interaction without opening runtime or write-capable mutation.'},{title:'Current upgrade',body:'COCKPIT2-B-A adds a first structured draft result-card lift.'}]},hpClaim:{label:'H. pylori / Claim focus',case:'h-pylori-ulcer',subtitle:'Claim-centered state anchored on the stronger causal claim.',status:{text:'Structured suggestion lift active',tone:'good'},objects:[{key:'hpClaimCore',label:'C-0001 stronger claim',type:'claim anchor',focus:'Helicobacter pylori is a major cause of chronic gastritis and many peptic ulcers.',pressure:['biological plausibility resistance','causality-direction objection'],route:['claim surface → verdict surface','stronger claim → narrower descendant path'],boundary:['accepted current threshold only','no full public release claim']},{key:'hpVerdictCurrent',label:'Current verdict floor',type:'verdict anchor',focus:'The second case stands at an accepted first governed public layer with explicit orchestration boundary.',pressure:['do not pretend first-case equivalence','do not over-extend the orchestration layer'],route:['claim focus → verdict boundary','verdict boundary → stage closeout'],boundary:['HOLD_NO_FULL_PUBLIC_RELEASE','HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY']}] ,right:[{title:'Current pressure',bullets:['causality-direction objection','over-generalization risk','current-threshold honesty']},{title:'Why this state matters',body:'It is the first trigger-result-card proving ground.'}]},hpVerdict:{label:'H. pylori / Verdict boundary',case:'h-pylori-ulcer',subtitle:'Verdict-boundary state anchored on current-stage honesty and retained holds.',status:{text:'Boundary honesty active',tone:'warn'},objects:[{key:'hpStageVerdict',label:'Stage verdict object',type:'verdict anchor',focus:'Accepted first governed public layer with explicit orchestration boundary.',pressure:['resist momentum-driven expansion','keep non-upgrade honesty visible'],route:['acceptance pass → richer hardening lifts','hardening lifts → stage closeout'],boundary:['HOLD_NO_FULL_PUBLIC_RELEASE','HOLD_NO_PAGE_EMISSION_LAYER','HOLD_NO_REPOSITORY_WIDE_PUBLIC_LAYER_GENERALIZATION']}] ,right:[{title:'Retained holds',bullets:['HOLD_NO_FULL_PUBLIC_RELEASE','HOLD_NO_PAGE_EMISSION_LAYER','HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY']}]},ppDissent:{label:'Power posing / Dissent pressure',case:'power-posing',subtitle:'Dissent-centered state anchored on replication failure and downstream weakening.',status:{text:'Dissent-rich claim neighborhood',tone:'warn'},objects:[{key:'ppClaimOriginal',label:'Original strong claim',type:'claim anchor',focus:'Original strong-form power-posing claim under replication and methodological pressure.',pressure:['replication failure and null effect pressure','internal withdrawal-of-support pressure'],route:['original claim → weaker descendant claim','claim pressure → route plurality'],boundary:['do not fake verdict rescue','keep lineage split visible']}] ,right:[{title:'Pressure profile',bullets:['replication failure','internal withdrawal of support','methodological / p-curve attack']}]},ppRoute:{label:'Power posing / Route map',case:'power-posing',subtitle:'Route-centered state anchored on the richer public-layer and seam ecology.',status:{text:'Richer public-layer ecology',tone:'good'},objects:[{key:'ppPublicRoute',label:'Public-layer route',type:'route anchor',focus:'Snapshot, claim pages, source pages, metadata, and seam documents form a richer route ecology.',pressure:['route plurality is harder to browse cleanly','must not flatten surfaces into one page'],route:['snapshot-v2 public homepage','claim-page index','source-page index','template seam governance path'],boundary:['cockpit binds to the public layer','cockpit does not substitute for the public layer']}] ,right:[{title:'Route complexity',body:'This case remains the richer route / map reference for cockpit navigation.'}]}};

let currentStateKey='landing';
let currentLensKey='focus';
let currentObjectKey=states[currentStateKey].objects[0].key;
let auditLog=['COCKPIT2-B-A entered: first structured result-card lift.','Current holds remain active: HOLD_NO_LIVE_RUNTIME_COCKPIT and HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND.'];
let resultCard=null;

const app=document.getElementById('app');
app.innerHTML=`<div class="app-shell"><header class="topbar"><div><div class="eyebrow">Knowledge OS / COCKPIT2-B-A</div><h1>First Structured Result-Card Lift</h1></div><div class="topbar-meta"><span class="pill">Mode: Cockpit</span><span class="pill">Structured suggestion surface</span><span class="pill">Draft-only / no runtime / no mutation</span></div></header><main class="cockpit-grid"><aside class="left-rail panel"><div class="panel-header"><h2>States</h2><p>Five bound screen states retained from the current cockpit line</p></div><nav id="state-nav" class="state-nav"></nav><div class="panel-header"><h2>Object anchors</h2><p>Current case-scoped anchors</p></div><div id="object-nav" class="object-nav"></div></aside><section class="main-panel panel"><div class="panel-header"><h2 id="screen-title">Screen</h2><p id="screen-subtitle"></p></div><div class="lens-bar"><div><strong>Lens switch</strong><p>Foreground changes only. Governed object state does not mutate.</p></div><div id="lens-nav" class="lens-nav"></div></div><div id="main-content" class="main-content"></div><section class="result-section panel-subsection"><div class="panel-header"><h2>Draft Result Surface</h2><p>First cockpit-native structured draft result card</p></div><div id="result-surface" class="result-surface"></div></section></section><aside class="right-rail panel"><div class="panel-header"><h2>Triggers / Pressure / Boundary</h2><p>Structured results stay draft-only and non-authoritative</p></div><div id="trigger-panel" class="trigger-panel"></div><div id="right-content" class="stack-list"></div></aside></main><section class="sidecar panel"><div class="panel-header"><h2>Sidecar Audit Log</h2><p>Audit visibility remains even when a richer result card is shown</p></div><div id="sidecar-content" class="sidecar-content"></div></section></div>`;

const stateNav=document.getElementById('state-nav');
const objectNav=document.getElementById('object-nav');
const lensNav=document.getElementById('lens-nav');
const titleEl=document.getElementById('screen-title');
const subtitleEl=document.getElementById('screen-subtitle');
const mainContent=document.getElementById('main-content');
const rightContent=document.getElementById('right-content');
const triggerPanel=document.getElementById('trigger-panel');
const sidecarContent=document.getElementById('sidecar-content');
const resultSurface=document.getElementById('result-surface');

const getCurrentState=()=>states[currentStateKey];
const getCurrentObject=()=>getCurrentState().objects.find(o=>o.key===currentObjectKey)||getCurrentState().objects[0];
const pushAudit=(note)=>{ auditLog=[note,...auditLog].slice(0,6); };
const infoCard=(title,body='',bullets=[])=>`<article class="info-card"><h3>${title}</h3>${body?`<p>${body}</p>`:''}${bullets.length?`<ul>${bullets.map(i=>`<li>${i}</li>`).join('')}</ul>`:''}</article>`;
const stackCard=(card)=>infoCard(card.title,card.body||'',card.bullets||[]);

function buildResultCard(trigger, object) {
  if (trigger === 'check upgrade conditions') {
    return {
      title: 'Upgrade-condition check',
      outputClass: 'condition_check',
      anchor: object.label,
      summary: 'Current surface does not warrant a governed upgrade. The present route supports a bounded inspection result only.',
      basis: ['current threshold remains explicit','retained holds remain visible','no forcing condition for upgrade is currently shown'],
      unresolved: ['stronger basis for upgrade remains absent','current prototype still forbids frontend mutation'],
      nextStep: ['keep the verdict-boundary surface visible','continue with draft-only cockpit guidance'],
      audit: 'Generated from a bounded inspection trigger. No claim or verdict was changed.'
    };
  }
  if (trigger === 'prepare progress summary') {
    return {
      title: 'Progress summary draft',
      outputClass: 'summary_draft',
      anchor: object.label,
      summary: 'The cockpit currently supports bounded state switching, bounded lens switching, bounded object browsing, and a first structured result-card surface.',
      basis: ['interactive floor already passed','smoke route already survived'],
      unresolved: ['structured result-card coverage is still narrow','runtime remains out of scope'],
      nextStep: ['extend the result-card pattern to more triggers only if current honesty remains intact'],
      audit: 'Prepared as a draft-only recap. No publication or export occurred.'
    };
  }
  return null;
}

function renderStates(){
  stateNav.innerHTML=Object.entries(states).map(([k,s])=>`<button class="state-button ${k===currentStateKey?'active':''}" data-state="${k}"><strong>${s.label}</strong><small>${s.case}</small></button>`).join('');
  document.querySelectorAll('.state-button').forEach(btn=>btn.addEventListener('click',()=>{currentStateKey=btn.dataset.state; currentObjectKey=getCurrentState().objects[0].key; pushAudit(`State switched to ${btn.dataset.state}; active object anchor reset to first case-scoped object.`); render();}));
}
function renderObjects(){
  const state=getCurrentState();
  objectNav.innerHTML=state.objects.map(o=>`<button class="object-button ${o.key===currentObjectKey?'active':''}" data-object="${o.key}"><strong>${o.label}</strong><small>${o.type}</small></button>`).join('');
  document.querySelectorAll('.object-button').forEach(btn=>btn.addEventListener('click',()=>{currentObjectKey=btn.dataset.object; pushAudit(`Object anchor switched to ${btn.dataset.object} under ${currentLensKey} lens.`); render();}));
}
function renderLenses(){
  lensNav.innerHTML=Object.entries(lenses).map(([k,l])=>`<button class="lens-button ${k===currentLensKey?'active':''}" data-lens="${k}">${l.label}</button>`).join('');
  document.querySelectorAll('.lens-button').forEach(btn=>btn.addEventListener('click',()=>{currentLensKey=btn.dataset.lens; pushAudit(`Lens switched to ${btn.dataset.lens}; active object anchor preserved.`); render();}));
}
function renderMain(){
  const state=getCurrentState(); const object=getCurrentObject(); const lens=currentLensKey;
  titleEl.textContent=state.label; subtitleEl.textContent=state.subtitle;
  const cards=[infoCard('Active object',`${object.label} · ${object.type}`), infoCard('Lens posture',lenses[lens].description)];
  if(lens==='focus'){ cards.push(infoCard('Focus surface',object.focus)); }
  if(lens==='pressure'){ cards.push(infoCard('Pressure surface','',object.pressure)); }
  if(lens==='route'){ cards.push(infoCard('Route surface','',object.route)); }
  if(lens==='boundary'){ cards.push(infoCard('Boundary surface','',object.boundary)); }
  cards.push(infoCard('Bounded route reminder','Foreground may change. Governed object state does not mutate.'));
  mainContent.innerHTML=`<div class="status-line">${state.status.text}</div><div class="info-grid">${cards.join('')}</div>`;
}
function renderRight(){ rightContent.innerHTML=getCurrentState().right.map(stackCard).join(''); }
function renderResult(){
  if(!resultCard){ resultSurface.innerHTML=`<div class="result-empty"><strong>No structured draft result yet.</strong><p>Run <code>check upgrade conditions</code> or <code>prepare progress summary</code> to generate the first cockpit-native draft result card.</p></div>`; return; }
  resultSurface.innerHTML=`<article class="result-card" data-result-card="true"><h3>${resultCard.title}</h3><div class="result-meta"><span class="badge class">Output class: ${resultCard.outputClass}</span><span class="badge anchor">Anchor: ${resultCard.anchor}</span><span class="badge draft">Draft-only</span></div><div class="result-block"><strong>Summary</strong><p>${resultCard.summary}</p></div><div class="result-block"><strong>Basis hints</strong><ul>${resultCard.basis.map(i=>`<li>${i}</li>`).join('')}</ul></div><div class="result-block"><strong>Unresolved remainder</strong><ul>${resultCard.unresolved.map(i=>`<li>${i}</li>`).join('')}</ul></div><div class="result-block"><strong>Next-step hint</strong><ul>${resultCard.nextStep.map(i=>`<li>${i}</li>`).join('')}</ul></div><div class="result-block"><strong>Audit trace note</strong><p>${resultCard.audit}</p></div></article>`;
}
function renderTriggers(){
  triggerPanel.innerHTML=triggerLabels.map(label=>`<article class="trigger-card"><h3>${label}</h3><p>Suggestion-layer only. No governed object mutation is committed from this surface.</p><button class="trigger-button" data-trigger="${label}">Run draft-only trigger</button></article>`).join('');
  document.querySelectorAll('.trigger-button').forEach(btn=>btn.addEventListener('click',()=>{ const object=getCurrentObject(); const label=btn.dataset.trigger; const card=buildResultCard(label, object); if(card){ resultCard=card; pushAudit(`${label} produced a structured draft result card for ${object.label}. Output class remains draft-only / suggestion-layer.`); } else { pushAudit(`${label} prepared for ${object.label}. Output class remains draft-only / suggestion-layer.`); } renderResult(); renderAudit(); }));
}
function renderAudit(){ sidecarContent.innerHTML=auditLog.map((entry,i)=>`<article class="audit-card"><h3>${i===0?'Current audit note':'Recent audit note'}</h3><p><strong>Draft-only:</strong> ${entry}</p></article>`).join(''); }
function render(){ renderStates(); renderObjects(); renderLenses(); renderMain(); renderRight(); renderTriggers(); renderResult(); renderAudit(); }
render();
