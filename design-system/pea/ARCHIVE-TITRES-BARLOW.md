# Archive — police des titres « Barlow Condensed » (avant le 7 octobre 2026)

Typographie des titres utilisée jusqu’au passage à Poppins (police du logo). Conservée pour pouvoir la rétablir.

## Chargement (tools/pages/base.py → `FONTS`)
```html
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&amp;family=Barlow:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet">
```
Barlow Condensed reste chargée : elle sert toujours aux labels, boutons, dates et chiffres-clés (`--font-display`).

## Tokens (styles.css)
```css
--font-display: "Barlow Condensed", "Arial Narrow", sans-serif;
--fs-h1: clamp(2.25rem, 5vw, 4.25rem);
--fs-hero: clamp(2.75rem, 7vw, 6rem);
--fs-h2: clamp(1.75rem, 3.2vw, 2.75rem);
--fs-h3: clamp(1.25rem, 1.6vw, 1.5rem);
```

## Règles des titres
```css
h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: 800;
  text-transform: uppercase;
  color: inherit;
  overflow-wrap: break-word;
  hyphens: manual;
  text-wrap: balance;
}
h1 { font-size: var(--fs-h1); line-height: .92; letter-spacing: -.005em; margin: 0 0 var(--s-5); }
h2 { font-size: var(--fs-h2); line-height: .95; margin: 0 0 var(--s-5); }
h3 { font-size: var(--fs-h3); line-height: 1.05; font-weight: 700; letter-spacing: .01em; margin: 0 0 var(--s-2); hyphens: manual; }
.t3 { font-size: var(--fs-h3); line-height: 1.05; font-weight: 700; letter-spacing: .01em; margin: 0 0 var(--s-2); hyphens: manual; }
.page-hero--compact h1 { font-size: clamp(2rem, 4vw, 3.25rem); }
.hero--slider h1 { font-size: clamp(2.25rem, 4.8vw, 4.25rem); margin-bottom: var(--s-4); }
.event:first-child :is(h2, h3) { font-size: var(--fs-h2); line-height: .95; }   /* ≥ 1024 px */
```
Couleur : encre `#111217` sur clair, blanc sur sombre et sur photo.

## Pour rétablir
1. Dans `styles.css`, remettre `--font-title: var(--font-display)`, `--title-weight: 800`, `--title-case: uppercase`, `--title-color: inherit` et les tailles ci-dessus (bloc « Titres » des tokens).
2. Dans `tools/pages/base.py`, retirer `family=Poppins:wght@600` du lien Google Fonts, puis `python3 tools/pages/generer.py`.
