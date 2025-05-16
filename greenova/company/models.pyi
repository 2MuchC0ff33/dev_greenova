# Stub file for company.models

from datetime import datetime
from typing import Any, TypeVar

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Manager, QuerySet

T = TypeVar("T", bound="Company")

class CompanyManager(models.Manager["Company"]):
    """Custom manager for Company model."""

    def create(self, **kwargs: Any) -> Company:
        """Create and return a new Company instance.

        Args:
            **kwargs: Arbitrary keyword arguments for Company fields.

        Returns:
            Company: The created Company instance.
        """
        ...

class Company(models.Model):
    """Company model."""

    # objects: CompanyManager  # Do not annotate to avoid mypy error; Django provides this.
    name: str
    logo: str | None
    description: str
    website: str
    phone: str
    email: str
    address: str | None
    company_type: str
    size: str
    industry: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    users: Manager[User]

    COMPANY_TYPES: list[tuple[str, str]]
    COMPANY_SIZES: list[tuple[str, str]]
    INDUSTRY_SECTORS: list[tuple[str, str]]

    def __str__(self) -> str:
        """Return string representation of the company."""
        ...

    def get_member_count(self) -> int:
        """Return the number of members in the company."""
        ...

    def get_active_projects_count(self) -> int:
        """Return the number of active projects for the company."""
        ...

    def get_members_by_role(self, role: str) -> QuerySet[User]:
        """Return members filtered by role.

        Args:
            role: The role to filter members by.

        Returns:
            QuerySet: Members with the specified role.
        """
        ...

    def add_member(self, user: User, role: str = "member") -> None:
        """Add a member to the company.

        Args:
            user: The user to add.
            role: The role to assign.
        """
        ...

    def remove_member(self, user: User) -> None:
        """Remove a member from the company.

        Args:
            user: The user to remove.
        """
        ...

    def clean(self) -> None:
        """Clean and validate the company instance."""
        ...

    @staticmethod
    def get_default_company() -> int:
        """Return the default company ID.

        Returns:
            int: The default company ID.
        """
        ...

class CompanyMembership(models.Model):
    """Company membership model."""

    company: Company
    user: User
    role: str
    department: str
    position: str
    date_joined: datetime
    is_primary: bool

    ROLE_CHOICES: list[tuple[str, str]]

    def __str__(self) -> str:
        """Return string representation of the membership."""
        ...

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Save the membership instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        ...

    def clean(self) -> None:
        """Clean and validate the membership instance."""
        ...

class CompanyDocument(models.Model):
    """Company document model."""

    company: Company
    name: str
    description: str
    file: str
    document_type: str
    uploaded_by: User | None
    uploaded_at: datetime

    def __str__(self) -> str:
        """Return string representation of the document."""
        ...

class Obligation(models.Model):
    """Obligation model."""

    company: Company
    name: str
    description: str
    due_date: datetime
    status: str
    created_at: datetime
    updated_at: datetime

    def __str__(self) -> str:
        """Return string representation of the obligation."""
        ...
