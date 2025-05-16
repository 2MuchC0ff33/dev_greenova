# Stub file for mechanisms.models

from typing import Any, TypeVar

from django.db import models
from projects.models import Project

T = TypeVar("T", bound="EnvironmentalMechanism")

class EnvironmentalMechanismManager(models.Manager["EnvironmentalMechanism"]):
    """Custom manager for EnvironmentalMechanism model."""

    def create(self, **kwargs: Any) -> EnvironmentalMechanism:
        """Create and return a new EnvironmentalMechanism instance.

        Args:
            **kwargs: Arbitrary keyword arguments for EnvironmentalMechanism fields.

        Returns:
            EnvironmentalMechanism: The created EnvironmentalMechanism instance.
        """
        ...

class EnvironmentalMechanism(models.Model):
    """EnvironmentalMechanism model."""

    # objects: EnvironmentalMechanismManager  # Provided by Django; do not annotate.
    name: str
    project: Project
    not_started_count: int
    in_progress_count: int
    completed_count: int
    overdue_count: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize an EnvironmentalMechanism instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        ...

def update_all_mechanism_counts() -> int:
    """Update all mechanism counts.

    Returns:
        The number of mechanisms updated.
    """
    ...
