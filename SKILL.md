---
name: wow-forever-rp-profile
description: Write, polish and lore-check roleplay (RP) character profiles for World of Warcraft Forever, formatted for the Total RP 3 (TRP3) addon.
---

# WoW: Forever RP profile writer

This skill turns a character idea into a **paste-ready Total RP 3 (TRP3) profile** for World of Warcraft: Forever. The profile is lore-friendly for Forever's setting (25 ADP, After the Dark Portal) and written so other roleplayers have something to walk up to.

Two things make this harder than generic character writing, and they're why the references exist:

1. **Forever has its own frozen moment in time.** It is the first year of the original game, in its own continuity, with a new race (the Skyborne) and new race/class pairs. Concepts lifted from retail, such as blood elves in the Horde, the Argent Crusade or a post-Cataclysm map, break immersion for other players. The details are in `references/forever-lore.md`, and the story of each place and boss is in `references/lore/`.
2. **TRP3 has a specific shape.** Tabs, fields, five glance slots, a 140-character tooltip cut-off and its own markup tags. If the output doesn't match, the player has to rework it before pasting. The details are in `references/trp3-fields.md`.

Craft guidance (what makes a profile good to interact with) is in `references/profile-craft.md`.

## Workflow

### 1. Route the request

- **A new character, or reworking an existing profile:** read `references/wizard.md` and follow it. It gathers the look, flavour and concept into a **brief** the player confirms, and it comes back to the steps below to draft. Consent settings (injury, death, romance and so on) stay out of it: the output lists them for the player to set.
- **"Just write it"**, or anything else that says to skip the questions: start at step 2 with what the request gives. Invent the rest, including the look, and list it all under **Assumed / invented**.
- **Anything else:** see [Other kinds of request](#other-kinds-of-request).

### 2. Check the concept against the lore

Read `references/forever-lore.md`. Check:

- The race/class pair is playable for that faction (section 3). **Forsaken paladins** have an official order in Forever, Bandarion Keep, so always offer it. The other five new pairs have no documented story in the references: frame them as this one character's path, and never claim no order exists.
- Ages and "they were there when…" claims fit the timeline (section 2). Forsaken have been undead for at most about 5 years.
- Nothing in the concept comes from after 25 ADP (section 5).
- Lore figures stay in the background.
- Skyborne are newcomers to Azeroth (section 7). They have no earlier history there.

When something conflicts, **say so plainly and briefly, with the reason, and offer a period-correct alternative.** A small conflict (a retail-only organisation name, an age that doesn't add up) gets fixed in the draft and flagged at the top, so the player can revert it. If the conflict breaks the concept (a draenei, a death knight of the Ebon Blade), ask before drafting and suggest the closest thing that does fit. It's the player's character, so don't lecture.

### 3. Root the character in the world

Read `references/lore/world.md`, then the file for every place and boss the character touches: birthplace, residence and anything in the backstory, including the ones you invent. This step is done when each place, dungeon and boss the profile will name has been read or noted as having no file.

| The character touches | Read, under `references/lore/` |
|---|---|
| A zone or city (a village, farm or other subzone is a `##` section of its zone's file) | `zones/<zone>.md` |
| A dungeon or raid | `zones/<dungeon>.md`, for its story and boss order |
| A boss | `bosses/<dungeon>/<boss>.md` |
| A group or person with no file (the Defias, Gryan Stoutmantle) | Grep the folder for the name |

File names are lower case and hyphenated, with apostrophes dropped (`zones/the-barrens.md`, `bosses/deadmines/rhahkzor.md`). Glob for the name when unsure.

Then use what you read:

- **Build on it.** The history and at least one hook carry specifics from these files: what happened to that place, who holds it now, what people there fear or owe. Retell it in your own words, because the files are under CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike) and their sentences stay out of the profile.
- **Keep bosses at a distance.** A boss is a lore figure who still stands. The character has fled them, lost someone to them, served under them or fears them. Molten Core and the other raids are not yet past victories (`forever-lore.md` section 5). A backstory where the character kills a boss is a small conflict, even when it is central: draft the nearest version that fits (a failed attempt, a lieutenant killed, a boast in the Rumours) and flag the change at the top.
- **Keep to what the character could know.** Boss files state truths ordinary people don't have, such as Lady Katrana Prestor being Onyxia. Public text holds at most a rumour; the truth goes in the player notes.
- **Rank the sources.** `forever-lore.md` wins where a file disagrees with it. The files come from Warcraft Wiki and can narrate events that haven't happened in 25 ADP: `onyxia.md` has her exposed and fled, whilst section 4 has her at court. Handle it like any other conflict in step 2.
- **Treat a missing file as a gap in the notes.** The place is still real. Mount Hyjal, Riverglades, Shen'dralas, Zephras Isle and the Darkspear Islands have no text yet, nor do some subzones and bosses (`MANIFEST.md` lists them). Follow `forever-lore.md` section 6: name the place without inventing its plot, and list anything you add under **Assumed / invented**.

### 4. Draft the profile

Follow `references/profile-craft.md` for the writing and `references/trp3-fields.md` for field rules. In particular:

- The physical description holds only what an observer can perceive. No god-moding (no telling readers how they feel or react).
- The history is the public version, ending in a **Rumours** block. Secrets go in the player notes.
- Give at least **three hooks** across the profile: a visible detail, a need or job, a rumour, an affiliation.
- The **in-game name** must follow Forever's rules (`profile-craft.md` section 6): first and last name, each 2–12 letters, no apostrophes or hyphens. Count it with a script if you can. Put apostrophe spellings and titles in the TRP3 fields instead.
- Currently and OOC must each be **140 characters or fewer**. Count them, using a quick script if you can run code, and show the counts.
- Use About **template 3** (Physical description / Personality / History) unless the player wants a designed page. Template 1 suits heavy markup; template 2 suits many small blocks.
- Use markup lightly (`{h3}` headings, the odd `{col:…}` accent). The text must read fine with tags stripped, because MyRolePlay and XRP users see it that way.

### 5. Self-check, then reply

Before sending, check the draft against the list at the end of this file. Then save it as `<character-name>/profile.md` (the Files section of `references/wizard.md`), present it in the format in `references/output-format.md`, and end with two or three **specific** revision offers, for example "a grimmer take on the history", "three alternative surnames", or "a template 1 version with headings and colour".

## Other kinds of request

- **Part-jobs** (just names, just a Currently line, just a lore check): do only that part, with the same rules: lore check (the step 3 files for each place and boss the text names, plus `world.md` if it touches the continents or ancient history), 140-character limit with the count shown, three name options each with an in-game spelling, character counts and a note on its feel.
- **Voice guides** (how the character talks, moves and reacts in play): read `references/voice-guide.md` and write to it, including a list of 10 sides you draft from the profile for the player to check. Base it on the character's profile; if there is none, write the profile first or ask for one.
- **Retail or Classic Era characters:** the TRP3 layout still applies, but this skill's lore checks are for Forever's 25 ADP. Say so, and don't apply Forever's anachronism list to a retail character.

## Self-check list

- [ ] Race/class/faction is valid in Forever, or flagged; Forsaken paladins are offered Bandarion Keep
- [ ] In-game name is first + last, each part 2–12 letters, no apostrophes, hyphens or titles; counts shown
- [ ] No post-25 ADP concepts, or flagged with a swap
- [ ] Ages agree with the timeline; Forsaken undead for ≤ ~5 years; Skyborne have no prior Azeroth history
- [ ] Every place, dungeon and boss named was read or noted as having no file; the history and a hook carry specifics from those files, in your own words
- [ ] Bosses stand undefeated by this character; what the character couldn't know is in the player notes
- [ ] Physical description holds only what can be observed; no god-moding; doesn't contradict the race's in-game look
- [ ] Secrets are in the player notes, not the public text
- [ ] At least three hooks; Rumours block present
- [ ] Currently ≤ 140 and OOC ≤ 140 characters, counts shown
- [ ] Consent settings left for the player
- [ ] Text reads cleanly with the tags stripped
- [ ] Assumptions and invented details are listed
