"""
Stub file for obligations.api_views.

This module provides type stubs for the API views related to obligations management.
"""

import logging
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.views import View

logger: logging.Logger


class MarkObligationsCompleteAPI(View):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...


class DeleteObligationsAPI(View):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def delete(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> JsonResponse: ...
