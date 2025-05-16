---
description: |
  Redesign the mechanism analysis card in the root ("/") view so that, after a project is selected, the mechanism charts are displayed in a modern, responsive grid layout. The grid should dynamically resize and reflow based on the user's device (large desktop, small desktop, laptop, tablet, or mobile), eliminating the current horizontal scroll and improving visual appeal and usability. Use matplotlib to generate SVG charts and plotly to add interactivity, following all project technology and style standards.
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

Redesign the mechanism analysis card in the root ("/") view so that, after a
project is selected from the project selector tool, the mechanism charts are
displayed in a modern, visually appealing, responsive grid layout. The grid
must dynamically resize and reflow for all device sizes (large desktop, small
desktop, laptop, tablet, mobile). Use matplotlib to generate SVG charts for
each mechanism and use plotly to add interactivity, allowing users to gain
insights and analyze obligation records related to specific chart sections when
hovering over mechanism chart segments. Eliminate the current horizontal scroll
and improve usability and accessibility. Ensure that selecting a mechanism
chart still updates the view to show procedure analysis charts as before.

# Context

- Currently, after selecting a project, the mechanism analysis card displays
  pie charts in a single horizontal row, requiring horizontal scrolling to view
  all charts.
- Users click a mechanism chart to update the view to show procedure analysis
  charts.
- This layout is not visually appealing or user-friendly, especially on smaller
  screens.
- The project enforces strict Django, HTML, PicoCSS, and frontend interactivity
  standards (django-hyperscript, django-htmx).

# Objectives

- Replace the horizontal row/scroll of mechanism charts with a responsive grid
  layout.
- Use semantic HTML and PicoCSS for structure and styling.
- Use matplotlib to generate SVG charts for each mechanism.
- Use plotly to add interactivity to mechanism charts, enabling data insights
  and analysis on hover for obligation records related to chart sections.
- Ensure the grid dynamically resizes and reflows for all device sizes.
- Eliminate horizontal scroll for mechanism charts.
- Maintain or improve accessibility and usability.
- Ensure mechanism chart selection and view update logic remains functional
  (clicking a mechanism chart updates the view to show procedure analysis
  charts).
- Update or add tests to verify the new layout and interactivity.
- Update documentation to reflect the new design and behavior.

# Sources

- /workspaces/greenova/templates/ (root view and dashboard templates)
- /workspaces/greenova/static/ (JS, CSS, hyperscript, htmx)
- /workspaces/greenova/views.py (or relevant view file)
- context7 for project-specific frontend and layout standards

# Expectations

- Mechanism charts are displayed in a visually appealing, responsive grid.
- No horizontal scroll is required to view all mechanism charts.
- The grid adapts to different screen sizes and devices.
- All code and templates pass pre-commit, linting, formatting, and type
  checking.
- Documentation and tests are updated to match the new layout and behavior.

# Acceptance Criteria

- Mechanism charts are shown in a responsive grid layout in the mechanism
  analysis card.
- The grid dynamically resizes and reflows for all device sizes.
- No horizontal scroll is present for mechanism charts.
- Chart selection and view update logic works as before (clicking a mechanism
  chart updates the view to show procedure analysis charts).
- All code passes pre-commit, linting, formatting, and type checking.
- Documentation and tests are updated and clear.

# Instructions

- Review the current mechanism analysis card template(s), view(s), and static
  files.
- Refactor the mechanism chart display to use a responsive grid layout,
  following project standards and technology priority.
- Use matplotlib for SVG chart generation and plotly for interactive
  enhancements (including hover insights for obligation records).
- Ensure the grid is accessible and visually appealing on all device sizes.
- Maintain or improve the mechanism chart selection and view update logic.
- Update or add tests to verify the new layout and interactivity.
- Update documentation as needed.
- Iterate until all acceptance criteria are met.

# Additional Guidelines

1. Use RST for content/messages, semantic HTML for structure, PicoCSS for
   styling.
2. Use django-hyperscript for interactivity; django-htmx only as needed.
3. Avoid inline styles/scripts; use classless CSS and progressive enhancement.
4. Only use TypeScript or advanced CSS if simpler solutions are insufficient.
5. Ensure accessibility and responsive design best practices.
