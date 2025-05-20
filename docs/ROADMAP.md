# Greenova Roadmap

## Phase 1: Core User and Project Management

1. Log in using the credentials created during setup
2. Create projects and define environmental mechanisms
3. Add obligations related to your projects
4. Assign responsibilities to users
5. Monitor compliance status
6. CRUD user profiles and company information
7. Drill down into mechanisms, then into procedures, then into obligations for
   detailed information
   - Perform CRUD operations on obligations
8. When hovering over the overdue obligations card, a tooltip will display a
   list of overdue obligations
   - Each overdue obligation will be listed and clickable, linking to its
     detail page
   - You can edit individual obligation records from their detail pages
   - Full CRUD operations are supported for overdue obligations

## Phase 2: Advanced Features and Reporting

- Generate charts and data visualizations using matplotlib (static) and Plotly
  (interactive)
- Integrate static and interactive charts into dashboard and reporting views
- Use protobuf3 for data serialization between backend and frontend, especially
  for chart data
- Implement compliance summaries, trend analysis, and printable reports
- Add notifications (email and SMS alerts)
- Support multi-tenancy (multiple organizations)
- Performance optimization (database indexing, query optimization)

## Phase 3: Modularization, UI/UX, and Auditing

- Modularize auditing and comment tracking (see PR #145)
- Refactor header bar and UI components for accessibility and responsiveness
  (see PR #149)
- Enhance filtering, sorting, and HTMX/JS logic for obligations and procedures
  (see PR #150)
- Add mechanism and procedure charts (see PR #154)
- Improve scrollable chart areas and UI consistency (see PR #148)
- Integrate authentication improvements and allauth (see PR #131)
- Enhance import/export and data validation (see PR #128)
- Add developer tooling, syntax checking, and bash aliases (see PR #103)

---

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [HTMX Documentation](https://htmx.org/)
- [Greenova GitHub Pull Requests](https://github.com/enveng-group/dev_greenova/pulls)
- [Greenova GitHub Issues](https://github.com/enveng-group/dev_greenova/issues)
- [Greenova Project Board](https://github.com/users/enveng-group/projects/8)
