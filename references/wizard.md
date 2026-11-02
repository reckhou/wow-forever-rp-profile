# Character wizard

**Abbreviations:** TRP3 = Total RP 3; ADP = After the Dark Portal.

The wizard gathers what shapes a character before the first draft, so the player keeps what gets written. The **brief** is its product: one summary of every decision, which the player confirms and the draft is written from.

## Starting

**Pre-fill** first: mark each stage the request or an existing profile already settles, and run that stage's done-when check on it. The check still applies to pre-filled answers.

- **The request settles identity and gives a concept:** go straight to stage 7, so the whole brief is one message. Read the lore for any place it names first (stage 4), propose a value for each open field, and mark those values as proposed. The look is the exception: its line stays "pending" until the screenshot arrives, and the same message asks for the screenshot or "add later".
- **Otherwise:** start at the first open stage and take one stage per turn.

Open with one line naming the stages ahead, and say that "just write it" skips to the draft at any point. When the player says it, go to `SKILL.md` step 2 with the answers so far, invent the rest including the look, and list it all under **Assumed / invented**.

## Asking

Use `AskUserQuestion` when it is available, otherwise short numbered questions in the reply. Options need to come from the references: class options from `forever-lore.md` section 3, concept seeds from the lore just read. `AskUserQuestion` takes at most four options, so ask for the faction before the race. For a longer list, such as a race's classes, write the options out and take the answer as text.

Every stage accepts "invent it", and an invention is shown in the brief for approval. A conflict with the lore is handled as in `SKILL.md` step 2, at the stage where it appears.

## Stages

| # | Stage | Done when |
|---|---|---|
| 1 | **Identity:** faction, race, class, level (see below) | The pair is valid in `forever-lore.md` section 3, or the player accepted the closest fit. A Forsaken paladin has been offered Bandarion Keep. A new character's level is a whole number from 1 to 60 |
| 2 | **Look:** see below | The screenshot was read and its look noted, or the player chose "add later" |
| 3 | **Name:** check theirs, or offer three options | The first and last in-game names pass `profile-craft.md` section 6, with counts shown |
| 4 | **Home:** where they come from and live now | `lore/world.md` and each place's file are read, or the place is noted as having no file (`SKILL.md` step 3) |
| 5 | **Concept:** offer three seeds, each built on a specific from the lore just read | Who they are, what they want, what they fear and what stands in the way are all settled |
| 6 | **Flavour:** age, pronouns, tone, what they miss, what they enjoy, trait sliders | Every field has a value, and the age fits `forever-lore.md` section 2 |
| 7 | **Brief:** see below | The player confirmed it, and it is saved as `brief.md` |
| 8 | **Draft:** `SKILL.md` steps 2–5, written from the brief | `profile.md` is saved, and every item on the self-check list holds |
| 9 | **Finish:** see below | The player accepted or declined the voice guide, and each TRP3 tab was covered or skipped |

### Stage 1: the level

Ask a new character's level, offering 1 as the default because a newly created character is usually level 1, and let the player give any other. If the request doesn't say, it doesn't hold the stage open: put level 1 in the brief, marked *(proposed)*. Don't ask for an existing profile, whose brief shows a level only if the player or the profile gives one.

The level is the character's in-game progress, not their life experience, so a level 1 can still be a veteran. It only limits what the profile says they are doing now: Currently and the hooks stay within what that level can reach in play. It goes in the brief and not in the TRP3 fields, because the game shows it.

### Stage 2: the look

The in-game look decides what the physical description can say, so ask for a screenshot of the character. The player can paste it into the chat if the client allows that, or give a path. WoW saves to the `Screenshots` folder in the client's install folder (`_forever_` for Forever), as JPG unless set otherwise. If it is a TGA file you can't read, ask them to paste it, or to type `/console screenshotFormat jpg` and take another.

Note what the character model fixes: skin, hair, eyes, build. Gear can change, so treat it as a suggestion. Say what you see in the brief, so the player can catch the wrong character or a misreading.

With **"add later"**, leave out the physical description and eye colour, mark them as pending in the profile, and keep At first glance to things that don't depend on the look. Adding the screenshot later follows [Existing profiles](#existing-profiles).

### Stage 7: the brief

```markdown
# <Full name>: brief
*<Faction> · <Race> <Class> · Level <n> · In-game name: <First> (<n>) <Last> (<n>)*

- **Look:** <what the screenshot shows, or "pending">
- **From / lives:** <places; note any with no lore file>
- **Who:** …
- **Wants:** …
- **Fears:** …
- **In the way:** …
- **Age / pronouns / tone:** …
- **Misses / enjoys:** …
- **Traits:** <sliders and their leans>

**Lore flags:** <each conflict, the fix and how to revert it>
**Proposed or invented:** <everything the player did not say>
```

Mark each value the player did not give with *(proposed)* on its line, including small ones such as pronouns and tone. End by asking the player to confirm or change the brief. Every line except the look carries a value, because an open line comes back later as a thin section in the profile and voice guide.

### Stage 9: finishing

1. Offer the voice guide, which includes sample scenes (`voice-guide.md`). If accepted, save it as `voice-guide.md`.
2. Walk through pasting, one tab per turn, in the paste order in `output-format.md`.

When a calling skill has said what to do at this stage, follow that instead: it may require the voice guide, and it may do the entry itself.

## Files

Save to a `<character-name>/` folder, lower case and hyphenated, under the current directory: `brief.md`, `profile.md` and `voice-guide.md`. If you can't write files, keep everything in the reply.

## Existing profiles

Take the profile as a path or pasted text, and pre-fill the stages from it.

- **A specific request** (polish it, add this screenshot, change the history): do it straight away, and check every place and boss the profile names against the `SKILL.md` step 3 files.
- **No specific request:** show the brief with its gaps marked, such as a missing fear or no Rumours block, and lore problems under **Lore flags**. Then ask what they want to change.

Then, in both cases:

1. Follow `profile-craft.md` section 8: keep the player's voice, names and core events, and fix things in the order it gives.
2. Rewrite the fields the change affects and leave the rest word for word.
3. Give the result in the format in `output-format.md`, followed by a bullet list of each substantive change and why.
4. If a `voice-guide.md` sits beside the profile, name the sides and lines the change affects and offer to update them.
