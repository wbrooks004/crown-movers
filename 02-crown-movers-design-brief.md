# Crown Movers / Déménagement Crown Design-System Brief

## Official company names

- **English:** Crown Movers
- **French:** Déménagement Crown

Use the English name on English interfaces and the French name on French interfaces. Do not translate the French company name back to Crown Movers inside French copy.

## Business and positioning

Crown Movers is a professional Montreal moving company serving residential, commercial, local, long-distance, packing, furniture, storage-related and specialty moving needs.

The redesign should position the company as:

- Organized and operationally competent
- Dependable and transparent
- Careful with customers' belongings
- Local to Montreal and experienced with its moving conditions
- Friendly but serious
- Premium in quality without appearing expensive or pretentious
- Conversion-focused without becoming aggressive or sales-heavy

The core emotional promise is: **Moving day, handled.**

## Existing website and photography permission

Reference the current website at https://www.crownmovers.ca/ for services, brand assets, trust signals, content structure and real company photography.

You are explicitly permitted to use **any photograph currently published on the existing Crown Movers website** as reference or source imagery in the proposed design system, component library and page mockups.

Photography rules:

- Prioritize real Crown Movers employees, trucks, uniforms, furniture protection, packing, homes, apartments, offices and Montreal environments.
- Prefer real site photography over stock photography or AI-generated movers.
- You may crop, reframe and apply restrained colour correction for design concepts.
- Do not distort the logo, truck branding, uniforms or people.
- Do not fabricate customer situations, awards, partnerships or credentials.
- When a source image is too small for production, use it as a layout reference and label it **higher-resolution original required**.
- Do not hotlink images in the final production website. Original media files should be copied into the new WordPress media library after rights and resolution are confirmed.

## Visual direction

The design should feel calm, controlled, direct, established and locally authoritative.

Use visual cues inspired by:

- The angular Crown Movers crown symbol
- The orange-to-amber logo gradient
- Branded trucks, uniforms and moving equipment
- Organized steps, routes, labels and logistics
- Protective blankets, wrapped furniture and clean equipment
- Montreal apartments, stairs, elevators, streets and seasonal conditions

Avoid:

- Generic moving-company templates
- Cartoon boxes or movers
- Generic purple or blue SaaS gradients
- Glassmorphism
- Fake black-and-gold luxury styling
- Large pill buttons everywhere
- Excessive rounded cards
- Repeating crown icons as decoration
- Excessive orange backgrounds
- Unverified review, pricing, award or certification claims

## Colour direction

Use the supplied token files and palette board. The official logo gradient sampled from the supplied logo is approximately:

- Crown Coral: `#F04836`
- Crown Amber: `#F89C3E`

Important accessibility rule: use dark text on orange and amber buttons. White text does not consistently meet WCAG AA contrast on these colours.

## Typography

Use no more than two type families.

Recommended starting point:

- **Headings:** Archivo
- **Body and UI:** Inter

Typography should feel sturdy, clean and highly readable, with compact headings and practical body copy. French labels can be 15-30% longer, so avoid fixed-width or fixed-height text containers.

## Primary conversion actions

1. Request a free quote
2. Call Crown Movers / Appeler Déménagement Crown
3. Check availability
4. Calculate a starting moving estimate
5. Explore moving services and service areas

Treat the quote and estimate experience as a major product interface, not as a generic contact form.

## Required design-system coverage

Create one coherent bilingual system containing:

- Logo rules for light and dark backgrounds
- Colour tokens and accessibility combinations
- Fluid typography and spacing
- Grid, containers and responsive breakpoints
- Headers, navigation and language switcher
- Buttons, links and focus states
- Forms, validation and multi-step quote/estimate flow
- Service cards and service-page patterns
- Location cards and location-page patterns
- Review, rating, trust and statistics components
- Process steps, FAQs and calls to action
- Footer and mobile sticky conversion controls
- Desktop and mobile examples
- English and French content examples

## Implementation constraints

The website will be built with:

- WordPress
- Bricks Builder
- Automatic CSS
- Frames
- Advanced Custom Fields
- Polylang
- Rank Math

Prefer reusable global classes, semantic design tokens, CSS Grid, Flexbox, ACF-driven templates, accessible HTML and minimal JavaScript. Avoid layouts dependent on fragile absolute positioning or heavy animation libraries.
