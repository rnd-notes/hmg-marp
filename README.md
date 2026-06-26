# hmg-marp

HMG-style [Marp](https://github.com/marp-team/marp) presentation template project.

This repository provides a reusable Marp CSS theme, example Markdown decks, and validation/build scripts inspired by the local PowerPoint reference template:

```text
C:\Users\JoJoonhee\Desktop\ppt\hmg-template.pptx
```

The PowerPoint file itself is **not required** to render the examples after assets have been extracted into this repository.

## What is included

- `themes/hmg.css` — default HMG-style Marp theme.
- `examples/hmg-sample.md` — full sample deck showing cover, agenda, content, table, cards, and closing slides.
- `examples/hmg-wide.md` — compact feature-check deck.
- `assets/hmg-template-media/` — media extracted from the source PPTX.
- `docs/reference.md` — extracted reference facts: colors, fonts, slide counts, and Marp references.
- `.github/workflows/ci.yml` — validates and builds sample decks on GitHub Actions.

## Quick start

```bash
npm install
npm run validate
npm run build
```

Outputs are written to `dist/`.

To try PPTX export as well:

```bash
npm run build:all
```

## Use the theme in a deck

Create a Markdown file with Marp frontmatter:

```markdown
---
marp: true
theme: hmg
paginate: true
style: |
  @import url('../themes/hmg.css');
---

<!-- _class: cover -->

# Presentation title

Subtitle or metadata
```

Render with:

```bash
npx marp path/to/deck.md --theme themes/hmg.css --html -o deck.html
npx marp path/to/deck.md --theme themes/hmg.css --pdf -o deck.pdf
npx marp path/to/deck.md --theme themes/hmg.css --pptx -o deck.pptx
```

## Fonts and licensing

The original PPTX references Hyundai Sans font families. This repository does **not** redistribute proprietary font files. The CSS prefers locally installed Hyundai Sans fonts and falls back to Helvetica Neue, Arial, and sans-serif.

## Design notes

The PowerPoint template contains multiple layouts. Marp cannot exactly reproduce every PowerPoint layout, so this project focuses on reusable presentation patterns:

- dark HMG navy cover/divider slides;
- clean white content slides;
- strong title hierarchy;
- subtle footer/pagination;
- two-column layouts and card grids;
- accent utilities based on the extracted HMG color palette.

See `docs/reference.md` for extracted reference details.

## Related Marp projects

- [marp-team/marp](https://github.com/marp-team/marp)
- [marp-team/marp-cli](https://github.com/marp-team/marp-cli)
- [marp-team/marp-core](https://github.com/marp-team/marp-core)
- [marp-team/marpit](https://github.com/marp-team/marpit)
- [marp-team/awesome-marp](https://github.com/marp-team/awesome-marp)

## License

MIT
