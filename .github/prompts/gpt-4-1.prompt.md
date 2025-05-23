---
description: |
  Replicate the same grid and container layouts for the procedure charts as already implemented with the mechanism charts, including SVG matplotlib and Plotly interactivity on hover for the pie charts. Ensure the UI, interactivity, and accessibility are consistent between mechanisms and procedures. Update backend, templates, and static assets as needed.
mode: agent
tools:
  - filesystem
  - dbcode
  - context7
  - json
  - git
  - sequential-thinking
  - github
---

# GitHub Copilot Prompt Template for Automated Issue Resolution

## Goal

Replicate the grid and container layouts for the procedure charts to match
those used for the mechanism charts, including SVG matplotlib and Plotly
interactivity on hover for the pie charts.

## Context

Currently, the mechanism charts use a responsive grid layout and provide
interactive pie charts (SVG/Plotly) with hover tooltips. The procedure charts
do not match this layout or interactivity. For a consistent user experience,
the procedure charts must use the same grid/container structure and interactive
chart features as the mechanism charts.

## Objectives

- Update the procedure charts UI to use the same grid and container layouts as
  the mechanism charts.
- Ensure procedure pie charts support SVG (matplotlib) and Plotly interactivity
  on hover, including tooltips.
- Refactor backend, templates, and static assets to support these features.
- Maintain accessibility and responsive design.
- Remove any redundant or conflicting code.
- Ensure all pre-commit checks (ruff, pylint, mypy, stylelint, djlint, eslint,
  etc.) pass.

## Sources

- `/greenova/procedures/templates/procedures/procedure_charts.html`
- `/greenova/procedures/templates/procedures/components/_procedure_charts.html`
- `/greenova/mechanisms/templates/mechanisms/mechanism_charts.html`
- `/greenova/procedures/views.py`
- `/greenova/procedures/figures.py`
- `/greenova/mechanisms/figures.py`
- Any related static files (CSS/JS/TS) for chart rendering and interactivity

## Expectations

- Use all available MCP servers and tools to analyze and replicate the layouts
  and interactivity.
- Refactor code, templates, and static assets for consistency and
  maintainability.
- Test in the browser for visual and interactive consistency.
- Run all pre-commit checks to validate compliance.
- Document the changes and reasoning.

## Acceptance Criteria

- Procedure charts use the same grid and container layouts as mechanism charts.
- Procedure pie charts support SVG/Plotly interactivity on hover, with
  tooltips.
- UI and accessibility are consistent between mechanisms and procedures.
- Application runs without errors or missing variable issues.
- All pre-commit checks pass.
- The solution is documented with an explanation of the root cause and the fix.

## Instructions

- Review the mechanism chart grid/container and interactivity implementation.
- Update the procedure chart templates and backend to match the mechanism chart
  structure and features.
- Implement or adapt SVG/Plotly interactivity for procedure pie charts.
- Test and validate as required.
- Document the changes and reasoning in the solution.
