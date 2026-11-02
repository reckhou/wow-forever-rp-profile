# Plan: a conversational wizard for new and existing characters

Status: built on 2 November 2026. One eval run, with Bash withheld and one run per case, passed 3 of 4 cases. `detailed-request-brief-first` missed one grader: most proposed values were marked, but some were not. The later stages, a pasted screenshot and the walkthrough have not been run with a real player.

**Abbreviations:** RP = roleplay; TRP3 = Total RP 3, the profile add-on; ADP = After the Dark Portal, the in-game calendar; Bridge = the local program in the RPMaster repository that writes Drafts for the RPMaster add-on; SavedVariables = the Lua files WoW writes to disk.

**Goal:** a player reaches a profile they keep with fewer rewrites, because the details that shape a character are gathered before the first draft. An existing profile can go through the same flow.

**Evidence:** Baldrake Cavethrone, the only character found made from start to finish, took two reworks because the screenshot, sliders and direction arrived after the first draft (`samples/README.md`).

## Decisions (agreed 2 November 2026)

| Topic | Decision |
|---|---|
| Form | A conversation run by the skill, not a bash script. This replaces the `scripts/new-character.sh` idea from the earlier `/wizard` session |
| Detailed first request | One message with the brief to confirm. "Just write it" skips to the draft |
| Screenshot | Required, pasted into chat or read from the player's WoW `Screenshots` folder. "Add later" is allowed and holds back the physical description |
| Flavour | Required. "Invent it" counts as an answer, and the invention is shown in the brief for approval |
| Existing profiles | Supported by the same flow, and also how a late screenshot gets added |
| After drafting | The skill stops at a tab-by-tab paste walkthrough. Writing to SavedVariables or installing into RPMaster is not the skill's job, because the skill runs standalone |

## Defaults chosen

- **Files:** `<character-name>/brief.md`, `profile.md` and `voice-guide.md` under the current directory, matching `RPProfiles-Private`.
- **"Just write it"** also waives the screenshot: the look is invented and listed under Assumed / invented, so the player still gets a complete profile.
- **Test scenes** are not a separate offer. The voice guide already has a Sample scenes section.
- **Calling skills:** a skill that calls this one can say what happens at stage 9, such as requiring the voice guide or doing the entry itself. The skill still knows nothing of RPMaster.
- **Player's RP experience:** asked in the first message, as new to RP, some experience or experienced, and recorded in the brief. It changes the explanations, concept complexity, markup and stage 9, not the lore checks or limits. It sits outside the numbered stages so that references to stage 7 and stage 9 stay correct.
- **Question format:** `AskUserQuestion` where available, numbered text elsewhere. Its four-option limit means faction comes before race, and class uses text or a narrowed list.

## Stages

Each stage takes one turn. Anything the request already answered is pre-filled and skipped. Every stage accepts "invent it", except that the screenshot's alternative is "add later".

| # | Stage | Done when |
|---|---|---|
| 1 | **Identity:** faction, race, class, level | The pair is valid in `forever-lore.md` section 3, or the player accepted the closest fit. Forsaken paladins have been offered Bandarion Keep. A new character's level is from 1 to 60, defaulting to 1 |
| 2 | **Look:** screenshot | The image was read and its eye colour, hair and build noted, or the player chose "add later" |
| 3 | **Name:** check theirs or offer three options | The in-game first and last names pass `profile-craft.md` section 6, with counts shown |
| 4 | **Home:** a place | `references/lore/world.md` and that place's file are read, or the place is noted as having no file |
| 5 | **Concept:** three seeds built from that lore | Who they are, what they want, what they fear and what blocks them are all settled |
| 6 | **Flavour:** age, pronouns, tone, what they miss, what they enjoy, sliders | Every field has a value, and the age fits `forever-lore.md` section 2 |
| 7 | **Brief:** one summary with lore flags and invented details | The player confirmed it and `brief.md` is saved |
| 8 | **Draft:** the existing lore, rooting, drafting and self-check steps | `profile.md` is saved and the self-check list passes |
| 9 | **Finish:** offer the voice guide, then walk through pasting tab by tab | The player accepted or declined the guide, and each TRP3 tab was covered or skipped |

## Existing profiles

1. Take the profile as a path or pasted text, and pre-fill the stages from it.
2. **A specific request** (polish it, add this screenshot, change the history) is done straight away, following `profile-craft.md` section 8.
3. **No specific request:** show the brief with its gaps marked, such as a missing fear, and let the player choose what to change.
4. Redraft only the fields affected, keep the player's voice, and list each substantive change and why.
5. If a `voice-guide.md` sits beside the profile, name the sides or lines the change affects and offer to update them.

## File changes

| File | Change |
|---|---|
| `references/wizard.md` (new) | The stages, their completion criteria, the existing-profile flow, question format and file saving |
| `references/output-format.md` (new) | The output format moved out of `SKILL.md`, plus the paste order from the Baldrake sample, used by stage 9. Part-jobs and voice guides do not need it |
| `SKILL.md` | Step 1 becomes routing: full new character or rework goes to the wizard, with the "just write it" rule. The screenshot and flavour rules replace "draft straight away". The output format becomes a pointer. Steps 2–5 stay |
| `evals/` | Cut to four basic sanity checks at the owner's request, because runs are expensive. Do not add to them. `detailed-request-brief-first`: gives a brief, not a profile. `forsaken-paladin-lore-traps` and `skyborne-mage-newcomer`: "just write it" gives a full profile. `revise-profile-gaps`: an existing profile with no screenshot gets its gaps shown |
| `README.md` | Update the "What it does" and Layout sections |
| `docs/plans/wow-forever-rp-profile-skill.md` | Mark the old Intake decision as replaced by this plan |

## Constraints

- **RPMaster mounts this repository as a submodule** and reads `references/forever-lore.md` and `references/lore/`, so those stay where they are (RPMaster `AGENTS.md`). The new files do not affect it, and the submodule moves only when its pointer is updated.
- **RPMaster's Sides tab reads a heading ending in "sides"**, so `references/voice-guide.md` keeps its format.
- **`.gitattributes` ships `SKILL.md`, `references/` and `LICENSE`**, so the wizard must live in `references/`.

## Limits and checks at build time

- **Evals use a single prompt**, so they test routing and the first reply, not a full walk through the stages.
- **Screenshot format:** WoW defaults to JPG and can be set to TGA ([Warcraft Wiki](https://warcraft.wiki.gg/wiki/Changing_the_screenshot_format)). This has not been checked on the Forever client.

## Out of scope: RPMaster and in-game updates

Checked in RPMaster on 2 November 2026. It has no universal workflow:

- **Voice guide:** covered for a human, not as an agent workflow. `README.md` gives the file name, says a changed guide reaches only Scenes started after a Bridge restart, and says the Sides tab needs Update now and `/reload`.
- **TRP3 profile:** not covered. No tracked RPMaster code outside `docs/` and `tests/` touches `TRP3_Profiles` or `totalRP3.lua`.
- **Closest thing:** `RPProfiles-Private/docs/install-profile-and-voice-guide.md` with `tools/patch_trp3.py`. Its profile ID, sliders and slot titles are hard-coded for Baldrake v3, it updates only some fields, and its path uses `_retail_` rather than `_forever_`.

Any universal workflow belongs in RPMaster, as a separate piece of work. Forever has rulesets rather than retail-style realms, and a full name is unique across them (owner, 2 November 2026). The plan for it is `docs/plans/rp-character-skill.md` in the RPMaster repository.
