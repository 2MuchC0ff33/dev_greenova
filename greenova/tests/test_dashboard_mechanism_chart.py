"""Test that only one mechanism chart card is rendered per project selection on the dashboard root view.

This test ensures that duplicate environment mechanical analysis charts cards are not rendered
when a project is selected from the project selector tool.

Copyright 2025 Enveng Group.
SPDX-License-Identifier: AGPL-3.0-or-later
"""

from typing import Any

import pytest
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from mechanisms.models import EnvironmentalMechanism
from projects.models import Project

CHART_CARD_EXPECTED_COUNT = 2  # Mechanism + Procedures


@pytest.mark.django_db
def test_single_mechanism_chart_card(
    client: Any,
    regular_user: AbstractUser,
    project: Project,
    mechanism: EnvironmentalMechanism,
) -> None:
    """Test that only one mechanism chart card is rendered per project selection."""
    client.force_login(regular_user)
    url = reverse("dashboard:home") + f"?project_id={getattr(project, 'id', 1)}"
    response = client.get(url, HTTP_HX_REQUEST="true")
    html = response.content.decode("utf-8")
    # There should be only one mechanism chart container
    assert html.count('id="mechanism-data-container"') == 1
    # There should not be multiple chart cards for the same project
    assert html.count('class="card chart-container"') == CHART_CARD_EXPECTED_COUNT
    # Ensure no duplicate chart galleries
    assert html.count("chart-gallery") <= 1
