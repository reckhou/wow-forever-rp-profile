# wow-forever-rp-profile

A [Claude Code](https://claude.com/claude-code) skill that writes **roleplay (RP) character profiles for World of Warcraft: Forever**. Each profile is laid out field by field for the **Total RP 3 (TRP3)** addon and lore-checked against Forever's fixed setting (25 ADP, After the Dark Portal).

**Abbreviations:** RP = roleplay; TRP3 = Total RP 3; ADP = After the Dark Portal (the in-game calendar); IC / OOC = in character / out of character.

## What it does

- Walks you through a new character as a wizard: identity and level, a screenshot of the look, name, home, concept and flavour, with concept ideas drawn from the lore of the character's home. It then shows you one brief to confirm before drafting.
- Turns a detailed first request straight into that brief. Say "just write it" at any point to skip to the draft.
- Reworks an existing profile through the same flow, showing what's missing and changing only what you choose.
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
- Roots the backstory in the world: it reads the lore of each zone, dungeon and boss the character touches, builds on those details, and keeps bosses' secrets out of what the character could know.
- Gives every character a valid Forever in-game name (first + last name; no apostrophes or hyphens) alongside the free-text TRP3 name.
- Writes for other players: observable descriptions, no god-moding, secrets kept in a separate player-only section, and hooks to walk up to.
- Also handles part-jobs: suggesting names, writing a Currently line, or lore-checking a backstory.
- Writes voice guides for playing the character, including a list of 10 sides it drafts for you to check.

## Install

Pick one. All of them run on their own, with nothing else needed.

- **As a plugin:**
  ```
  claude plugin marketplace add reckhou/wow-forever-rp-profile
  claude plugin install wow-forever-rp-profile@wow-forever-rp-profile
  ```
  Add `--scope project` or `--scope local` to the install to turn it on for one project only. The files still go to Claude Code's plugin cache in your user folder.
- **As a personal skill:** `git clone https://github.com/reckhou/wow-forever-rp-profile.git ~/.claude/skills/wow-forever-rp-profile`
- **For one session, with nothing installed:** clone it anywhere and run `claude --plugin-dir <folder>`.
- **Inside another project:** place it at `.claude/skills/wow-forever-rp-profile`, as a copy or a git submodule. It is available when Claude Code starts in that project.

Then type `/wow-forever-rp-profile`, or just ask, for example: *"Write a TRP3 profile for my Horde Skyborne shaman on Forever"*. Or say *"make me an RP profile for my orc on Forever"*, and it will ask what it needs.

## Layout

```
SKILL.md                     routing, drafting steps and self-check
references/
├── wizard.md                the stages for creating or reworking a character
├── output-format.md         the profile layout and TRP3 paste order
├── forever-lore.md          25 ADP setting, race/class table, Skyborne lore, anachronisms, sources
├── trp3-fields.md           TRP3 tabs, fields, markup tags and limits (from the TRP3 source)
├── profile-craft.md         how to write a profile people want to interact with
└── lore/                    one file per zone, dungeon and boss, plus world.md (CC BY-SA 4.0)
.claude-plugin/              plugin and marketplace manifests
evals/                       test cases (claude plugin eval layout)
scripts/, tests/             the lore rebuild script and its tests
docs/plans/                  design plan
samples/                     worked examples of the skill's output (profiles, voice guides)
```

`git archive` leaves out everything except `SKILL.md`, `references/` and `LICENSE`, the only files the skill needs to run. `.gitattributes` holds that list.

## Rebuilding the lore

`references/lore/` is generated from the [Spoken add-on](https://github.com/rusty-key/spoken-wow)'s data, so don't edit it by hand. Other projects read these files, so keep their names and layout stable. The script needs Python 3 and [Lupa](https://pypi.org/project/lupa/).

```
git clone --depth 1 https://github.com/rusty-key/spoken-wow private-local/spoken-wow
python -I scripts/build_spoken_lore.py --spoken private-local/spoken-wow --out references/lore
python -m unittest discover -s tests
```

## Accuracy

The lore was compiled on 27 October 2026, before Forever's launch on 4 November 2026, from Warcraft Wiki, Blizzard news and press coverage; sources are listed in `forever-lore.md`. Forever has its own continuity and its story will grow with patches, so the live game wins where they differ. The TRP3 details come from the TRP3 source code (release 3.5.3).

Issues and pull requests with corrections are welcome.

## Licence

[MIT](LICENSE), except `references/lore/`, which is adapted from Warcraft Wiki and stays under CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike; see `references/lore/ATTRIBUTION.md`). World of Warcraft and Warcraft are trademarks of Blizzard Entertainment, Inc. This is an unofficial fan project, not affiliated with or endorsed by Blizzard or the Total RP 3 authors.
