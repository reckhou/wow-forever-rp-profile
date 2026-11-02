# Writing a voice guide

A voice guide tells whoever voices the character, a person or an AI, how they talk, move and react. An AI reads it as instructions and follows every line of it, so what the guide repeats, the AI repeats. A worked example is [`samples/baldrake-cavethrone/voice-guide.md`](../samples/baldrake-cavethrone/voice-guide.md).

## Sections

Write these, in this order, and leave out any that has nothing to say:

1. **In one line:** who they are, in one sentence.
2. **Sides:** see below. Every guide has this section.
3. **Registers:** the few ways they speak, each with when it applies and an example line.
4. **Dialect:** how they spell and phrase things, kept light. Include a short table of plain English against their version.
5. **Signature lines:** a few, marked for use once a scene at most.
6. **Answers to the usual openers:** what they say to the questions strangers ask first.
7. **Body language:** ready-made emotes.
8. **Companion:** a pet or demon's role and voice, if they have one.
9. **Do and don't:** only what the sections above do not already cover.
10. **Sample scenes:** one or two short ones, showing the registers in use.

## Sides

The sides are the character's range: what they can bring to any moment. Draft the list yourself from the profile and show it to the player to check, so nobody has to write it by hand.

Put it under a heading named `## His sides`, `## Her sides` or `## Their sides`, with one bullet per side, in this form:

```markdown
## His sides
Baldrake shows one of these at a time, whichever the moment calls for.
- **The showman:** vanity, titles, a bow for every occasion, stories that grow with each telling.
- **The man with a price:** when work, a deal or a boast invites it, he names a figure and haggles for fun.
```

A list is finished when all of these hold:

- **It has 10 sides, and the strongest traits are among them.** One flat list, with no main side and no ranking. Fewer sides leave too little to draw on, and the character starts to repeat.
- **Each side plays several ways.** "The sceptic: no time for omens or spirits" fits a hundred moments; "hates the loa of the north shore" fits one. Name what the side covers, then stop.
- **The strongest trait is held to its moments.** It gets a condition saying when it comes out: "when work, a deal or a boast invites it". Without one, it takes over every reply.
- **The quiet sides are there too.** Include what they fear, what they miss, who they bicker with, what they enjoy, and at least one side where they stop performing.
- **Every side comes from the profile.** Add no new history. A side may draw on anything the profile says, including the Personality text and the traits.

## Keep the guide to what the character does

- **Say when a trait comes out, and let it rest:** "money is his running joke, and a joke needs a rest". Leave out orders of frequency ("in every scene", "always"), because they make that trait the point of every reply.
- **Write "mostly not" by default, not "never".** People have exceptions, and an AI follows "never" to the letter, so the character can't break the habit even when a scene calls for it. Write "rarely" or "seldom", and say what would make them do it: "he rarely swears by the loa, unless real fear gets the better of him". Keep "never" for hard limits, such as the lore, what the character can't know, or a limit the player set.
- **Spread the examples.** Across the signature lines, openers and sample scenes, let no single trait fill most of them, because examples teach as strongly as rules.
- **Leave out the character's level.** It only sets the starting point in the brief, and it goes out of date as the character plays.
- **Keep advice for the human out of the guide.** Tips on playing the character, finding scenes or growing them over time go in a separate player notes file, because an AI reads them as things to act on in the scene.
