# Design System Inspired by Apple

## 1. Visual Theme & Atmosphere

Apple's web language is a precision editorial system that alternates between gallery-like calm and retail-density information blocks. The visual tone stays restrained: broad neutral canvases, quiet chrome, and product imagery given almost all of the expressive weight. The interface is engineered to disappear so hardware, materials, and finish options become the narrative foreground.

Across the five analyzed pages, the rhythm is consistent but not monolithic. Marketing surfaces (homepage and Environment) use cinematic black-and-light chaptering, while commerce surfaces (Store and Shop flows) introduce tighter spacing, more utility controls, and denser card stacks without breaking the core brand grammar. The result is one system with two gears: showcase mode and transaction mode.

Typography is the stabilizer. SF Pro Display carries hero and merchandising hierarchy with compact line heights and controlled tracking, while SF Pro Text handles product metadata, navigation, filters, and dense selection UI. The typography stays understated, but the scale range is wide enough to support both billboard hero messaging and micro utility labels.

**Key Characteristics:**
- App surface rhythm: pale app background (`#F1F2F6`) alternating with white card surfaces (`#FFFFFF`) and clean border separation (`#E7E8EB`, `#EBEDF3`, `#F8F8F8`)
- Primary accent pair for action and highlight semantics (`#FFC300`, `#4A5CFF`) with secondary support colors for categorized UI states
- Dual operating modes in one system: cinematic showcase modules and dense commerce configurators
- Heavy reliance on imagery and material finishes; UI chrome remains visually thin
- Tight headline metrics (SF Pro Display, semibold) paired with compact body/link typography (SF Pro Text)
- Pill and capsule geometry as signature action language (`18px` to `980px` and circular controls)
- Depth used sparingly through three shadow tokens (`@@ Shadow`, `## Shadow`, `** Shadow`) and light border-led separation
- Multi-page color-block rhythm: pale app background -> white cards -> primary accent moments -> secondary palette state modules

## 2. Color Palette & Roles

> **Source:** Attached color board screenshot.  
> The screenshot defines the base brand palette and light-mode surface tokens. For implementation, separate colors into **Core Brand Tokens**, **Light Mode Semantic Tokens**, and **Dark Mode Semantic Tokens** so components can switch themes without rewriting every color value.

### 2.1 Core Brand Tokens

Core tokens do not change by mode. They define the recognizable brand colors and should be referenced by semantic tokens rather than used directly everywhere.

| Token | Name | Hex | Role |
|------|------|-----|------|
| `brand.primary.yellow` | Primary Yellow | `#FFC300` | Brand highlight, featured CTA, selected emphasis, icon border accent |
| `brand.primary.blue` | Primary Blue | `#4A5CFF` | Main action, active state, selected state, key interaction color |
| `brand.secondary.orange` | Orange | `#EE9A01` | Warning-like emphasis, category color, avatar/random accent |
| `brand.secondary.blue` | Blue | `#075ED9` | Information emphasis, secondary blue state, data/category distinction |
| `brand.secondary.red` | Red | `#E4032E` | Error, destructive, alert, strong negative emphasis |
| `brand.secondary.green` | Green | `#16813B` | Success, completed, confirmed, positive state |
| `brand.secondary.gray` | Gray | `#5F6368` | Neutral category, inactive state, subdued utility accent |

### 2.2 Light Mode Color Tokens

Use these values as the default app theme. This mode is closest to the attached screenshot.

#### Light Mode Surface & Border

| Semantic Token | Hex | Use |
|------|-----|-----|
| `color.background.default` | `#F1F2F6` | Main app background |
| `color.background.subtle` | `#F8F8F8` | Very light section background, soft divider area |
| `color.surface.default` | `#FFFFFF` | Cards, panels, input fields, modal surfaces |
| `color.surface.elevated` | `#FFFFFF` | Floating cards, dropdowns, popovers |
| `color.surface.selected` | `#E9F0FE` | Selected row/card background when blue emphasis is needed |
| `color.border.strong` | `#E7E8EB` | Strongest visible border for cards, tables, containers |
| `color.border.default` | `#EBEDF3` | Default border for inputs, dividers, cards |
| `color.border.subtle` | `#F8F8F8` | Softest border for low-contrast separation |

#### Light Mode Typography

| Semantic Token | Hex | Use |
|------|-----|-----|
| `color.text.primary` | `#161A1C` | Main title, strongest text |
| `color.text.secondary` | `#26292D` | Secondary title, main body text |
| `color.text.tertiary` | `#818496` | Subtitle, helper text, description |
| `color.text.muted` | `#A9AEB5` | Metadata, low-emphasis labels |
| `color.text.disabled` | `#CDD3DB` | Disabled, placeholder, unavailable text |
| `color.text.inverse` | `#FFFFFF` | Text on dark or blue surfaces |

#### Light Mode Action & State

| Semantic Token | Hex | Use |
|------|-----|-----|
| `color.action.primary` | `#4A5CFF` | Primary button, selected control, active navigation |
| `color.action.primary.text` | `#FFFFFF` | Text/icon on primary blue |
| `color.action.highlight` | `#FFC300` | Featured CTA, brand highlight, important notice accent |
| `color.action.highlight.text` | `#161A1C` | Text/icon on primary yellow |
| `color.focus.ring` | `#4A5CFF` | Keyboard focus, selected outline, active form state |
| `color.link.default` | `#075ED9` | Text link and secondary blue action |

#### Light Mode Status Tints

| Semantic Token | Foreground | Background | Use |
|------|------------|------------|-----|
| `color.status.warning` | `#EE9A01` | `#FFF7E1` | Caution, pending, needs review |
| `color.status.info` | `#075ED9` | `#E9F0FE` | Information, guide, neutral notice |
| `color.status.danger` | `#E4032E` | `#FCE8E5` | Error, failed, destructive action |
| `color.status.success` | `#16813B` | `#E7F4EB` | Success, completed, confirmed |
| `color.status.neutral` | `#5F6368` | `#E8EAEE` | Neutral chip, inactive category, utility badge |

### 2.3 Dark Mode Color Tokens

The screenshot does not provide a separate dark-mode board, so these are **implementation-safe dark-mode counterpart tokens** derived from the same brand palette. Keep the brand identity visible, but reduce eye strain by using dark surfaces, lifted text, and slightly brighter action colors.

#### Dark Mode Surface & Border

| Semantic Token | Hex | Use |
|------|-----|-----|
| `color.background.default` | `#121316` | Main dark app background |
| `color.background.subtle` | `#181A1F` | Secondary dark background, app shell areas |
| `color.surface.default` | `#1A1C20` | Cards, panels, input fields, modal surfaces |
| `color.surface.elevated` | `#22252B` | Floating cards, dropdowns, popovers |
| `color.surface.selected` | `#252A46` | Selected row/card background when blue emphasis is needed |
| `color.border.strong` | `#3A3E46` | Strongest visible border in dark UI |
| `color.border.default` | `#2E323A` | Default dark border for inputs, dividers, cards |
| `color.border.subtle` | `#24272E` | Softest dark border for low-contrast separation |

#### Dark Mode Typography

| Semantic Token | Hex | Use |
|------|-----|-----|
| `color.text.primary` | `#F5F7FA` | Main title, strongest text on dark surfaces |
| `color.text.secondary` | `#D6DAE2` | Secondary title, main body text |
| `color.text.tertiary` | `#A9AEB5` | Subtitle, helper text, description |
| `color.text.muted` | `#818796` | Metadata, low-emphasis labels |
| `color.text.disabled` | `#5F6670` | Disabled, placeholder, unavailable text |
| `color.text.inverse` | `#161A1C` | Text on yellow or very light surfaces |

#### Dark Mode Action & State

| Semantic Token | Hex | Use |
|------|-----|-----|
| `color.action.primary` | `#6B78FF` | Primary button, selected control, active navigation in dark mode |
| `color.action.primary.text` | `#FFFFFF` | Text/icon on primary blue |
| `color.action.highlight` | `#FFC300` | Featured CTA, brand highlight, important notice accent |
| `color.action.highlight.text` | `#161A1C` | Text/icon on primary yellow |
| `color.focus.ring` | `#7D87FF` | Keyboard focus, selected outline, active form state |
| `color.link.default` | `#8FA0FF` | Text link and secondary blue action on dark surfaces |

#### Dark Mode Status Tints

| Semantic Token | Foreground | Background | Border | Use |
|------|------------|------------|--------|-----|
| `color.status.warning` | `#FFD761` | `#3A2A10` | `#5D4614` | Caution, pending, needs review |
| `color.status.info` | `#8FA0FF` | `#121D3A` | `#243E78` | Information, guide, neutral notice |
| `color.status.danger` | `#FF6B7E` | `#3A111A` | `#6A1A2A` | Error, failed, destructive action |
| `color.status.success` | `#4AD276` | `#10291A` | `#1E4B2D` | Success, completed, confirmed |
| `color.status.neutral` | `#C5CBD4` | `#2D3138` | `#3A3E46` | Neutral chip, inactive category, utility badge |

### 2.4 Mode-Aware Shadow Tokens

Use screenshot shadow tokens for light mode. In dark mode, rely more on surface stepping and borders; shadows should be softer but deeper, not visually gray or muddy.

| Token | Light Mode | Dark Mode | Use |
|------|------------|-----------|-----|
| `shadow.default` | `0 4px 12px 0 rgba(0, 0, 0, 0.15)` | `0 8px 20px 0 rgba(0, 0, 0, 0.30)` | Default elevated card, modal, prominent surface |
| `shadow.compact` | `0 2px 4px 0 rgba(0, 0, 0, 0.15)` | `0 4px 8px 0 rgba(0, 0, 0, 0.25)` | Compact controls, small cards, dropdowns |
| `shadow.soft` | `0 4px 12px 0 rgba(0, 0, 0, 0.05)` | `0 4px 12px 0 rgba(0, 0, 0, 0.20)` | Gentle thematic depth and large background modules |
| `shadow.outline` | `0 0 0 1px rgba(231, 232, 235, 1)` | `0 0 0 1px rgba(255, 255, 255, 0.06)` | Border-like elevation where real shadow is too heavy |

### 2.5 CSS Token Example

```css
:root,
[data-theme="light"] {
  --brand-primary-yellow: #FFC300;
  --brand-primary-blue: #4A5CFF;

  --color-background-default: #F1F2F6;
  --color-background-subtle: #F8F8F8;
  --color-surface-default: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-surface-selected: #E9F0FE;

  --color-border-strong: #E7E8EB;
  --color-border-default: #EBEDF3;
  --color-border-subtle: #F8F8F8;

  --color-text-primary: #161A1C;
  --color-text-secondary: #26292D;
  --color-text-tertiary: #818496;
  --color-text-muted: #A9AEB5;
  --color-text-disabled: #CDD3DB;
  --color-text-inverse: #FFFFFF;

  --color-action-primary: #4A5CFF;
  --color-action-primary-text: #FFFFFF;
  --color-action-highlight: #FFC300;
  --color-action-highlight-text: #161A1C;
  --color-focus-ring: #4A5CFF;
  --color-link-default: #075ED9;

  --shadow-default: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
  --shadow-compact: 0 2px 4px 0 rgba(0, 0, 0, 0.15);
  --shadow-soft: 0 4px 12px 0 rgba(0, 0, 0, 0.05);
}

[data-theme="dark"] {
  --brand-primary-yellow: #FFC300;
  --brand-primary-blue: #4A5CFF;

  --color-background-default: #121316;
  --color-background-subtle: #181A1F;
  --color-surface-default: #1A1C20;
  --color-surface-elevated: #22252B;
  --color-surface-selected: #252A46;

  --color-border-strong: #3A3E46;
  --color-border-default: #2E323A;
  --color-border-subtle: #24272E;

  --color-text-primary: #F5F7FA;
  --color-text-secondary: #D6DAE2;
  --color-text-tertiary: #A9AEB5;
  --color-text-muted: #818796;
  --color-text-disabled: #5F6670;
  --color-text-inverse: #161A1C;

  --color-action-primary: #6B78FF;
  --color-action-primary-text: #FFFFFF;
  --color-action-highlight: #FFC300;
  --color-action-highlight-text: #161A1C;
  --color-focus-ring: #7D87FF;
  --color-link-default: #8FA0FF;

  --shadow-default: 0 8px 20px 0 rgba(0, 0, 0, 0.30);
  --shadow-compact: 0 4px 8px 0 rgba(0, 0, 0, 0.25);
  --shadow-soft: 0 4px 12px 0 rgba(0, 0, 0, 0.20);
}
```

### 2.6 Theme Usage Rules

- Do not hard-code screenshot hex values directly into components. Use semantic tokens like `color.background.default`, `color.surface.default`, and `color.text.primary`.
- Keep `brand.primary.yellow` and `brand.primary.blue` as brand-level constants, then map them to action/highlight tokens by mode.
- In light mode, separation can rely on pale background, white cards, border tokens, and the original screenshot shadows.
- In dark mode, separation should rely on darker surface steps, subtle borders, and restrained shadows.
- Yellow should remain a highlight color, not a general background color. Overusing yellow weakens the brand cue.
- Blue should remain the clearest interaction signal across both light and dark modes.

## 3. Typography Rules

### Font Family
- **Display Family:** `SF Pro Display`, fallbacks `SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif`
- **Text Family:** `SF Pro Text`, fallbacks `SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif`
- **Usage Split:** Display family handles hero/product headlines and merchandising headings; Text family handles navigation, controls, labels, and dense commerce copy.

### Hierarchy
| Role | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|--------|-------------|----------------|-------|
| Hero Display XL | 80px | 600 | 1.00-1.05 | -1.2px | Environment/store hero scale |
| Hero Display L | 56px | 600 | 1.07 | -0.28px | Homepage hero moments |
| Section Display | 48px | 500-600 | 1.08 | -0.144px | Major chapter headings |
| Product Heading | 40px | 600 | 1.10 | normal | Product and campaign section titles |
| Feature Display | 38px | 600 | 1.21 | 0.152px | Device and merchandising callouts |
| Promo Display | 32px | 300-600 | 1.09-1.13 | 0.128px to 0.352px | Module-level sub-heroes |
| Card/Product Title | 28px | 600 | 1.14 | 0.196px | Tile-level naming and key copy |
| Utility Heading | 24px | 600 | 1.17 | 0.216px / -0.2px | Configurator and grouped content headers |
| Link/Action Heading | 21px | 600 | 1.14-1.38 | 0.231px | Larger promotional links |
| Subhead | 19px | 600 | 1.21 | 0.228px | Compact section intros |
| Body Primary | 17px | 400 | 1.47 | -0.374px | Standard body and retail descriptions |
| Body Emphasis | 17px | 600 | 1.24 | -0.374px | Emphasized labels and key values |
| Control Label | 14px | 400-600 | 1.29-1.47 | -0.224px | Buttons, helper labels, compact nav text |
| Micro UI | 12px | 400-600 | 1.00-1.33 | -0.12px | Fine print, micro labels |
| Legal/Meta | 10px | 400 | 1.30-1.47 | -0.08px | Dense metadata and legal support text |

### Principles
- **Continuity across page types:** The same typographic DNA spans cinematic launches and product-purchase flows, preventing a brand split between marketing and commerce.
- **Compression at scale:** Display tiers use tight leading and controlled tracking to feel machined and product-first.
- **Readable density at retail depth:** SF Pro Text balances compactness with enough vertical rhythm for long product lists and option matrices.
- **Measured weight ladder:** 600 is the dominant emphasis weight; 700 appears selectively; 300 is used sparingly for contrast in larger lines.

### Note on Font Substitutes
- Closest freely available substitutes: `Inter` for text-heavy implementation and `SF Pro Display-like` metrics approximated with `Inter Tight` for headings.
- When substituting, increase line-height slightly (+0.02 to +0.06) on body sizes and reduce negative tracking intensity to preserve readability.

## 4. Component Stylings

### Buttons
- **Primary Fill Action:** `#4A5CFF` background, `#FFFFFF` text, 8px radius, compact horizontal padding (commonly 8px 15px). Used for decisive progression actions and selected states.
- **Highlight Fill Action:** `#FFC300` background, `#161A1C` text, 8px radius. Used for branded emphasis, featured controls, and high-attention actions.
- **Pill/Capsule Action Family:** large capsule actions at `18px`-`56px` radii and extreme pill links at `980px`. Establishes Apple’s soft but precise call-to-action silhouette.
- **Utility Filter/Button Shells:** light shells (`#FFFFFF` or `#F8F8F8`) with subtle borders (`#EBEDF3` / `#E7E8EB`) for dense configuration contexts.
- **Pressed Behavior:** active controls commonly reduce scale or shift fill slightly to indicate physical press confirmation.

### Cards & Containers
- **Editorial/Product Cards:** light cards on `#F1F2F6` or `#FFFFFF` fields with minimal framing and image-first composition.
- **Dark Utility Cards:** dark neutral steps (`#26292D` to `#5F6368`) used for overlays, media controls, and dark-context modules.
- **Configurator Panels:** rounded containers (often 12px-18px) with clear but restrained border definition.
- **Carousel/Spotlight Modules:** larger rounded shells (`28px`-`36px`) for featured content lanes.

### Inputs & Forms
- **Input Fields:** `#FFFFFF` backgrounds, dark text (`#161A1C`), and border-led containment (`#E7E8EB` / `#EBEDF3`).
- **Selection Controls:** circular/toggle-like control geometry appears frequently in product selection interfaces.
- **Density Strategy:** form fields remain visually quiet to keep device imagery and pricing hierarchy dominant.

### Navigation
- **Global Marketing Nav:** compact dark translucent bar with small-type links and restrained iconography.
- **Store/Sub-shop Nav Layers:** additional utility bars, chips, and segmented controls for category and product narrowing.
- **Link Hierarchy:** `#4A5CFF` and `#075ED9` remain the primary interactive signals while neutral text colors support dense navigation sets.

### Image Treatment
- **Object-First Photography:** hardware and accessories are foregrounded on controlled solid surfaces.
- **High-fidelity finish rendering:** reflective/material details are central to visual persuasion.
- **Mixed framing:** full-bleed hero scenes coexist with rounded retail cards and tightly cropped merchandising thumbnails.

### Other Distinctive Components
- **Product Configurator Matrix:** option stacks and selectors combining chips, radio-style controls, and contextual pricing/summary blocks.
- **Carousel Control Dots/Arrows:** circular control vocabulary in muted overlays for gallery progression.
- **Environment Story Panels:** narrative chapters that blend editorial typography with cinematic product/environment visuals.

## 5. Layout Principles

### Spacing System
- Base unit is effectively `8px`, but the system supports dense micro-steps for precision alignment.
- Frequently reused spacing values across pages: `2`, `4`, `6`, `7`, `8`, `9`, `10`, `12`, `14`, `17`, `20` px.
- Universal rhythm constants visible across both marketing and retail flows: `8px` unit scaffolding with `14-20px` utility intervals for component padding and list spacing.

### Grid & Container
- **Showcase pages:** large central columns with broad horizontal breathing room and full-width color chapters.
- **Commerce pages:** tighter multi-column product and control grids with frequent modular stacking.
- **Container behavior:** constrained readable core with generous outer margins at desktop widths.

### Whitespace Philosophy
- **Scene pacing:** major visual chapters use broad top/bottom breathing room.
- **Information compaction where needed:** retail pages deliberately compress spacing to expose more actionable information per viewport.
- **Contrast-led separation:** section transitions rely more on surface changes than decorative separators.

### Border Radius Scale
- **5px:** tiny utility links/tags and minor small shells.
- **8px-12px:** standard controls and compact fields.
- **16px-18px:** cards, module frames, and commerce panels.
- **28px-36px:** larger module and spotlight containers.
- **56px / 100px / 980px:** capsules, large pills, and signature elongated CTA forms.
- **50%:** circular media and selection controls.

## 6. Depth & Elevation

| Token | X | Y | Blur | Spread | Color | CSS Value | Use |
|------|---:|---:|-----:|-------:|-------|-----------|-----|
| `@@ Shadow` | 0 | 4 | 12 | 0 | `#000000` / 15% | `0 4px 12px 0 rgba(0, 0, 0, 0.15)` | Default elevated card, modal, and prominent surface shadow |
| `## Shadow` | 0 | 2 | 4 | 0 | `#000000` / 15% | `0 2px 4px 0 rgba(0, 0, 0, 0.15)` | Compact controls, small cards, dropdowns, and subtle raised elements |
| `** Shadow` | 0 | 4 | 12 | 0 | `#000000` / 5% | `0 4px 12px 0 rgba(0, 0, 0, 0.05)` | Soft background elevation and gentle thematic depth |

Depth should stay light and utility-driven. Use `#F1F2F6` as the main background, `#FFFFFF` for card surfaces, and border tokens (`#E7E8EB`, `#EBEDF3`, `#F8F8F8`) before adding shadow.

### Decorative Depth
- Use `@@ Shadow` only when a surface needs clear separation from the background.
- Use `## Shadow` for compact UI where elevation should be visible but not dramatic.
- Use `** Shadow` for soft theme depth, pale cards, or large background modules.
- Avoid stacking multiple shadows on the same element unless a component explicitly requires a layered floating state.

## 7. Do's and Don'ts

### Do
- Use the surface foundation (`#F1F2F6`, `#FFFFFF`, `#161A1C`) as the structural base.
- Reserve `#4A5CFF` for genuine action/selection semantics and `#FFC300` for featured highlight moments.
- Keep typography tight and deliberate, especially at display scales.
- Maintain the capsule/circle geometry language for controls and key actions.
- Let product imagery carry visual drama; keep chrome understated.
- Use border-led containment (`#E7E8EB`, `#EBEDF3`, `#F8F8F8`) in dense contexts instead of heavy ornamentation.
- Preserve clear separation between modules while keeping the screenshot palette and shadow tokens shared.

### Don't
- Don’t introduce additional accent palettes that compete with the defined primary and secondary screenshot palette.
- Don’t overuse shadows, glow effects, or decorative gradients in core UI chrome; stay within `@@ Shadow`, `## Shadow`, and `** Shadow`.
- Don’t mix unrelated font families or loosen tracking indiscriminately.
- Don’t flatten all corners to a single radius; Apple uses purposeful radius tiers.
- Don’t overload commerce modules with thick borders or loud visual effects.
- Don’t remove the soft contrast cadence between `#F1F2F6`, `#FFFFFF`, border tokens, and text grays.
- Don’t treat marketing and purchase flows as separate design systems.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | 374px and below | Tightened retail controls, single-column product stacks |
| Mobile | 375px-640px | One-column modules, compact action rows, condensed selectors |
| Tablet | 641px-833px | Expanded cards and mixed 1-2 column transitions |
| Tablet Wide | 834px-1023px | More stable multi-column merchandising, larger text blocks |
| Desktop | 1024px-1240px | Full retail layouts and product comparison structures |
| Desktop Wide | 1241px-1440px | Marketing hero expansion and broader section spacing |
| Large Desktop | 1441px+ | Maximum chapter breathing room and wide editorial composition |

### Touch Targets
- Primary and secondary actions are generally presented in tap-friendly pill/button geometries.
- Circular media and selection controls align with minimum touchable intent in mobile contexts.
- Dense commerce UI uses compact labels but maintains clear hit regions via surrounding shape padding.

### Collapsing Strategy
- Marketing hero typography scales down in discrete tiers while preserving hierarchy contrast.
- Product and commerce grids collapse from multi-column to stacked cards with persistent selector visibility.
- Utility navigation compresses into simpler link/control groupings while preserving key actions.
- Option/configuration clusters become vertically sequenced to keep purchase flow linear on small screens.

### Image Behavior
- Product imagery preserves aspect and centrality through breakpoints.
- Hero visuals remain dominant on mobile, with text repositioned around media priority.
- Retail thumbnails stay legible via tighter crop logic and denser card stacking.
- Image-led modules continue to anchor the rhythm as layout density increases.

## 9. Agent Prompt Guide

### Quick Color Reference

#### Core Brand
- Primary yellow: **Primary Yellow** (`#FFC300`)
- Primary blue: **Primary Blue** (`#4A5CFF`)
- Secondary accents: Orange `#EE9A01`, Blue `#075ED9`, Red `#E4032E`, Green `#16813B`, Gray `#5F6368`

#### Light Mode
- Background: `color.background.default` = `#F1F2F6`
- Card/surface: `color.surface.default` = `#FFFFFF`
- Title text: `color.text.primary` = `#161A1C`
- Body text: `color.text.secondary` = `#26292D`
- Helper text: `color.text.tertiary` = `#818496`
- Default border: `color.border.default` = `#EBEDF3`
- Strong border: `color.border.strong` = `#E7E8EB`
- Primary action: `color.action.primary` = `#4A5CFF`
- Highlight action: `color.action.highlight` = `#FFC300`
- Default shadow: `shadow.default` = `0 4px 12px 0 rgba(0, 0, 0, 0.15)`

#### Dark Mode
- Background: `color.background.default` = `#121316`
- Card/surface: `color.surface.default` = `#1A1C20`
- Elevated surface: `color.surface.elevated` = `#22252B`
- Title text: `color.text.primary` = `#F5F7FA`
- Body text: `color.text.secondary` = `#D6DAE2`
- Helper text: `color.text.tertiary` = `#A9AEB5`
- Default border: `color.border.default` = `#2E323A`
- Strong border: `color.border.strong` = `#3A3E46`
- Primary action: `color.action.primary` = `#6B78FF`
- Highlight action: `color.action.highlight` = `#FFC300`
- Default shadow: `shadow.default` = `0 8px 20px 0 rgba(0, 0, 0, 0.30)`

### Example Component Prompts
- "Design a clean product hero on `#F1F2F6` with SF Pro Display semibold headline (48-56px), concise supporting copy, and two capsule CTAs using `#4A5CFF` and `#FFC300`."
- "Create a configuration panel on white (`#FFFFFF`) with 18px rounded cards, `#E7E8EB` border fields, SF Pro Text 17px body copy, and compact option selectors."
- "Build a card grid alternating `#F1F2F6` and `#FFFFFF` surfaces, with image-first cards, `@@ Shadow` or `** Shadow`, and 14-17px SF Pro Text metadata."
- "Generate a carousel control cluster using circular buttons (50% radius), muted gray overlays, and clear active feedback for gallery navigation."
- "Compose a mixed page rhythm: `#F1F2F6` background -> `#FFFFFF` cards -> dense list module while keeping `#4A5CFF` for actions and `#FFC300` for featured highlights."

### Iteration Guide
1. Lock the surface foundation first (`#F1F2F6`, `#FFFFFF`, `#161A1C`) before tuning accents.
2. Keep `#4A5CFF` and `#FFC300` scarce and purposeful; if everything is accented, hierarchy collapses.
3. Tune typography in this order: display scale, body readability, then micro labels.
4. Match radius by component class (field, card, capsule, circle) rather than one-size-fits-all rounding.
5. Increase density gradually when moving from showcase sections to commerce sections.
6. Validate that product imagery remains the strongest visual layer after each revision.

### Known Gaps
- Distinct semantic status colors (error/warning/success) were not consistently visible in the extracted page set.
- Some interaction micro-states vary by module and are not represented as universal system tokens.
- A few retail modules expose context-specific typography overrides that do not appear across all five pages.
