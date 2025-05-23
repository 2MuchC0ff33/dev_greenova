# Type stub file for obligations.models
# This stub supports both "obligations.models" and "greenova.obligations.models" imports

from typing import Any, ClassVar

from django.db.models import Manager, Model

class ObligationManager(Manager['Obligation']):
    pass

class Obligation(Model):
    objects: ClassVar[ObligationManager]
    obligation_number: str
    status: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
