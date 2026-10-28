# wow-forever-rp-profile

A [Claude Code](https://claude.com/claude-code) skill that writes **roleplay (RP) character profiles for World of Warcraft: Forever**. Each profile is laid out field by field for the **Total RP 3 (TRP3)** addon and lore-checked against Forever's fixed setting (25 ADP, After the Dark Portal).

**Abbreviations:** RP = roleplay; TRP3 = Total RP 3; ADP = After the Dark Portal (the in-game calendar); IC / OOC = in character / out of character.

## What it does

- Asks 3–5 quick questions when you give it very little, and drafts straight away when you've already described the character.
- Produces a paste-ready TRP3 profile:
  - Characteristics, additional information and personality-trait sliders
  - About text (physical description, personality, history with a Rumours block)
  - Five *At first glance* slots
  - **Currently** and **OOC** lines kept within TRP3's 140-character tooltip limit
- Checks the concept against Forever's lore:
  - valid race/class pairs, including the Skyborne and the six new pairs
  - age arithmetic
  - anachronisms from later expansions (blood elves in the Horde, the Argent Crusade, the Cataclysm …)
  - lore figures kept in the background
  - Forever-only lore such as the Forsaken paladins of Bandarion Keep
- Gives every character a valid Forever in-game name (first + last name; no apostrophes or hyphens) alongside the free-text TRP3 name.
- Writes for other players: observable descriptions, no god-moding, secrets kept in a separate player-only section, and hooks to walk up to.
- Also handles part-jobs: polishing an existing profile, suggesting names, writing a Currently line, or lore-checking a backstory.

## Install

The skill lives in `.claude/skills/wow-forever-rp-profile/`.

- **Use it in this folder:** clone the repository and run Claude Code inside it. Project skills load automatically.
- **Use it everywhere:** copy `.claude/skills/wow-forever-rp-profile/` into `~/.claude/skills/`.

Then ask, for example: *"Write a TRP3 profile for my Horde Skyborne shaman on Forever"*. Or just say *"make me an RP profile for my orc on Forever"*, and it will ask what it needs.

## Layout

```
.claude/skills/wow-forever-rp-profile/
├── SKILL.md                     workflow and output format
├── references/
│   ├── forever-lore.md          25 ADP setting, race/class table, Skyborne lore, anachronisms, sources
│   ├── trp3-fields.md           TRP3 tabs, fields, markup tags and limits (from the TRP3 source)
│   └── profile-craft.md         how to write a profile people want to interact with
└── evals/                       test cases (claude plugin eval layout)
docs/plans/                      design plan
samples/                         worked examples of the skill's output (profiles, voice guides)
```

## Accuracy

The lore was compiled on 27 October 2026, before Forever's launch on 4 November 2026, from Warcraft Wiki, Blizzard news and press coverage; sources are listed in `forever-lore.md`. Forever has its own continuity and its story will grow with patches, so the live game wins where they differ. The TRP3 details come from the TRP3 source code (release 3.5.3).

Issues and pull requests with corrections are welcome.

## Licence

[MIT](LICENSE). World of Warcraft and Warcraft are trademarks of Blizzard Entertainment, Inc. This is an unofficial fan project, not affiliated with or endorsed by Blizzard or the Total RP 3 authors.
