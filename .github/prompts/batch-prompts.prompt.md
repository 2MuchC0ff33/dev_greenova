# Sequential Micro Prompts for Mechanism Analysis Card Redesign

Below are sequential micro prompts for redesigning the mechanism analysis card
with a responsive grid layout and interactive charts. Execute these prompts in
order, ensuring each step meets its acceptance criteria before proceeding to
the next.

## Micro Prompt 1: Analysis of Current Implementation

---

description: | Analyze the current implementation of the mechanism analysis
card in the root view to understand its structure, dependencies, and
functionality. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- context7

---

### Goal

Analyze the current implementation of the mechanism analysis card in the root
("/") view to understand its structure, data flow, and how the horizontal
scroll mechanism works.

### Context

The current mechanism analysis card displays pie charts in a single horizontal
row, requiring horizontal scrolling to view all charts. We need to understand
this implementation before redesigning it into a responsive grid layout.

### Objectives

- Identify all relevant files (templates, views, CSS, JS) related to the
  mechanism analysis card
- Understand how mechanism charts are currently generated and rendered
- Identify how chart selection updates the view to show procedure analysis
  charts
- Document the current data flow from backend to frontend
- Analyze the current chart generation mechanism

### Sources

- Root view templates
- Related view functions/classes
- JavaScript/hyperscript files handling chart interactions
- CSS files styling the charts
- Any other relevant files

### Expectations

- Provide a comprehensive analysis of the current implementation
- Document the file structure and relationships
- Explain how charts are currently generated and rendered
- Identify potential challenges for the redesign

### Acceptance Criteria

- Complete documentation of all files involved in the current mechanism
  analysis card
- Clear explanation of the current chart generation and rendering process
- Understanding of data flow from backend to frontend
- Identification of key functions/methods that will need to be modified

### Documentation References

- [Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/) -
  Use `context7` or `fetch` to access
- [HTMX](https://htmx.org/docs/) - Use `context7` or `fetch` to access
- [django-hyperscript](https://github.com/LucLor06/django-hyperscript#readme) -
  Use `context7` or `fetch` to access
- [Matplotlib](https://matplotlib.org/stable/users/index) - Use `context7` or
  `fetch` to access
- [PicoCSS Classless](https://picocss.com/docs/classless) - Use `context7` or
  `fetch` to access

## Micro Prompt 2: Design Responsive Grid Layout

---

description: | Design a responsive grid layout for the mechanism analysis card
that works across all device sizes. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- write_file
- insert_edit_into_file
- context7

---

### Goal

Design and implement a responsive grid layout for the mechanism charts that
dynamically adjusts to different screen sizes.

### Context

Based on the analysis from the previous step, we now need to replace the
horizontal scrolling row with a responsive grid layout using HTML and PicoCSS.

### Objectives

- Create a responsive grid layout using semantic HTML
- Implement CSS grid or flexbox system that follows project standards
- Ensure the grid adapts to different screen sizes (desktop, tablet, mobile)
- Maintain accessibility standards
- Replace horizontal scrolling with a properly flowing grid

### Sources

- Project frontend standards from context7
- PicoCSS documentation
- Current template files

### Expectations

- Modify the template structure to use a responsive grid layout
- Follow the project's frontend technology priority order
- Ensure the solution is as simple as possible while meeting requirements
- Implement proper responsive breakpoints for different device sizes

### Acceptance Criteria

- Grid layout properly adapts to different screen sizes without horizontal
  scrolling
- All chart containers have appropriate sizing and spacing
- Layout uses semantic HTML and follows PicoCSS standards
- Chart containers are visually appealing and evenly distributed
- Layout passes accessibility checks

### Documentation References

- [PicoCSS Grid System](https://picocss.com/docs/grid) - Use `context7` or
  `fetch` to access
- [PicoCSS Classless](https://picocss.com/docs/classless) - Use `context7` or
  `fetch` to access
- [Web Accessibility Initiative (WAI-ARIA)](https://www.w3.org/WAI/standards-guidelines/aria/) -
  Use `fetch` to access
- [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout) -
  Use `fetch` to access
- [CSS Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout) -
  Use `fetch` to access
- [HTML Semantic Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) -
  Use `fetch` to access

## Micro Prompt 3: Implement Matplotlib SVG Chart Generation

---

description: | Modify chart generation to use matplotlib for creating SVG
charts for each mechanism. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- write_file
- insert_edit_into_file
- context7
- get_errors

---

### Goal

Implement matplotlib-based SVG chart generation for mechanism charts to replace
current charting method.

### Context

Based on the previous steps, we need to modify the chart generation mechanism
to use matplotlib for creating SVG charts for mechanisms, which will later be
enhanced with plotly interactivity.

### Objectives

- Implement matplotlib chart generation for mechanism data
- Export charts as SVG format for better quality and scalability
- Ensure charts are properly styled according to project standards
- Optimize chart generation for performance
- Maintain existing data flow and chart selection functionality

### Sources

- Matplotlib documentation
- Current chart generation code
- Project styling standards

### Expectations

- Create functions to generate SVG charts using matplotlib
- Implement proper styling for the charts
- Ensure charts are properly sized for the grid layout
- Maintain data integrity and visual representation

### Acceptance Criteria

- SVG charts are successfully generated using matplotlib
- Charts maintain visual consistency with the application design
- Chart generation is efficient and doesn't impact performance
- SVG charts are properly integrated into the grid layout
- Chart selection functionality remains intact

### Documentation References

- [Matplotlib](https://matplotlib.org/stable/users/index) - Use `context7` or
  `fetch` to access
- [Matplotlib SVG Output](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.savefig) -
  Use `context7` or `fetch` to access
- [Django and Matplotlib Integration](https://github.com/scidam/django_matplotlib) -
  Use `context7` or `fetch` to access
- [Web Accessibility for Data Visualizations](https://www.w3.org/WAI/WCAG21/Understanding/sensory-characteristics.html) -
  Use `fetch` to access

## Micro Prompt 4: Add Plotly Interactivity to Charts

---

description: | Enhance the matplotlib SVG charts with plotly interactivity to
show insights on hover. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- write_file
- insert_edit_into_file
- context7
- get_errors

---

### Goal

Add plotly-based interactivity to the mechanism charts to display insights
about obligation records when hovering over chart segments.

### Context

Now that we have matplotlib SVG charts in a responsive grid, we need to enhance
them with plotly interactivity to provide data insights on hover events.

### Objectives

- Implement plotly overlays or transformations for the matplotlib charts
- Add hover functionality to display obligation record insights
- Ensure data is appropriately fetched and displayed
- Maintain performance with potentially large datasets
- Keep the interactive elements accessible and user-friendly

### Sources

- Plotly documentation
- Current chart data sources
- Obligation record structure

### Expectations

- Add interactive elements to charts without disrupting the grid layout
- Implement efficient data retrieval for hover insights
- Follow project standards for frontend interactions
- Ensure interactive elements are accessible

### Acceptance Criteria

- Charts show relevant data insights when hovered
- Interaction is smooth and responsive
- Data displayed on hover is accurate and helpful
- Interactivity works across different device sizes
- Solution follows project's frontend technology priority order

### Documentation References

- [Plotly](https://plotly.com/python/) - Use `context7` or `fetch` to access
- [Plotly Events](https://plotly.com/python/hover-events/) - Use `fetch` to
  access
- [Plotly with SVG](https://plotly.com/python/svg-export/) - Use `fetch` to
  access
- [Accessibility in Data Visualization](https://www.w3.org/WAI/WCAG21/Understanding/non-text-content.html) -
  Use `fetch` to access
- [django-hyperscript](https://github.com/LucLor06/django-hyperscript#readme) -
  Use `context7` or `fetch` to access

## Micro Prompt 5: Preserve Chart Selection Functionality

---

description: | Ensure that clicking on a mechanism chart still updates the view
to show procedure analysis charts. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- write_file
- insert_edit_into_file
- context7
- get_errors
- run_tests

---

### Goal

Preserve and optimize the functionality where clicking a mechanism chart
updates the view to show procedure analysis charts.

### Context

We've redesigned the layout and chart generation, but we need to ensure the
original functionality where clicking a chart updates the view is preserved.

### Objectives

- Maintain click event handlers for mechanism charts
- Ensure view updates correctly when a chart is selected
- Optimize the transition between mechanism and procedure views
- Test functionality across different devices and screen sizes
- Ensure the interaction is accessible

### Sources

- Current chart selection implementation
- Event handling code
- View update functionality

### Expectations

- Preserve click-to-update functionality with the new grid layout
- Optimize the code for better performance
- Ensure smooth transitions between views
- Keep the code clean and maintainable

### Acceptance Criteria

- Clicking a mechanism chart successfully updates the view to show procedure
  analysis charts
- Transition between views is smooth and intuitive
- Functionality works consistently across all device sizes
- Implementation follows project standards for frontend interactions
- All interactions are accessible

### Documentation References

- [django-hyperscript](https://github.com/LucLor06/django-hyperscript#readme) -
  Use `context7` or `fetch` to access
- [HTMX](https://htmx.org/docs/) - Use `context7` or `fetch` to access
- [Django URL Dispatcher](https://docs.djangoproject.com/en/5.2/topics/http/urls/) -
  Use `context7` or `fetch` to access
- [Web Accessibility Initiative (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/) -
  Use `fetch` to access
- [PicoCSS Classless](https://picocss.com/docs/classless) - Use `context7` or
  `fetch` to access

## Micro Prompt 6: Implement Responsive Behavior Testing

---

description: | Create and run tests to verify the responsive behavior of the
redesigned mechanism analysis card. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- write_file
- insert_edit_into_file
- context7
- get_errors
- run_tests

---

### Goal

Implement tests to verify that the redesigned mechanism analysis card behaves
correctly across different screen sizes and devices.

### Context

After implementing all the changes, we need to ensure that the responsive grid,
chart rendering, and interactivity work correctly across different
environments.

### Objectives

- Create tests for responsive grid behavior
- Test chart rendering at different screen sizes
- Verify interactive features work across devices
- Test chart selection functionality
- Ensure accessibility across different contexts

### Sources

- Project testing standards
- Current test suite
- Responsive testing best practices

### Expectations

- Create comprehensive tests for the redesigned component
- Test across multiple breakpoints and device contexts
- Verify all functionality works as expected
- Document any edge cases or limitations

### Acceptance Criteria

- All tests pass across different simulated screen sizes
- Chart rendering is verified to work correctly
- Interactive features are confirmed functional
- Chart selection and view updates work as expected
- All functions meet accessibility standards

### Documentation References

- [pytest-django](https://pytest-django.readthedocs.io/) - Use `context7` or
  `fetch` to access
- [Django Testing Tools](https://docs.djangoproject.com/en/5.2/topics/testing/tools/) -
  Use `context7` or `fetch` to access
- [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/WCAG21/Understanding/) -
  Use `fetch` to access
- [Responsive Testing Best Practices](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) -
  Use `fetch` to access
- [PicoCSS Breakpoints](https://picocss.com/docs/breakpoints) - Use `context7`
  or `fetch` to access

## Micro Prompt 7: Documentation and Final Review

---

description: | Document the changes made to the mechanism analysis card and
perform a final review of the implementation. mode: agent tools:

- filesystem
- semantic_search
- file_search
- read_file
- write_file
- insert_edit_into_file
- context7
- get_errors
- run_tests

---

### Goal

Create comprehensive documentation for the redesigned mechanism analysis card
and perform a final review of the implementation.

### Context

Now that all functionality has been implemented and tested, we need to document
the changes and perform a final review to ensure everything meets the
requirements and follows project standards.

### Objectives

- Document all changes made during the redesign
- Update any relevant developer documentation
- Review code against project standards
- Verify all acceptance criteria from previous steps
- Identify any areas for future improvement

### Sources

- All modified files
- Project documentation standards
- Previous micro prompt acceptance criteria

### Expectations

- Create clear documentation of the redesigned component
- Update README or other documentation files as needed
- Review all code against project standards
- Ensure all acceptance criteria have been met

### Acceptance Criteria

- Comprehensive documentation of the redesign is created
- All code follows project standards
- All features work as specified
- All tests pass
- The implementation meets all requirements from the original task
- No horizontal scrolling is required to view mechanism charts
- Charts are interactive and provide insights on hover
- Layout is responsive across all specified device sizes

### Documentation References

- [Django Documentation Style Guide](https://docs.djangoproject.com/en/5.2/internals/contributing/writing-documentation/) -
  Use `context7` or `fetch` to access
- [Python DocString Conventions (Google Style)](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) -
  Use `fetch` to access
- [W3C Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/) -
  Use `fetch` to access
- [Matplotlib Documentation Standards](https://matplotlib.org/stable/devel/index.html) -
  Use `context7` or `fetch` to access
- [Plotly Documentation Guide](https://plotly.com/python/getting-started/) -
  Use `context7` or `fetch` to access
