from collections.abc import Callable
from typing import Any

def hyperscript_tags() -> str: ...
def _() -> Callable[[str], str]: ...
def add_class() -> Callable[[str, str], str]: ...
def remove_class() -> Callable[[str, str], str]: ...
def toggle_class() -> Callable[[str, str], str]: ...
def take_class() -> Callable[[str, str], str]: ...
def settle() -> str: ...
def wait() -> str: ...
def hyperscript() -> dict[str, Any]: ...
