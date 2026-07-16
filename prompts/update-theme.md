# Prompt: Update an already-applied Visual Assault theme

Use this once you've already applied a theme to your app (via
`prompts/apply-theme.md`) and the theme's definition in `themes/THEMES.md`
has since changed upstream — a token was tweaked, or the theme gained a
field it didn't have before.

## Before you start: know what you're diffing

If the theme file your assistant generated recorded which version it came
from (see "Tracking what you applied" below), you have a ref to diff from.
If it didn't, compare the theme's current block in `themes/THEMES.md`
against whatever you remember applying, or just re-run `apply-theme.md` and
review the diff to the existing file.

## Prompt template

```
I previously applied the "<THEME NAME>" theme from Visual Assault to this
app, and the theme's definition has changed upstream. Here's the diff
between what I applied and the current version:

<paste `git diff <old-ref>..<new-ref> -- themes/THEMES.md`, or the old vs.
new token block if you don't have git refs to diff>

Please update <path to the theme file this app already has> to match the
new values — only touch the tokens that actually changed, and leave
everything else (including any customizations I've made since) alone. Show
me the diff before/after so I can review it.
```

## Tracking what you applied

To make future updates easy, ask the assistant to leave a one-line marker in
the generated theme file recording what it applied, e.g.:

```css
/* visual-assault-theme: lava @ main (applied 2026-07-16) */
```

or the equivalent comment syntax for the target language. That's the only
piece of state you need — it turns "did anything change?" into a simple
diff instead of a guess.

## Why this is a separate prompt from apply-theme.md

A first-time apply has no existing file to protect. An update does — the
consumer's generated file may have been hand-edited since it was created,
so the update should be a small, reviewable patch of just what changed, not
a full regenerate that silently overwrites local edits.
