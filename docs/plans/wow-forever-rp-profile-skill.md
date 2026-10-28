# Plan: `wow-forever-rp-profile` skill

**Abbreviations:** RP = roleplay; TRP3 = Total RP 3 (the WoW roleplay profile addon); ADP = After the Dark Portal (the in-game calendar; World of Warcraft: Forever is fixed in 25 ADP); IC / OOC = in character / out of character; MSP = Mary Sue Protocol (the shared data format TRP3, MyRolePlay and XRP use to exchange profiles).

## Goal

A Claude Code skill that writes lore-friendly RP character profiles for **World of Warcraft: Forever**, laid out field by field so they can be pasted straight into **TRP3**.

## Decisions (agreed 2026-10-27)

| Question | Decision |
|---|---|
| Addon layout | TRP3 only (TRP3 supports the Forever client: its `.toc` lists interface `16001` and its 3.5.2 changelog fixes a bug "on Forever") |
| Intake | Short interview (3-5 questions in one message), then draft. Skip the interview when the request already covers the essentials |
| Language | English |
| Location | Project-level skill at `.claude/skills/wow-forever-rp-profile/` in this folder, which is its own public GitHub repository |

## Files

| Path | Purpose |
|---|---|
| `.claude/skills/wow-forever-rp-profile/SKILL.md` | Workflow: intake → lore check → draft → TRP3 layout → self-check |
| `.../references/forever-lore.md` | 25 ADP setting, race/class table, Skyborne lore, anachronism list, sources |
| `.../references/trp3-fields.md` | TRP3 tabs, fields, presets, markup tags, the 140-character tooltip limit |
| `.../references/profile-craft.md` | Writing craft: observable description, hooks, rumours, Mary Sue pitfalls, naming |
| `.../evals/<case>/` | Test cases in the `claude plugin eval` layout |
| `README.md`, `LICENSE`, `.gitignore` | Public repository basics; the eval workspace is ignored |

## Steps

1. Research Forever lore and TRP3 fields (done; sources listed in `forever-lore.md` and `trp3-fields.md`).
2. Draft the skill and references.
3. Write 4 test cases; run each with and without the skill; grade; open the eval viewer for review.
4. Create the public GitHub repository and push.
5. Iterate on feedback.
6. Optimise the skill description for triggering; package.

## Status

- **Iteration 1 (2026-10-28):** with the skill 100 % of assertions passed; without it, 89 %. All three baseline failures were Currently/OOC text over TRP3's 140-character cut-off. Runs with the skill were about 190 s faster. Must fix next: add Forever's Forsaken paladin hub (Bandarion Keep, Danitha Morr) and Forever's in-game naming rules to the references; tighten loose assertions (question count, consent handling, secret placement).
- **Fixes after iteration 1 (2026-10-28):** added Bandarion Keep / Danitha Morr / the Tarnished to `forever-lore.md`; added Forever's in-game naming rules to `profile-craft.md` section 6, with an in-game name line and checks in `SKILL.md`. The paladin case's assertion 07 now requires Bandarion Keep, and the new assertion 08 checks the in-game name. Still to do: tighten the question-count, consent and secret-placement assertions.

## Open questions / later ideas

- **TRP3 import string:** TRP3 3.5.x can import profiles from an exported string (CBOR data, compressed, wrapped in a PEM-style block). Generating that string would save the player retyping every field, but it can't be tested without the game client, so it's out of scope for v1.
- Forever lore will grow after launch (4 November 2026). Revisit `forever-lore.md` after launch and when new patches add story.
