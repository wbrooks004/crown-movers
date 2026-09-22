# Crown Movers — Bricks & Automatic.css Development Standards

## Purpose

This file defines the implementation rules for the Crown Movers WordPress rebuild.

Technology:

* WordPress
* Bricks Builder 2.4
* Automatic.css 4.x
* ACF Pro
* BricksExtras
* WS Form
* Polylang Pro

Maintainability and design-system consistency are mandatory.

---

## Automatic.css Is the Design-System Authority

Automatic.css should control the global visual system wherever possible.

Before creating any custom value, check whether ACSS already provides an appropriate:

* Variable
* Token
* Utility
* Framework setting
* Typography value
* Spacing value
* Width
* Grid
* Gap
* Color
* Radius
* Shadow
* Button system
* Responsive value

Use the existing ACSS system first.

---

## Global Variables Before Custom Values

Never create arbitrary values when the global design system already provides the intended value.

Example:

Prefer:

`border-radius: var(--radius);`

over:

`border-radius: 12px;`

when `--radius` represents the project's intended global radius.

Apply the same principle to:

* Spacing
* Font sizes
* Line height
* Content width
* Colors
* Shadows
* Gaps
* Section spacing
* Border radius
* Container behavior

Global design decisions should remain adjustable from the ACSS dashboard whenever reasonably possible.

---

## Avoid Magic Numbers

Avoid arbitrary values such as:

* `13px`
* `27px`
* `43rem`
* `7px`

unless there is a legitimate technical or visual reason.

First determine whether an ACSS token can solve the requirement.

If a new value is genuinely needed, determine whether it belongs in:

1. ACSS/global design system
2. Component-level custom property
3. Exceptional local implementation

Do not create repeated one-off values.

---

## Class-Only Styling

All visual styling must be applied through CSS classes.

Do not visually style Bricks elements directly using element-level controls as the normal implementation approach.

Do not use inline styles.

Do not use element IDs as styling hooks.

Do not create styling that can only be found by opening an individual Bricks element.

The site should remain manageable through:

* ACSS
* Global variables
* Utility classes
* Semantic classes
* Reusable component classes

If an unavoidable technical exception occurs, identify it explicitly.

---

## BEM Naming

Use semantic BEM-style naming for custom components.

Pattern:

`.block`

`.block__element`

`.block--modifier`

`.block__element--modifier`

Example:

`.service-card`

`.service-card__icon`

`.service-card__title`

`.service-card__text`

`.service-card__action`

`.service-card--featured`

---

## Semantic Naming

Name classes according to the component or semantic role.

Good:

* `.hero`
* `.service-card`
* `.quote-panel`
* `.review-card`
* `.location-card`
* `.moving-process`
* `.site-footer`

Avoid visual naming such as:

* `.blue-box`
* `.left-column`
* `.big-heading`
* `.rounded-card`
* `.white-text`
* `.twenty-gap`

Class names should survive future visual redesigns where possible.

---

## Class Strategy

Use this preference hierarchy:

1. ACSS global configuration
2. ACSS global variables
3. ACSS utility classes
4. Semantic BEM component classes
5. Component-specific custom properties
6. Exceptional custom implementation

Do not create custom semantic classes when an existing ACSS utility cleanly solves a simple styling requirement.

Do not overuse utilities when a coherent component deserves its own semantic class architecture.

Use judgment.

---

## Bricks Structure

Keep Bricks structure clean.

Prefer:

* Semantic HTML elements
* Necessary wrappers only
* Reusable components
* Templates
* Dynamic content
* Query loops
* Global classes

Avoid unnecessary nested containers.

A wrapper should generally have a reason related to:

* Layout
* Semantics
* Responsive behavior
* Component structure
* Interaction
* Accessibility

---

## Reusability

When the same UI appears repeatedly, evaluate whether it should become:

* A Bricks component
* A template
* A reusable section
* A query-driven structure
* An ACF-driven component

Do not independently rebuild the same pattern on many pages.

Examples likely to benefit from reuse:

* Service cards
* Reviews
* FAQs
* Location cards
* CTAs
* Quote sections
* Trust modules
* Navigation components
* Footer components

---

## ACF Pro

Use ACF when structured data provides a real benefit.

Good candidates include data that:

* Appears in multiple locations
* Varies by service
* Varies by city
* Powers templates
* Requires consistent administration
* Will scale with Toronto
* Needs relationships
* May be queried dynamically

Do not turn every paragraph or heading into an ACF field.

Use normal WordPress/Bricks content when structured data provides no meaningful advantage.

---

## Service and Location Architecture

Anticipate:

* Multiple services
* Montreal
* Toronto
* Possible future service areas
* English
* French

Avoid structures that hard-code Montreal into every component when the same component will eventually serve Toronto.

Use structured data where it makes future expansion materially easier.

---

## BricksExtras

Use BricksExtras when it provides meaningful functionality or implementation advantages.

Prefer native Bricks when native functionality solves the requirement cleanly.

Do not create unnecessary dependency on specialty elements.

---

## WS Form

WS Form is the standard forms system.

Build forms with:

* Accessible labels
* Clear validation
* Useful errors
* Logical grouping
* Mobile usability
* Appropriate confirmation states

Primary conversion is form submission.

Forms should be technically reliable and easy to complete.

---

## Polylang Pro

Polylang Pro manages English/French content relationships.

Account for multilingual requirements when implementing:

* Menus
* Templates
* Forms
* Dynamic content
* URLs
* ACF data
* Internal links
* Reusable components

Do not assume strings embedded in custom implementation will automatically translate correctly.

---

## Custom CSS

Custom CSS is acceptable when required.

It must follow:

* Semantic class architecture
* BEM where appropriate
* ACSS variables first
* Minimal duplication
* Responsive consistency
* Maintainability

Avoid unnecessary specificity.

Avoid `!important` unless a specific technical conflict justifies it.

Avoid selectors that depend heavily on fragile DOM nesting.

Prefer:

`.service-card__title`

over deeply nested selectors such as:

`.page-wrapper .section:nth-child(3) div > div h3`

---

## Custom JavaScript

Use JavaScript only when the interaction genuinely requires it.

Prefer native:

* HTML
* CSS
* Bricks
* BricksExtras

before custom JavaScript.

Custom JavaScript should be:

* Minimal
* Understandable
* Scoped
* Maintainable
* Accessible
* Performance-conscious

Do not introduce libraries for trivial effects.

---

## Performance

Prefer:

* Lean DOM
* Optimized media
* Appropriate image dimensions
* Modern image formats where appropriate
* Limited scripts
* Minimal unnecessary dependencies
* Efficient queries
* Reusable CSS

Avoid adding technical complexity for decorative effects.

---

## Accessibility

Implementation must support:

* Semantic HTML
* Correct heading structure
* Keyboard access
* Visible focus states
* Proper labels
* Accessible buttons and links
* Useful alt text
* Appropriate landmarks
* Valid interactive elements

Do not build clickable `div` elements when proper buttons or anchors should be used.

---

## Implementation Response Standard

When providing implementation guidance, do not give generic advice if a Bricks/ACSS-specific solution can be provided.

For components, specify where useful:

* Suggested HTML/Bricks structure
* BEM classes
* Relevant ACSS utilities
* Relevant ACSS variables
* Dynamic data
* ACF requirements
* Responsive considerations
* Accessibility considerations
* Reuse strategy

Do not invent nonexistent ACSS variables.

If the exact project token is unknown, identify the desired token concept and verify the available ACSS variable before implementation.

---

## Core Development Principle

A future developer should be able to understand and globally modify the website without hunting through hundreds of individually styled Bricks elements.

The site must behave like a coherent design system, not a collection of separately designed pages.

---