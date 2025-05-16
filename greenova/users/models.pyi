from collections.abc import Mapping
from typing import Any, TypeVar

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

T = TypeVar("T", bound="Profile")

class ProfileManager(models.Manager["Profile"]):
    def get_or_create(
        self, defaults: Mapping[str, Any] | None = ..., **kwargs: Any
    ) -> tuple[Profile, bool]: ...

class Profile(models.Model):
    # objects: ProfileManager  # Provided by Django; do not annotate.
    user: AbstractBaseUser

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
