# Stub file for projects.models

from typing import Any, TypeVar

from django.db import models

T = TypeVar("T", bound="Project")

class ProjectManager(models.Manager["Project"]):
    """Custom manager for Project model."""

    def create(self, **kwargs: Any) -> Project:
        """Create and return a new Project instance.

        Args:
            **kwargs: Arbitrary keyword arguments for Project fields.

        Returns:
            Project: The created Project instance.
        """
        ...

class Project(models.Model):
    """Project model."""

    # objects: ProjectManager  # Provided by Django; do not annotate.
    name: str

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize a Project instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        ...
