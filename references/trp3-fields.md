# Total RP 3 (TRP3) field reference

**Abbreviations:** TRP3 = Total RP 3; IC / OOC = in character / out of character; MSP = Mary Sue Protocol (the shared format TRP3 uses to exchange basic profile data with MyRolePlay and XRP).

Taken from the TRP3 source code (github.com/Total-RP/Total-RP-3, `main` branch, October 2026, release 3.5.3). TRP3 runs on the Forever client: its `.toc` lists interface `16001` beside retail's, and the 3.5.2 changelog fixes a bug "on Forever".

## Contents

1. Characteristics tab
2. About tab
3. Miscellaneous tab
4. Status: Currently and OOC
5. Markup tags
6. Practical limits and gotchas

---

## 1. Characteristics tab

| Field | Notes from TRP3's own tooltips |
|---|---|
| Title | Short, like "Countess", "Magus", "Lord". TRP3 says to avoid long titles and use Full title for those |
| First name | Mandatory. If blank, TRP3 uses the in-game name. Nicknames are allowed. Free text, so apostrophe spellings Forever's in-game names forbid ("Ka'jinto") belong here |
| Last name | Optional |
| Full title | A longer epithet or a different title: "Warden of Thendal Grove" |
| Race | Free text. Custom values are allowed ("Half-elf") |
| Class | Free text. Custom values are allowed ("Knight", "Arcanist", "Elite marksman"). Class colour can be set too |
| Age | A number or an adjective ("young", "venerable") |
| Birthplace | Region, zone or continent. A button fills in the current location |
| Residence | Home or crash spot. A button fills in the current location and can mark it on the map |
| Eye colour | Worth filling in even if the face is usually hidden |
| Height | A number ("170 cm", "6'5\"") or a word ("tall") |
| Body shape | "Slim", "Muscular", "Stout" … |
| Relationship status | Dropdown: Single, Taken, Married, Divorced, Widowed, or Do not show |

**Additional information** rows, each with an icon, a name and a value. The presets:

| Preset | Shown on tooltip? |
|---|---|
| Pronouns | Yes |
| Guild name | Yes |
| Guild rank | Yes |
| Voice reference | Yes |
| Nickname | No |
| House name | No |
| Motto | No |
| Facial features | No |
| Tattoos | No |
| Piercings | No |

Custom rows (any name) are also allowed. Only add rows that say something: three good ones beat ten filler ones.

**Personality traits:** sliders between two opposite traits. The built-in pairs:

Chaotic–Lawful · Chaste–Lustful · Forgiving–Vindictive · Altruistic–Selfish · Truthful–Deceitful · Gentle–Brutal · Superstitious–Rational · Renegade–Paragon · Cautious–Impulsive · Ascetic–Bon vivant · Valorous–Spineless

Custom traits take any two names, icons and colours (for example Pious–Doubting, or Homesick–Wanderlust for a Skyborne). Give each trait a direction and a strength ("strongly Cautious", "slightly Forgiving") and the player drags the slider to match. Four to six traits is plenty; pick the ones that drive behaviour.

## 2. About tab

The player picks one of three templates. **Only the selected template is visible to others.**

| Template | Shape | Best for |
|---|---|---|
| 1 | One free-text page with full markup (section 5) | Players who want headings, colour, images and a designed look |
| 2 | A list of independent frames, each with an icon, a background and text | Many short themed blocks (Appearance / Rumours / Known associates …) |
| 3 | Three fixed frames: **Physical description**, **Personality**, **History**, each with an icon and a background. Empty frames are hidden | Most profiles. The default recommendation |

A music theme can also be attached; the player picks it from TRP3's in-game list.

## 3. Miscellaneous tab

**At first glance:** **5 slots**. Each has an icon, a title (the "attribute name") and a short text. These are what another player notices *immediately*, and community etiquette treats them as fair game to react to without any prior IC introduction. Use them for things that start conversations: "Feather-braided hair", "Smells of brine and ozone", "Kirin Tor letter of passage". Keep each text to one to three sentences.

**Roleplay style:** each of these can be Yes, No or With player permission:
- Accept character injury
- Accept character death
- Accept character romance
- Accept criminal activity (being mugged, for example)
- Accept loss of control (imprisonment, mind control)
- Guild membership: IC or OOC

These are the **player's own consent settings**. Never choose them for the player. List them and leave the values blank unless the player has stated their preference.

## 4. Status: Currently and OOC

Set from the TRP3 toolbar or dashboard and shown on the character's tooltip:

| Field | Purpose |
|---|---|
| Character status | In character / Out of character |
| Roleplay experience | Newcomer (icon on tooltip), Veteran (no icon), Newcomer Guide (icon; signals willingness to help beginners) |
| **Currently** | "Anything that is currently happening or relevant to your character": a present-tense IC hook |
| **Other information (OOC)** | "Anything important about you, as a player": time zone, walk-ups welcome, contact, limits |

**By default other TRP3 users see only the first 140 characters** of Currently and of OOC in the tooltip. Keep both at **140 characters or fewer**, spaces included, and count them.

## 5. Markup tags

The About tab renders TRP3's tags as HTML. Template 1 uses them most; templates 2 and 3 accept them in frame text as well.

| Tag | Effect |
|---|---|
| `{h1}…{/h1}`, `{h2}…{/h2}`, `{h3}…{/h3}` | Headings; add `:c` or `:r` to centre or right-align: `{h2:c}Rumours{/h2}` |
| `{p}…{/p}`, `{p:c}…{/p}`, `{p:r}…{/p}` | Paragraph; centre or right-align |
| `{col:RRGGBB}…{/col}` | Hex colour: `{col:c8a2ff}lavender{/col}` |
| `{col:x}…{/col}` | Short colours: `r` red, `g` green, `b` blue, `y` yellow, `p` purple, `c` cyan, `w` white, `o` orange, `0` black |
| `{icon:ICON_NAME:SIZE}` | Inline game icon: `{icon:inv_misc_feather_01:20}` |
| `{img:PATH:WIDTH:HEIGHT:ALIGN}` | Image; ALIGN is `l`, `c` or `r` (centre by default). Images must sit outside paragraph tags. A very small height gives a decorative divider line |
| `{link*URL*TEXT}` or `[TEXT](URL)` | Clickable link; the URL is shown for the player to copy |
| `{twitter*HANDLE*TEXT}`, `{bsky*HANDLE*TEXT}` | Social links |

## 6. Practical limits and gotchas

- **Icon names:** TRP3 3.5 lets players search icons by name or ID. Forever uses the original game's art, so retail-only icons may be missing. Suggest an icon as a search word ("feather", "scroll", "skull") rather than as an exact filename, unless the filename is a long-standing classic one.
- **Colour:** the About background is pale parchment by default. Bright yellow, cyan and white text is hard to read on it. Use colour sparingly, for headings or one accent.
- **Length:** TRP3 sets no small limit on About text, and 3.5.x removed the export size limit. Readers skim, though. Aim for about 150–300 words for Physical description, 80–200 for Personality, and 200–500 for History.
- **MSP interop:** players using MyRolePlay or XRP receive the names, titles, basic characteristics, Currently, OOC and the About text **with all tags stripped**. With template 3, Physical description and Personality are merged into their Description, and History goes to their History. Glances, trait sliders and images don't reach them, so the text must read cleanly with the tags removed. Never let colour alone carry meaning.
- **Profile import strings:** TRP3 3.5.x can export and import a whole profile as an encoded text block. This skill doesn't generate those strings: they can't be checked outside the game, and a malformed one would fail to import. The player pastes each field instead.
