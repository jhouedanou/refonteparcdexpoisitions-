#!/usr/bin/env node
// Contrôle de conformité : charte graphique PEA + composants Bento DS.
// Usage : node tools/verif/conformite.mjs [--base=http://localhost:8000] [--out=<dossier>] [--shots] [--pages=a.html,b.html] [--widths=375,1440]
// Prérequis : Node ≥ 22 (WebSocket et fetch natifs), Google Chrome, serveur de la maquette lancé (configuration « maquette-pea »).
// Chaque page est ouverte dans Chrome headless (protocole DevTools) à 4 largeurs ; les styles CALCULÉS sont contrôlés
// (police, graisses, rayons, fonds, titres, boutons, hauteurs, contrastes, composants Bento présents, débordement, logo).
// Sortie : rapport texte + JSON dans --out ; code de sortie 1 s'il reste un écart.
import { spawn } from "node:child_process";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const arg = (k, d) => (process.argv.find((a) => a.startsWith(`--${k}=`)) || "").split("=").slice(1).join("=") || d;
const BASE = arg("base", "http://localhost:8000");
const OUT = arg("out", join(tmpdir(), "pea-conformite"));
const SHOTS = process.argv.includes("--shots");
const WIDTHS = arg("widths", "375,768,1024,1440").split(",").map(Number);
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

// Pages représentatives et composants Bento attendus (attribut data-bento posé par le générateur)
const COMMUN = ["Topbar", "Site header", "Menu", "Footer", "Newsletter form"];
const PAGES = {
  "index.html": [...COMMUN, "Block/Hero", "Carousel", "Block/Key figures", "Block/Video", "Card", "Collection", "Block/Partners", "Cta", "Button", "Badge", "Title"],
  "nos-espaces.html": [...COMMUN, "Page header", "Breadcrumb", "Card", "Collection", "Button", "Title"],
  "le-dome.html": [...COMMUN, "Page header", "Breadcrumb", "Block/Key figures", "Image gallery", "Badge", "Button", "Title"],
  "agenda.html": [...COMMUN, "Page header", "Breadcrumb", "Block/Agenda list", "Card", "Badge", "Modal", "Title"],
  "evenement-auto-expo.html": [...COMMUN, "Page header", "Breadcrumb", "Badge", "Button", "Title"],
  "contact-devis.html": [...COMMUN, "Page header", "Breadcrumb", "Form/Field", "Contact details", "Block/Map", "Button", "Title"],
  "venir-a-abidjan.html": [...COMMUN, "Page header", "Breadcrumb", "Accordion", "Title"],
  "en/index.html": [...COMMUN, "Block/Hero", "Block/Key figures", "Block/Video", "Card", "Title"],
};
const only = arg("pages", "");
const pages = only ? only.split(",") : Object.keys(PAGES);

// ---------------------------------------------------------------- Audit exécuté dans la page
function audit(expected) {
  const V = [];
  const add = (rule, el, detail) => V.push({ rule, el: el ? describe(el) : "", detail });
  function describe(el) {
    let s = el.tagName.toLowerCase();
    if (el.id) s += "#" + el.id;
    if (el.classList.length) s += "." + [...el.classList].slice(0, 2).join(".");
    const t = (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 32);
    return t ? `${s} « ${t} »` : s;
  }
  const parse = (c) => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lum = ({ r, g, b }) => { const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
  const hex = ({ r, g, b }) => "#" + [r, g, b].map((v) => Math.round(v).toString(16).padStart(2, "0")).join("").toUpperCase();
  const blend = (fg, bg) => ({ r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1 });
  const visible = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none" && parseFloat(cs.opacity) > 0.05 && !el.closest("[hidden],[aria-hidden='true'] .sr-only"); };
  const srOnly = (el) => el.closest(".sr-only") !== null;
  // Fond effectif : premier ancêtre opaque ; une image de fond, une photo ou une vidéo dessous = « sur image »
  function background(el) {
    let layers = [];
    for (let n = el; n; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (n.matches(".hero, .page-hero--bg, .video__facade, .video, .cta--photo, .space, .lightbox, .slider, .event-dialog__poster, [data-on-image]") && !n.matches(".cta--photo") ) return { image: true };
      if (cs.backgroundImage && cs.backgroundImage !== "none" && !cs.backgroundImage.startsWith("linear-gradient(rgb") && n !== document.documentElement && n !== document.body) return { image: true };
      const c = parse(cs.backgroundColor);
      if (c && c.a > 0) { layers.push(c); if (c.a >= 0.999) break; }
    }
    let bg = { r: 255, g: 255, b: 255, a: 1 };
    for (const l of layers.reverse()) bg = blend(l, bg);
    return { color: bg };
  }

  // 0. Chargement des polices : kit web = Poppins 100 / 400 / 700
  const fontLinks = [...document.querySelectorAll('link[href*="fonts.googleapis.com/css2"]')].map((l) => l.href);
  if (!fontLinks.length) add("fonts.load", null, "aucune feuille Google Fonts");
  for (const h of fontLinks) {
    if (!/family=Poppins/.test(h) || /family=(?!Poppins)/.test(h)) add("fonts.load", null, `autre famille que Poppins : ${h}`);
    const w = (decodeURIComponent(h).match(/wght@([^&]+)/) || [])[1] || "";
    const weights = w.split(";").map((x) => Number(x.split(",").pop()));
    if (weights.some((x) => ![100, 400, 700].includes(x))) add("fonts.load", null, `graisses chargées hors kit web : ${w}`);
  }

  const all = [...document.querySelectorAll("body *")].filter((el) => !el.closest("svg, iframe, noscript, template, script, style"));
  const textEls = all.filter((el) => [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()) && visible(el));

  // 1. Typographie : Poppins seule, graisses 100 / 400 / 700
  for (const el of textEls) {
    const cs = getComputedStyle(el);
    const fam = cs.fontFamily.split(",")[0].replace(/["']/g, "").trim();
    if (fam !== "Poppins") add("typo.famille", el, fam);
    if (![100, 400, 700].includes(Number(cs.fontWeight))) add("typo.graisse", el, cs.fontWeight);
  }

  // 2. Angles vifs : aucun rayon, sauf champs (2 px) et logo GL events (coin du fichier officiel)
  for (const el of all) {
    if (!visible(el)) continue;
    const cs = getComputedStyle(el);
    const r = Math.max(...["borderTopLeftRadius", "borderTopRightRadius", "borderBottomLeftRadius", "borderBottomRightRadius"].map((k) => parseFloat(cs[k]) || 0));
    if (!r) continue;
    if (el.matches("input:not([type=checkbox]):not([type=radio]), select, textarea") && r <= 2) continue;
    if (el.matches(".footer__partner-logo, .footer__partner-logo *")) continue;
    if (el.matches("input[type=checkbox], input[type=radio]")) continue;
    add("forme.rayon", el, `${r}px`);
  }

  // 3. Fonds : pas de noir (charte : noir = logo monochrome) ; voiles sur photo et visionneuse exceptés
  for (const el of all) {
    if (!visible(el) || el.matches("video, .lightbox, .lightbox *, .slider, .slider *, .hero__img, .video, .video *, .event-dialog__poster, .event-dialog__poster *, .skip")) continue;
    const c = parse(getComputedStyle(el).backgroundColor);
    if (!c || c.a < 0.9) continue;
    const r = el.getBoundingClientRect();
    if (r.width * r.height < 1500) continue;
    if (lum(c) < 0.02) add("fond.noir", el, hex(c));
  }

  // 4. Titres (Bento Title, couleur PEA) : Bold 700 ; ≥ 24 px sur fond clair = orange #DA5900 ; < 24 px jamais orange
  for (const h of document.querySelectorAll("h1, h2, h3, h4, .title")) {
    if (!visible(h) || srOnly(h)) continue;
    const cs = getComputedStyle(h), size = parseFloat(cs.fontSize), col = parse(cs.color), bg = background(h);
    if (Number(cs.fontWeight) !== 700) add("titre.graisse", h, cs.fontWeight);
    if (bg.image) continue;
    const light = lum(bg.color) > 0.4;
    if (light && size >= 23.5 && hex(col) !== "#DA5900") add("titre.couleur", h, `${hex(col)} à ${size}px sur ${hex(bg.color)}`);
    if (size < 23.5 && hex(col) === "#DA5900") add("titre.petit-orange", h, `${size}px`);
  }

  // 5. Boutons (Bento Button) : 16 px Regular, padding 12 / 16, bordure 2 px
  for (const b of document.querySelectorAll(".btn")) {
    if (!visible(b)) continue;
    const cs = getComputedStyle(b);
    if (parseFloat(cs.fontSize) !== 16) add("bouton.taille", b, cs.fontSize);
    if (Number(cs.fontWeight) !== 400) add("bouton.graisse", b, cs.fontWeight);
    if (parseFloat(cs.borderTopWidth) !== 2) add("bouton.bordure", b, cs.borderTopWidth);
  }

  // 6. Hauteurs Bento : Topbar 48 px ; Site header 64 px (72 px dès 1120 px, logo de 48 px)
  const tb = document.querySelector('[data-bento="Topbar"]');
  if (tb && visible(tb) && Math.round(tb.getBoundingClientRect().height) !== 48) add("topbar.hauteur", tb, `${Math.round(tb.getBoundingClientRect().height)}px`);
  const sh = document.querySelector('[data-bento="Site header"] .topbar__inner');
  if (sh) { const h = Math.round(sh.getBoundingClientRect().height), want = innerWidth >= 1120 ? 72 : 64; if (h !== want) add("header.hauteur", sh, `${h}px (attendu ${want})`); }

  // 7. Contrastes : 4,5:1, ou 3:1 pour le grand texte (≥ 24 px, ou ≥ 18,66 px en gras)
  for (const el of textEls) {
    if (srOnly(el) || el.closest("[data-contrast-skip]")) continue;
    const cs = getComputedStyle(el);
    const bg = background(el);
    if (bg.image) continue;
    const fg0 = parse(cs.color); if (!fg0) continue;
    const fg = blend({ ...fg0, a: fg0.a * parseFloat(cs.opacity) }, bg.color);
    const size = parseFloat(cs.fontSize), big = size >= 23.5 || (size >= 18.5 && Number(cs.fontWeight) >= 700);
    const r = ratio(fg, bg.color), need = big ? 3 : 4.5;
    if (r < need - 0.01) add("contraste", el, `${r.toFixed(2)}:1 < ${need} (${hex(fg)} sur ${hex(bg.color)}, ${size}px)`);
  }

  // 8. Composants Bento présents
  for (const name of expected) if (!document.querySelector(`[data-bento="${name}"]`)) add("bento.absent", null, name);

  // 9. Débordement horizontal
  if (document.documentElement.scrollWidth > innerWidth + 1) add("debordement", null, `${document.documentElement.scrollWidth}px > ${innerWidth}px`);

  // 11. Espacements : échelle Bento (space/1…16 = 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64) + mise en page 96 · 128.
  //     Contrôle 1 — chaque padding, marge verticale et gap CALCULÉ est sur l’échelle (1–3 px tolérés : filets, décalages de bordure).
  //     Contrôle 2 — l’écart RENDU entre deux sous-éléments voisins (bas de l’un → haut du suivant, ou bord à bord sur une ligne)
  //     est sur l’échelle, jamais négatif (chevauchement) et jamais nul entre deux blocs de texte (texte collé).
  //     Exceptions documentées : réserves de l’arche du logo (hauteur proportionnelle à la largeur), voir ARCHE ci-dessous.
  const SCALE = [0, 1, 2, 3, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96, 128];
  const onScale = (v) => SCALE.some((s) => Math.abs(Math.abs(v) - s) < 0.6);
  const ARCHE = { // élément → côtés dont la valeur dépend de l’arche (calc sur la largeur)
    ".page-hero--bg": ["paddingBottom"], ".footer": ["paddingTop"], ".figure--arch": [],
    ".section--brun, .section--vert, .section--brun-fonce": ["paddingBottom"], ".hero__arch": [] };
  // Marge « auto » (alignement, pas un token) : la valeur calculée ne change pas si on force « auto »
  const isAuto = (el, side) => { if (!side.startsWith("margin")) return false; const prop = side === "marginTop" ? "margin-top" : "margin-bottom";
    const before = getComputedStyle(el)[side], keep = el.style.getPropertyValue(prop), prio = el.style.getPropertyPriority(prop);
    el.style.setProperty(prop, "auto", "important"); const same = getComputedStyle(el)[side] === before;
    el.style.removeProperty(prop); if (keep) el.style.setProperty(prop, keep, prio); return same; };
  const exempt = (el, side) => Object.entries(ARCHE).some(([sel, sides]) => el.matches(sel) && sides.includes(side));
  const spaced = all.filter((el) => visible(el) && !srOnly(el) && !el.closest(".slider, .lightbox, dialog:not([open]), .cookie-banner"));
  for (const el of spaced) {
    const cs = getComputedStyle(el);
    if (cs.display === "inline" || cs.display === "contents") continue;
    for (const side of ["paddingTop", "paddingRight", "paddingBottom", "paddingLeft", "marginTop", "marginBottom"]) {
      const v = parseFloat(cs[side]) || 0;
      if (v && !onScale(v) && !exempt(el, side) && !isAuto(el, side)) add("espacement.hors-echelle", el, `${side} ${+v.toFixed(2)}px`);
    }
    if (/flex|grid/.test(cs.display)) for (const g of ["rowGap", "columnGap"]) {
      const v = parseFloat(cs[g]); if (v && !onScale(v)) add("espacement.hors-echelle", el, `${g} ${+v.toFixed(2)}px`);
    }
  }
  // Distance réelle entre deux textes : bas de la dernière ligne de A → haut de la première ligne de B (boîtes de glyphes)
  const textRects = (el) => { const r = document.createRange(); r.selectNodeContents(el); return [...r.getClientRects()].filter((q) => q.width > 0 && q.height > 0); };
  const textGap = (a, b) => { const ra = textRects(a), rb = textRects(b); if (!ra.length || !rb.length) return null;
    return Math.min(...rb.map((q) => q.top)) - Math.max(...ra.map((q) => q.bottom)); };
  const hasText = (el) => (el.textContent || "").trim().length > 0 && !el.querySelector("img, svg:not(.i), video, iframe");
  const gapStats = {};
  for (const parent of spaced) {
    const ps = getComputedStyle(parent);
    const flow = /flex|grid/.test(ps.display) ? "flex" : "bloc";
    const kids = [...parent.children].filter((k) => {
      if (!visible(k) || srOnly(k)) return false;
      const ks = getComputedStyle(k);
      return !["absolute", "fixed"].includes(ks.position) && ks.display !== "inline" && ks.float === "none" && !k.matches("br, script, style, template, dialog");
    });
    for (let i = 1; i < kids.length; i++) {
      const A = kids[i - 1], B = kids[i], a = A.getBoundingClientRect(), b = B.getBoundingClientRect();
      let g, axis;
      const overlapX = Math.min(a.right, b.right) - Math.max(a.left, b.left) > 1;   // l’un au-dessus de l’autre (même colonne)
      if (b.top >= a.bottom - 1 && overlapX) { g = b.top - a.bottom; axis = "vertical"; }
      else if (b.left >= a.right - 1 && Math.min(a.bottom, b.bottom) > Math.max(a.top, b.top)) { g = b.left - a.right; axis = "horizontal"; }
      else continue; // colonnes différentes ou retour à la ligne : pas des voisins visuels
      g = Math.round(g * 100) / 100;
      const key = `${axis} ${Math.round(g)}`; gapStats[key] = (gapStats[key] || 0) + 1;
      const where = `${describe(A)} → ${describe(B)}`;
      const minGap = axis === "vertical" ? (parseFloat(ps.rowGap) || 0) : (parseFloat(ps.columnGap) || 0);
      if (g < -1) add("espacement.chevauchement", parent, `${axis} ${g}px : ${where}`);
      // Flux de blocs : l’écart vient des marges (tokens) → il doit être sur l’échelle.
      // Flex / grille : l’écart vient du gap (contrôlé ci-dessus) ; le surplus est de l’espace libre d’alignement (space-between, margin auto) → seul le minimum est exigé.
      else if (flow === "bloc" && axis === "vertical" && !onScale(g)) add("espacement.ecart-hors-echelle", parent, `${axis} ${g}px : ${where}`);
      else if (flow === "flex" && minGap && g < minGap - 1) add("espacement.ecart-sous-gap", parent, `${axis} ${g}px < gap ${minGap}px : ${where}`);
      else if (flow === "flex" && axis === "vertical" && !onScale(g)) (V.libres ||= []).push(`${Math.round(g)}px (gap ${minGap}) dans ${describe(parent)} : ${where}`);
      // Texte collé : deux blocs de texte voisins sans espacement posé (marge, gap ou padding < 4 px) — listes et tableaux exclus
      if (axis === "vertical" && hasText(A) && hasText(B) && !A.matches("li, tr, td, th, thead, tbody, dt, dd, option, summary") && !parent.matches("ul, ol, dl, table, tbody, thead, tr")) {
        const as = getComputedStyle(A), bs = getComputedStyle(B);
        const eff = g + (parseFloat(as.paddingBottom) || 0) + (parseFloat(bs.paddingTop) || 0) + (parseFloat(as.borderBottomWidth) ? 4 : 0) + (parseFloat(bs.borderTopWidth) ? 4 : 0);
        if (eff < 4) add("espacement.texte-colle", parent, `${Math.round(eff * 10) / 10}px posés entre : ${where}`);
      }
    }
  }
  V.gaps = gapStats;

  // Relevé détaillé par composant Bento (pour le rapport d’intégration) : première occurrence visible de chaque composant
  const px = (v) => Math.round(parseFloat(v) * 10) / 10;
  const box = (el) => { const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height), padding: [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(px).join(" "),
      gap: /flex|grid/.test(cs.display) ? `${px(cs.rowGap) || 0} / ${px(cs.columnGap) || 0}` : "—", fond: (() => { const b = parse(cs.backgroundColor); return b && b.a > 0.05 ? hex(b) : "transparent"; })(),
      texte: hex(parse(cs.color)), police: `${cs.fontFamily.split(",")[0].replace(/["']/g, "")} ${cs.fontWeight} ${px(cs.fontSize)}px`,
      bordure: parseFloat(cs.borderTopWidth) ? `${px(cs.borderTopWidth)}px ${hex(parse(cs.borderTopColor))}` : "—", rayon: px(cs.borderTopLeftRadius) };
  };
  const releve = {};
  for (const el of document.querySelectorAll("[data-bento]")) {
    const name = el.dataset.bento; const r = (releve[name] ||= { nombre: 0, visibles: 0 }); r.nombre++;
    if (!visible(el) && !el.matches("dialog")) continue; r.visibles++;
    if (r.mesure) continue;
    r.mesure = box(el);
    const inner = [...el.children].filter((k) => visible(k) && !srOnly(k) && !["absolute", "fixed"].includes(getComputedStyle(k).position)).slice(0, 6);
    r.enfants = inner.map((k) => `${describe(k).split(" « ")[0]} ${Math.round(k.getBoundingClientRect().height)}px`);
    const gs = [];
    for (let i = 1; i < inner.length; i++) { const a = inner[i - 1].getBoundingClientRect(), b = inner[i].getBoundingClientRect();
      gs.push(b.top >= a.bottom - 1 ? Math.round(b.top - a.bottom) : Math.round(b.left - a.right)); }
    r.ecarts = gs;
  }
  // Titres par niveau, sections et leurs fonds, contraste minimal
  const titresSet = {}; for (const h of document.querySelectorAll(".title")) { const l = [...h.classList].find((x) => /^title--l\d$/.test(x)); if (l && visible(h) && !srOnly(h)) { const cs = getComputedStyle(h);
    const t = (titresSet[l] ||= { taille: `${px(cs.fontSize)}px ${cs.fontWeight}`, couleurs: new Set(), nombre: 0 }); t.couleurs.add(hex(parse(cs.color))); t.nombre++; } }
  const titres = Object.fromEntries(Object.entries(titresSet).map(([k, v]) => [k, `${v.taille} × ${v.nombre} (${[...v.couleurs].join(", ")})`]));
  const sections = [...document.querySelectorAll("body > section, body > footer, body > div.utility, body > header, main > section")].filter(visible).map((s) => {
    const cs = getComputedStyle(s); const t = s.querySelector(".title"); const b = parse(cs.backgroundColor);
    const nom = s.dataset.bento && !t ? s.dataset.bento : (t ? t.textContent.trim().slice(0, 48) : describe(s).split(" « ")[0]);
    return { section: s.matches(".utility") ? "Topbar" : s.matches(".topbar") ? "Site header" : s.matches(".footer") ? "Footer" : nom, fond: b && b.a > 0 ? hex(b) : "transparent", padding: `${px(cs.paddingTop)} / ${px(cs.paddingBottom)}`, hauteur: Math.round(s.getBoundingClientRect().height), composants: [...new Set([...s.querySelectorAll("[data-bento]")].map((e) => e.dataset.bento).concat(s.dataset.bento ? [s.dataset.bento] : []))] };
  });
  let minRatio = 99;
  for (const el of textEls) { if (srOnly(el)) continue; const bg = background(el); if (bg.image) continue; const cs = getComputedStyle(el); const f = parse(cs.color); if (!f) continue;
    const r = ratio(blend({ ...f, a: f.a * parseFloat(cs.opacity) }, bg.color), bg.color); if (r < minRatio) minRatio = r; }
  V.releve = { composants: releve, titres, sections, contrasteMin: Math.round(minRatio * 100) / 100, titrePage: document.title };

  // Couverture : nombre d’éléments réellement contrôlés (preuve que l’audit a porté sur la page)
  V.stats = { textes: textEls.length, titres: document.querySelectorAll("h1, h2, h3, h4").length, boutons: document.querySelectorAll(".btn").length,
    composants: [...new Set([...document.querySelectorAll("[data-bento]")].map((e) => e.dataset.bento))].length };

  // 10. Logo jamais déformé (charte p. 5)
  for (const img of document.querySelectorAll('img[src*="logo-pea"]')) {
    if (!visible(img) || !img.naturalWidth) continue;
    const r = img.getBoundingClientRect(), a = r.width / r.height, n = img.naturalWidth / img.naturalHeight;
    if (Math.abs(a / n - 1) > 0.02) add("logo.deforme", img, `${a.toFixed(3)} vs ${n.toFixed(3)}`);
  }
  return { violations: V, stats: V.stats, gaps: V.gaps, releve: V.releve, libres: V.libres || [] };
}

// ---------------------------------------------------------------- Pilotage de Chrome (DevTools Protocol)
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function main() {
  mkdirSync(OUT, { recursive: true });
  const profile = mkdtempSync(join(tmpdir(), "pea-chrome-"));
  const port = 9300 + Math.floor(Math.random() * 500);
  const chrome = spawn(CHROME, ["--headless=new", `--remote-debugging-port=${port}`, `--user-data-dir=${profile}`, "--hide-scrollbars", "--no-first-run", "--no-default-browser-check", "--mute-audio", "about:blank"], { stdio: "ignore" });
  let wsUrl;
  for (let i = 0; i < 50 && !wsUrl; i++) {
    await sleep(200);
    try { const list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); wsUrl = (list.find((t) => t.type === "page") || {}).webSocketDebuggerUrl; } catch {}
  }
  if (!wsUrl) { chrome.kill(); throw new Error("Chrome headless injoignable"); }
  const ws = new WebSocket(wsUrl);
  await new Promise((r, j) => { ws.onopen = r; ws.onerror = j; });
  let id = 0; const pending = new Map(); const waiters = [];
  ws.onmessage = (e) => {
    const m = JSON.parse(e.data);
    if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(m.error.message)) : res(m.result); }
    else if (m.method) for (const w of [...waiters]) if (w.method === m.method) { waiters.splice(waiters.indexOf(w), 1); w.res(m.params); }
  };
  const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
  const once = (method, timeout = 20000) => new Promise((res) => { waiters.push({ method, res }); setTimeout(() => res(null), timeout); });
  const evaluate = async (expr) => { const r = await send("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise: true }); if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || "erreur JS"); return r.result.value; };
  await send("Page.enable"); await send("Runtime.enable");
  // Mouvement réduit : aucune apparition au défilement (sinon les blocs sous le pli restent à opacité 0 et échappent au contrôle)
  await send("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: "reduce" }] });

  const report = []; let total = 0;
  for (const page of pages) {
    for (const width of WIDTHS) {
      await send("Emulation.setDeviceMetricsOverride", { width, height: 900, deviceScaleFactor: 1, mobile: width < 768 });
      const loaded = once("Page.loadEventFired");
      await send("Page.navigate", { url: `${BASE}/${page}` });
      await loaded;
      // Consentement refusé (bandeau masqué), polices prêtes, défilement complet pour déclencher les apparitions
      await evaluate(`(async () => { document.fonts && await document.fonts.ready;
        const b = [...document.querySelectorAll('button')].find(x => /Tout refuser|Reject all/.test(x.textContent)); if (b) b.click();
        const H = document.documentElement.scrollHeight; for (let y = 0; y < H; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); }
        scrollTo(0, 0); await new Promise(r => setTimeout(r, 900)); return true; })()`);
      const res = await evaluate(`(${audit.toString()})(${JSON.stringify(PAGES[page] || COMMUN)})`);
      const v = res.violations, st = res.stats;
      const hidden = await evaluate(`[...document.querySelectorAll("main *")].filter(e => parseFloat(getComputedStyle(e).opacity) < 0.05 && e.getBoundingClientRect().height > 0 && !e.closest("[hidden], .slider, .lightbox, dialog")).length`);
      if (hidden) v.push({ rule: "audit.masques", el: "", detail: `${hidden} éléments à opacité nulle non contrôlés` });
      if (!st || st.textes < 20) v.push({ rule: "audit.couverture", el: "", detail: `seulement ${st ? st.textes : 0} textes contrôlés : page mal chargée ?` });
      total += v.length;
      report.push({ page, width, stats: st, violations: v, gaps: res.gaps, releve: res.releve, libres: res.libres });
      if (SHOTS) {
        const metrics = await send("Page.getLayoutMetrics");
        const h = Math.min(Math.ceil(metrics.cssContentSize.height), 16000);
        const shot = await send("Page.captureScreenshot", { format: "jpeg", quality: 70, captureBeyondViewport: true, clip: { x: 0, y: 0, width, height: h, scale: 1 } });
        writeFileSync(join(OUT, `${page.replace(/\//g, "_").replace(".html", "")}-${width}.jpg`), Buffer.from(shot.data, "base64"));
      }
      process.stdout.write(`${v.length ? "✗" : "✓"} ${page} @${width} : ${v.length} écart(s) — ${st.textes} textes, ${st.titres} titres, ${st.boutons} boutons, ${st.composants} composants Bento contrôlés\n`);
    }
  }
  ws.close(); chrome.kill(); try { rmSync(profile, { recursive: true, force: true }); } catch {}

  // Synthèse par règle
  const byRule = {};
  for (const { page, width, violations } of report) for (const x of violations) {
    (byRule[x.rule] ||= []).push(`${page}@${width} ${x.el} ${x.detail}`.trim());
  }
  let txt = `Conformité charte + Bento — ${new Date().toISOString()}\n${total} écart(s)\n\n`;
  for (const [rule, items] of Object.entries(byRule).sort((a, b) => b[1].length - a[1].length)) {
    const uniq = [...new Set(items.map((s) => s.replace(/^\S+@\d+ /, "")))];
    txt += `## ${rule} — ${items.length} (${uniq.length} distincts)\n` + uniq.slice(0, 25).map((s) => "  - " + s).join("\n") + (uniq.length > 25 ? `\n  … +${uniq.length - 25}` : "") + "\n\n";
  }
  writeFileSync(join(OUT, "rapport.txt"), txt);
  writeFileSync(join(OUT, "rapport.json"), JSON.stringify(report, null, 1));
  console.log(`\n${total} écart(s). Rapport : ${join(OUT, "rapport.txt")}`);
  process.exit(total ? 1 : 0);
}
main().catch((e) => { console.error(e); process.exit(2); });
