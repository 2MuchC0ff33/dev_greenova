from typing import Any, ClassVar

from _typeshed import Incomplete
from core.mixins import BreadcrumbMixin, PageTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from projects.models import Project

logger: Incomplete

class ChartMixin:
    """Mixin for chart-related dashboard views."""
    ...

class ProjectAwareDashboardMixin:
    """Mixin for project-aware dashboard views."""
    ...

class DashboardContextMixin(LoginRequiredMixin, BreadcrumbMixin, PageTitleMixin):
    """Mixin for dashboard views that provides common context data."""
    page_title: str
    breadcrumbs: ClassVar[list[tuple[str, None]]]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

    def _get_current_project_id(self) -> int | None: ...

    def _get_user_projects(self) -> QuerySet[Project]: ...

    def _add_chart_data(
        self,
        context: dict[str, Any],
        project_id: int | None,
    ) -> None: ...

    def _add_statistics(
        self,
        context: dict[str, Any],
        project_id: int | None,
    ) -> None: ...
