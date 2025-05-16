---
description: |
  Automated prompt to resolve duplicate environment mechanical analysis charts cards in the Greenova Django project root view. Ensures only one chart card remains when a project is selected from the project selector tool, following all project coding, linting, and documentation standards.
mode: agent
tools:
  - filesystem
  - semantic_search
  - get_errors
  - run_tests
  - file_search
  - read_file
  - write_file
  - delete_file
  - sqlite
  - insert_edit_into_file
  - context7
  - json
  - git
  - sequential-thinking
---

# Goal

Remove duplicate environment mechanical analysis charts cards from the Greenova
Django project root ("/") view so that only one chart card remains when a
project is selected from the project selector tool.

# Context

- The root view ("/") currently displays multiple environment mechanical
  analysis charts cards when a project is selected from the project selector
  tool.
- This results in duplicate chart cards being rendered, which is not the
  intended behavior.
- The project enforces strict standards for configuration, linting, formatting,
  and testing.

# Objectives

- Identify and remove the logic or template code that causes duplicate
  environment mechanical analysis charts cards to be rendered in the root view
  when a project is selected.
- Ensure that only one chart card is displayed per project selection.
- Review and update the relevant Django view, template, and
  JavaScript/HTMX/hyperscript logic as needed.
- Ensure all code and configuration passes pre-commit, linting, formatting, and
  type checking.
- Add or update documentation to clarify the correct behavior for chart card
  rendering in the root view.
- Add or update a minimal test to verify that only one chart card is rendered
  per project selection.

# Sources

- /workspaces/greenova/templates/ (root view templates)
- /workspaces/greenova/views.py (or relevant view file)
- /workspaces/greenova/static/ (JS/HTMX/hyperscript logic)
- Project documentation on frontend and view rendering standards
- context7 for project-specific configuration

# Expectations

- Only one environment mechanical analysis charts card is rendered in the root
  view when a project is selected from the project selector tool.
- No duplicate chart cards are displayed.
- All code and configuration passes pre-commit, linting, formatting, and type
  checking.
- Documentation is updated to reflect the correct chart card rendering
  behavior.
- A minimal test verifies that only one chart card is rendered per project
  selection.

# Acceptance Criteria

- Only one environment mechanical analysis charts card is rendered in the root
  view per project selection.
- No duplicate chart cards are displayed.
- All code and configuration passes all pre-commit checks, linters, formatters,
  and type checkers.
- Documentation is updated and clear.
- A minimal test verifies correct chart card rendering.

# Instructions

- Review the root view template(s), view(s), and any related
  JavaScript/HTMX/hyperscript logic for duplicate chart card rendering.
- Remove or refactor the code that causes duplicate chart cards to be rendered.
- Ensure only one chart card is rendered per project selection.
- Run all linting, formatting, type checking and security checks to ensure
  compliance with project standards.
- Add or update a minimal test to verify only one chart card is rendered per
  project selection.
- Update documentation as needed.
- Iterate until all acceptance criteria are met.

# Additional Guidelines

1. **Restructured Text (RST)**: Use as the foundational layer for body,
   content, and messages for HTML.
2. **HTML**: Utilize for semantic structure and markup. Do not apply inline
   styles and scripts.
3. **Protobuf3**: Primary implementation for data serialization.
4. **Classless-CSS**: Apply minimal styling using Classless-PicoCSS as HTML.
5. **django-hyperscript**: Primary implementation for client-side interactions.
6. **django-htmx**: Secondary implementation for client-side interactions only
   to complement django-hyperscript.
7. **SASS/PostCSS**: Use for advanced styling needs when required.
8. **TypeScript**: Introduce only when django-hyperscript and django-htmx
   cannot meet the requirements. Use TypeScript for complex logic. Avoid using
   TypeScript for simple interactions that can be handled by django-hyperscript
   or django-htmx.
9. **AssemblyScript**: Primary implementation for critical client-side
   interactions and web assembly (WASM) implementations.
