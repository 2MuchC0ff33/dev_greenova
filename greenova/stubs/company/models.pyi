from django.db import models

class Company(models.Model):
    name: str
    description: str | None
    website: str | None
    email: str | None
    phone: str | None
    address: str | None
    city: str | None
    state: str | None
    country: str | None
    postal_code: str | None
    created_at: models.DateTimeField
    updated_at: models.DateTimeField

    class Meta:
        verbose_name_plural: str = "Companies"

    def __str__(self) -> str: ...
