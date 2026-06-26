---
marp: true
theme: hmg
paginate: true
footer: "2026. 06. 26"
---

<!-- _class: cover -->

<div class="cover-purpose"><span><b>○</b>Decision Making</span><span><b>●</b>Information Sharing</span><span><b>○</b>Directions</span></div>

# Decision-ready technical presentation

<div class="cover-meta">Month 00, 0000<br/>Management &amp; Administration Division<br/>Team Name</div>

---

<!-- _class: agenda -->

# Today’s flow

1. Frame the operating question and system boundary
2. Show the evidence in a readable technical layout
3. Convert findings into concrete actions and owners
4. Close with risks, validation, and next decision

---

<!-- _class: divider -->

# Part 1 — System context

---

<span class="kicker">Architecture</span>

# One message, two levels of detail

<div class="columns-2-1">
<div>

## Key message

Use the main column for the executive explanation. Keep the argument concise and let secondary details move into a rail.

- One idea per slide
- Explicit decision, risk, or status
- Supporting detail in tables, cards, or callouts

</div>
<div class="callout">

<span class="metric">03</span>

Reusable slide zones: title, evidence, and decision/action.

</div>
</div>

---

<!-- _class: table-heavy -->

<span class="kicker">Evidence</span>

# Technical status overview

| Area | Current state | Next action |
| --- | --- | --- |
| Template | HMG design tokens extracted | Apply reusable slide classes |
| Authoring | Markdown-first workflow | Add section rhythm and callouts |
| Output | HTML/PDF/PPTX via Marp CLI | Validate render in CI |
| Governance | Source PPTX retained locally | Avoid bundling proprietary fonts |

---

<!-- _class: bg-sand -->

<span class="kicker">Design system</span>

# Content cards with restrained accents

<div class="cards">
  <div class="card card--accent-blue"><h3>Clarity</h3><p class="muted">A smaller type scale keeps dense technical slides readable.</p></div>
  <div class="card card--accent-mint"><h3>Structure</h3><p class="muted">Divider, diagram, dense, table-heavy, and code-heavy classes reduce manual styling.</p></div>
  <div class="card card--accent-coral"><h3>Risk</h3><p class="muted">Use coral only for warnings or decision-critical caveats.</p></div>
</div>

---

<!-- _class: code-heavy -->

<span class="kicker">Implementation</span>

# Code-heavy slide support

<div class="code-split">
<div>

```bash
npm install
npm run validate
npm run build
npm run deck:pptx
```

</div>
<div class="callout sand">

## Why it works

The theme defines composable density modifiers instead of relying on one oversized base font.

</div>
</div>

---

<!-- _class: closing -->

# Thank you

<p class="subtitle">Responsible Person · Team Name</p>
