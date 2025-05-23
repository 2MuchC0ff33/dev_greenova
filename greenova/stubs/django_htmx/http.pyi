from typing import Any

def push_url(url: str) -> Any: ...
def redirect(url: str) -> Any: ...
def trigger_event(event_name: str, params: dict[str, Any] | None = None) -> Any: ...
def reload(
    template_name: str | None = None, context: dict[str, Any] | None = None
) -> Any: ...
