# HMG template reference

Source inspected locally: `C:\Users\JoJoonhee\Desktop\ppt\hmg-template.pptx`

## Extracted PPTX structure

- Slides: 11
- Slide layouts: 15
- Slide masters: 1
- Embedded media files: 3

Extracted media is stored under `assets/hmg-template-media/`.

## Observed color values

- `#000000`
- `#0000FF`
- `#002C5F`
- `#00A2FF`
- `#16E7CF`
- `#5E5E5E`
- `#61D836`
- `#8D8778`
- `#AEA99B`
- `#C6C1B7`
- `#D5D5D5`
- `#E4DCD3`
- `#FF00FF`
- `#FF42A1`
- `#FF644E`
- `#FFD932`
- `#FFFFFF`

## Observed font names

- `+mn-cs`
- `+mn-ea`
- `+mn-lt`
- `Aptos`
- `Arial`
- `Helvetica Neue`
- `Helvetica Neue Medium`
- `Hyundai Sans Head KR`
- `Hyundai Sans Head KR Medium`
- `Hyundai Sans Head Office`
- `Hyundai Sans Head Office Medium`
- `Hyundai Sans Text KR`
- `Hyundai Sans Text Office`
- `Hyundai Sans Text Office Medium`
- `현대산스 Text`

## Sample extracted text

- ○ Decision Making
- ● Information Sharing
- ○ Directions
- Standard report template
- Month 00, 0000
- Management &amp; Administration Division
- Team Name
- ○ Decision Making
- ● Information Sharing
- ○ Directions
- Standard report template
- Responsible Person
- Head of Group
- Head of Division
- Head of Department
- Cooperative Dept. 1
- Cooperative Dept. 2
- Cooperative Dept. 3
- Notes
- Month 00, 0000
- Management &amp; Administration Division
- Team Name
- 03
- Sample short headline
- This is a very long sample sub headline with two lines. This is a very long sample sub headline with two lines. This is a very long sample sub headline with two lines. 

## Marp reference projects reviewed

- `marp-team/marp` — entrance repository for the Marp Markdown presentation ecosystem.
- `marp-team/marp-cli` — CLI converter used by this project.
- `marp-team/marp-core` — core converter.
- `marp-team/marpit` — framework for Markdown slide decks.
- `marp-team/awesome-marp` — curated examples and ecosystem references.
- Third-party references: `favourhong/Awesome-Marp`, `yoanbernabeu/MARP-Template-Library`, `NYPL/nypl-marp-template`, `michaelfery/marp-template`, `danielcregg/marp-to-pages-template`.

## Implementation notes

The CSS theme approximates the PPTX visual system rather than attempting a one-to-one PowerPoint conversion. Marp provides Markdown-first slides; PowerPoint-specific placeholders, masters, and layout behavior are converted into reusable CSS classes and authoring examples.

Hyundai font files are not redistributed. The theme references Hyundai font names as preferred local fonts and falls back to common system fonts.
