"""
Stub file for obligations.views.

This module provides type stubs for the views related to obligations management.
"""

import logging
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from mechanisms.models import EnvironmentalMechanism

from .forms import ObligationForm
from .models import Obligation

logger: logging.Logger
MAX_EVIDENCE_FILES: int

class ObligationSummaryView(LoginRequiredMixin, View):
    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...
    def _filter_by_status(
        self, queryset: QuerySet[Obligation], status_values: list[str]
    ) -> QuerySet[Obligation]: ...
    def apply_filters(
        self, queryset: QuerySet[Obligation], filters: dict[str, Any]
    ) -> QuerySet[Obligation]: ...
    def get_filters(self) -> dict[str, Any]: ...
    def get_context_data(
        self, **kwargs: Any
    ) -> dict[str, Any]: ...
    def _get_overdue_data_for_user(
        self, context: dict[str, Any]
    ) -> dict[str, Any]: ...

class TotalOverdueObligationsView(LoginRequiredMixin, View):
    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> JsonResponse: ...

class ObligationCreateView(LoginRequiredMixin, CreateView):
    model: type[Obligation]
    form_class: type[ObligationForm]
    template_name: str
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_context_data(
        self, **kwargs: Any
    ) -> dict[str, Any]: ...
    def form_valid(
        self, form: ObligationForm
    ) -> HttpResponse: ...
    def form_invalid(
        self, form: ObligationForm
    ) -> HttpResponse: ...

class ObligationDetailView(LoginRequiredMixin, DetailView):
    model: type[Obligation]
    template_name: str
    context_object_name: str
    pk_url_kwarg: str
    object: Obligation
    def __init__(
        self, *args: Any, **kwargs: Any
    ) -> None: ...
    def get_context_data(
        self, **kwargs: Any
    ) -> dict[str, Any]: ...
    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...
    def post(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...

class ObligationUpdateView(LoginRequiredMixin, UpdateView):
    model: type[Obligation]
    form_class: type[ObligationForm]
    template_name: str
    slug_field: str
    slug_url_kwarg: str
    object: Obligation
    def __init__(
        self, *args: Any, **kwargs: Any
    ) -> None: ...
    def get_template_names(self) -> list[str]: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_context_data(
        self, **kwargs: Any
    ) -> dict[str, Any]: ...
    def _update_mechanism_counts(
        self,
        old_mechanism: EnvironmentalMechanism | None,
        updated_obligation: Obligation,
    ) -> None: ...
    def form_valid(
        self, form: ObligationForm
    ) -> HttpResponse: ...
    def form_invalid(
        self, form: ObligationForm
    ) -> HttpResponse: ...

class ObligationDeleteView(LoginRequiredMixin, DeleteView):
    model: type[Obligation]
    pk_url_kwarg: str
    def post(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> JsonResponse: ...

class ToggleCustomAspectView(View):
    def get(
        self, request: HttpRequest
    ) -> HttpResponse: ...

class ObligationListView(LoginRequiredMixin, ListView):
    model: type[Obligation]
    template_name: str
    context_object_name: str
    def get_queryset(self) -> QuerySet[Obligation]: ...

def upload_evidence(
    request: HttpRequest, obligation_id: int
) -> HttpResponse: ...

class MarkObligationsCompleteAPI(View):
    def post(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> JsonResponse: ...

class DeleteObligationsAPI(View):
    def delete(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> JsonResponse: ...
