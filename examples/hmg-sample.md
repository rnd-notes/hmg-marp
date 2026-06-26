---
marp: true
theme: hmg
paginate: true
---

<!-- _class: cover -->

# Standard report template

Month 00, 0000  
Management & Administration Division · Team Name

---

<span class="kicker">Agenda</span>

# Decision-ready presentation flow

<div class="cards">
  <div class="card"><h3>01 Context</h3><p>Frame the decision, audience, and operating constraints.</p></div>
  <div class="card"><h3>02 Findings</h3><p>Summarize evidence with concise, presentation-first language.</p></div>
  <div class="card"><h3>03 Actions</h3><p>Make ownership, sequence, and expected impact explicit.</p></div>
</div>

---

# Sample short headline

<div class="columns">
<div>

## Key message

This slide demonstrates a clean two-column content layout suitable for concise executive updates.

- Use one main idea per slide.
- Keep bullets short and action-oriented.
- Prefer tables, cards, or metrics over long paragraphs.

</div>
<div class="hmg-band">

<span class="metric">03</span>

Strong visual hierarchy helps readers find the point before reading details.

</div>
</div>

---

# Status overview

| Area | Current state | Next action |
| --- | --- | --- |
| Template | HMG style tokens extracted | Refine theme classes |
| Authoring | Markdown-first workflow | Add project decks |
| Output | HTML/PDF/PPTX via Marp CLI | Validate in CI |

---

# Content cards

<div class="cards">
  <div class="card"><h3>One</h3><p class="muted">Use card layouts for parallel points.</p></div>
  <div class="card"><h3>Two</h3><p class="muted">Keep each card to one concise idea.</p></div>
  <div class="card"><h3>Three</h3><p class="muted">Use accent classes only when they add signal.</p></div>
</div>

---

<!-- _class: divider -->

# Section divider

Use divider slides to reset attention between major sections.

---

# Implementation notes

```bash
npm run validate
npm run build
npm run build:all
```

- `themes/hmg.css` defines the theme.
- `examples/*.md` demonstrate usage.
- `docs/reference.md` records source template observations.

---

<!-- _class: cover -->

# Thank you

Responsible Person · Team Name
