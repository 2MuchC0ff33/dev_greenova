from datetime import datetime
from typing import Any, TypedDict

from _typeshed import Incomplete
from dashboard.mixins import ChartMixin, ProjectAwareDashboardMixin
from django.contrib.auth.models import AbstractUser
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, TemplateView
from obligations.models import Obligation
from projects.models import Project

SYSTEM_STATUS: str
APP_VERSION: str
LAST_UPDATED: datetime
logger: Incomplete

class DashboardContext(TypedDict):
    projects: QuerySet[Project]
    selected_project_id: str | None
    system_status: str
    app_version: str
    last_updated: datetime
    user: AbstractUser
    debug: bool
    error: str | None
    user_roles: dict[str, str]

def get_selected_project_id(request: HttpRequest) -> str | None: ...

class DashboardHomeView(ProjectAwareDashboardMixin, TemplateView):
    template_name: str
    login_url: str
    redirect_field_name: str
    request: HttpRequest
    include_charts: bool

    @property
    def selected_project_id(self) -> str | None: ...

    def get_template_names(self) -> list[str]: ...

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

    def add_specific_charts(self, context: dict[str, Any]) -> None: ...

    def get_projects(self) -> QuerySet[Project]: ...

    def get_active_obligations_count(self) -> int: ...

    def get_overdue_obligations_count(self) -> int: ...

    def get_obligations_trend(self) -> int: ...

    def get_upcoming_deadlines_count(self) -> int: ...

    def get_active_mechanisms_count(self) -> int: ...

class ChartView(ChartMixin, ProjectAwareDashboardMixin, TemplateView):
    template_name: str

    @property
    def selected_project_id(self) -> str | None: ...

    def get_queryset(self) -> QuerySet[Project]: ...

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class ProjectsAtRiskView(ProjectAwareDashboardMixin, ListView):
    model: type[Project]
    template_name: str
    context_object_name: str

    def get_queryset(self) -> QuerySet[Project]: ...

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class UpcomingObligationsView(ProjectAwareDashboardMixin, ListView):
    template_name: str
    context_object_name: str

    def get_queryset(self) -> QuerySet[Obligation]: ...

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
