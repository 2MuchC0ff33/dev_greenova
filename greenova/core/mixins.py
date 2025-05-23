from typing import Any, TypeVar

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin

# Define a type variable for views with context data
ContextView = TypeVar("ContextView", bound=ContextMixin)


class BreadcrumbMixin(ContextMixin):
    """
    Add breadcrumb data to template context.

    Usage:
        class MyView(BreadcrumbMixin, TemplateView):
            breadcrumbs = [
                ('Home', 'home'),
                ('Dashboard', 'dashboard:home'),
                ('Current Page', None),  # None for current page with no link
            ]
    """

    breadcrumbs: list[tuple[str, str | None]] = []

    def get_breadcrumbs(self) -> list[tuple[str, str | None]]:
        """Get breadcrumbs for this view."""
        return self.breadcrumbs

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = self.get_breadcrumbs()
        return context


class PageTitleMixin(ContextMixin):
    """
    Add page title to template context.

    Usage:
        class MyView(PageTitleMixin, TemplateView):
            page_title = "My Page Title"
    """

    page_title: str | None = None

    def get_page_title(self) -> str | None:
        """Get page title for this view."""
        return self.page_title

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title()
        return context


class SectionMixin(ContextMixin):
    """
    Add current section to template context for highlighting navigation.

    Usage:
        class MyView(SectionMixin, TemplateView):
            active_section = "dashboard"
    """

    active_section: str | None = None

    def get_active_section(self) -> str | None:
        """Get active section for this view."""
        return self.active_section

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active_section"] = self.get_active_section()
        return context


class ViewMixin(BreadcrumbMixin, PageTitleMixin, SectionMixin):
    """
    Combined mixin for standard view context data.

    Usage:
        class MyView(ViewMixin, TemplateView):
            page_title = "Dashboard"
            active_section = "dashboard"
            breadcrumbs = [('Home', 'home'), ('Dashboard', None)]
    """


class AuthViewMixin(LoginRequiredMixin, ViewMixin):
    """
    Combined mixin for authenticated views.

    Usage:
        class MyView(AuthViewMixin, TemplateView):
            page_title = "Dashboard"
            active_section = "dashboard"
            breadcrumbs = [('Home', 'home'), ('Dashboard', None)]
    """
