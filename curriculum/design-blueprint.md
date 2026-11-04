# Design blueprint: The Operator's Curriculum (akitsuu edition)

Set in the akitsuu design system (https://claude.ai/artifact/HveZEi2ZQR8hqCZLDaSqc4).

- **Logo:** the supplied lockup SVG, path unchanged (`akitsuu-lockup.svg`, taken from the system's Letterhead template), sits on the cover. The mark alone, using the same supplied path cropped with one eye-width of clear space, sits in every footer.
- **Colour:** ground #F5F0E8, ink #2B2321, text-muted #574E49, ivory surface for the Memorise panel, and brown #7D3D1E for numerals and secondary figure marks. Red #C41E3A appears once per page, as the key element of that page's figure. There is no red on ink.
- **Type:** IBM Plex Sans 600 for display and headings, Lexend for body, captions and chips, and EB Garamond italic for one highlighted word per page. The build enforces the one-per-page rule.
- **Texture:** the emergence panel only, in ground lines at 30% on the ink cover, with no text over its dense side. It is clipped clear of the title.
- **Layout:** square corners, no shadows, no gradients. No border boxes except chips. Surfaces are flat fills.
- **Copy checks run at build:** no em or en dashes, no never-say words, and the brand name is always lowercase.
- **Illustrations:** each skill page carries an inline SVG teaching figure ("See it"). Slots are reserved for botanical plates in `plates/` (prompts in `botanical-plate-prompts.md`).
