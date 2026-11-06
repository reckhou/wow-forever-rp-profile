# Character wizard

**Abbreviations:** RP = roleplay; TRP3 = Total RP 3; ADP = After the Dark Portal; IC / OOC = in character / out of character.

The wizard gathers what shapes a character before the first draft, so the player keeps what gets written. The **brief** is its product: one summary of every decision, which the player confirms and the draft is written from.

## Starting

**Pre-fill** first: mark each stage the request or an existing profile already settles, and run that stage's done-when check on it. The check still applies to pre-filled answers.

- **The request settles identity and says both who the character is and what they want:** go straight to stage 6, so the whole brief is one message. A temperament or a few traits are not enough: "conservative, and easily embarrassed when things go wrong" goes to the next open stage, and those traits carry into every idea at stage 3. Read the lore for any place the request names first (stage 3), propose a value for each open field, and mark those values as proposed. The look is the exception: its line stays "pending" until the screenshot arrives, and the same message asks for the screenshot or "add later".
- **Otherwise:** start at the first open stage and take one stage per turn, waiting for the player's answer before the next.

Open with one line naming the stages ahead, and say that "just write it" skips to the draft at any point. When the player says it, go to `SKILL.md` step 2 with the answers so far, invent the rest including the look, and list it all under **Assumed / invented**.

### The player's RP experience

In that first message, ask how much RP the player has done, unless the request or conversation already says: new to RP, some experience or experienced. This is about the player, not the character, and it sets how you work for the rest of the session. A one-message brief asks it alongside the confirmation.

Never hold up the work for it. With "just write it" or a specific request on an existing profile, don't ask: use what the request implies, otherwise some experience. If the player doesn't answer, use some experience and mark it *(proposed)* in the brief.

| | New to RP | Some experience | Experienced |
|---|---|---|---|
| **Explaining** | Explain terms such as IC, OOC, hook, god-moding and sides in plain words at first use, and say what each stage is for | Explain only what is specific to Forever or TRP3 | Skip the explanations |
| **Broad ideas** | Ideas with one clear want and one fear, easy to play from the first scene | As the stages describe | Can offer more complex ideas: conflicting loyalties, an unreliable public story |
| **Profile** | Plain template 3 with little markup. Add **First scene** to the player notes | As `SKILL.md` step 4 describes | Offer a designed template 1 or 2 page with heavier markup |
| **Stage 8** | Recommend the voice guide. Walk through pasting in full, and explain what each Roleplay style setting means | As stage 8 describes | Offer the voice guide. Give the paste order in one message and ask if they want the walkthrough |

Every answer gets the same lore checks, in-game name rules, character limits, self-check list and revision offers, and the player still sets the consent options. Experience changes how much you explain and how complex the character is, not how well the profile is checked.

## Asking

Use `AskUserQuestion` when it is available, otherwise short numbered questions in the reply. Options need to come from the references: class options from `forever-lore.md` section 3, broad ideas from the lore just read. `AskUserQuestion` takes at most four options, so ask for the faction before the race. For a longer list, such as a race's classes, write the options out and take the answer as text.

Every stage accepts "invent it", and an invention is shown in the brief for approval. A conflict with the lore is handled as in `SKILL.md` step 2, at the stage where it appears.

## Stages

| # | Stage | Done when |
|---|---|---|
| 1 | **Identity:** faction, race, class, level (see below) | The pair is valid in `forever-lore.md` section 3, or the player accepted the closest fit. A Forsaken paladin has been offered Bandarion Keep. A new character's level is a whole number from 1 to 60 |
| 2 | **Look:** see below | The screenshot was read and its look noted, or the player chose "add later" |
| 3 | **Broad ideas:** see below | The player chose or shaped an idea, so who they are, what they want, what they fear, what stands in the way, and where they come from and live now are all settled. `lore/world.md` and each place's file are read, or the place is noted as having no file (`SKILL.md` step 3) |
| 4 | **Name:** check theirs, or offer three options | The first and last in-game names pass `profile-craft.md` section 6, with counts shown |
| 5 | **Flavour:** age, pronouns, tone, what they miss, what they enjoy, trait sliders | Every field has a value, and the age fits `forever-lore.md` section 2 |
| 6 | **Brief:** see below | The player confirmed it, and it is saved as `brief.md` |
| 7 | **Draft:** `SKILL.md` steps 2–5, written from the brief | `profile.md` is saved, every item on the self-check list holds, and the player accepted the profile |
| 8 | **Finish:** see below | The player accepted or declined the voice guide, and each TRP3 tab was covered or skipped |

### Stage 1: the level

Ask a new character's level, offering 1 as the default because a newly created character is usually level 1, and let the player give any other. If the request doesn't say, it doesn't hold the stage open: put level 1 in the brief, marked *(proposed)*. Don't ask for an existing profile, whose brief shows a level only if the player or the profile gives one.

The level is the character's in-game progress, not their life experience, so a level 1 can still be a veteran. It only sets the starting point: what they are doing now, in Currently and the hooks, stays within what that level can reach in play. It is recorded in the brief and nowhere else. Don't state it in the TRP3 profile or the voice guide, because it changes as the character plays and the text would go out of date.

### Stage 2: the look

The in-game look decides what the physical description can say, so ask for a screenshot of the character. The player can paste it into the chat if the client allows that, or give a path. WoW saves to the `Screenshots` folder in the client's install folder (`_forever_` for Forever), as JPG unless set otherwise. If it is a TGA file you can't read, ask them to paste it, or to type `/console screenshotFormat jpg` and take another.

Note what the character model fixes: skin, hair, eyes, build. Gear can change, so treat it as a suggestion. Say what you see in the brief, so the player can catch the wrong character or a misreading.

With **"add later"**, leave out the physical description and eye colour, mark them as pending in the profile, and keep At first glance to things that don't depend on the look. Adding the screenshot later follows [Existing profiles](#existing-profiles).

### Stage 3: broad ideas

Offer three ideas, a few lines each: who they are, what they want, what they fear, where they come from, why they are leaving now and the tone. Each one keeps everything the player has said, fits the look, and is built on a specific from the lore you read. Then stop and wait: the player can pick one, mix them or ask for more. Until then, write no files and don't fill in the later stages.

### Stage 6: the brief

```markdown
# <Full name>: brief
*<Faction> · <Race> <Class> · Level <n> · In-game name: <First> (<n>) <Last> (<n>)*

- **Look:** <what the screenshot shows, or "pending">
- **From / lives:** <places; note any with no lore file>
- **Who:** …
- **Wants:** …
- **Fears:** …
- **In the way:** …
- **Setting out:** <new characters: why they are leaving and where they head first; the Currently line is built from this>
- **Age / pronouns / tone:** …
- **Misses / enjoys:** …
- **Traits:** <sliders and their leans>

**Player's RP experience:** <new to RP, some experience or experienced>
**Lore flags:** <each conflict, the fix and how to revert it>
**Proposed or invented:** <everything the player did not say>
```

Mark each value the player did not give with *(proposed)* on its line, including small ones such as pronouns and tone. End by asking the player to confirm or change the brief. Every line except the look carries a value, because an open line comes back later as a thin section in the profile and voice guide.

### Stage 8: finishing

Start only after the player has accepted the profile, even when a calling skill requires the voice guide, because the guide is built on the profile.

1. Offer the voice guide (`voice-guide.md`). If accepted, save it as `voice-guide.md`.
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
