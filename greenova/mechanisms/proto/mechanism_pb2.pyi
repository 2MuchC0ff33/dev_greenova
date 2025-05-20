"""Type stub for mechanism_pb2.py."""

from typing import Any

class ChartData:
    mechanism_id: int
    mechanism_name: str
    segments: list[Any]  # Replace Any with the specific segment type when known

    def __init__(self) -> None: ...

    class Segment:
        label: str
        value: int
        color: str

        def __init__(self) -> None: ...

class ChartResponse:
    charts: list[ChartData]
    error: str

    def __init__(self) -> None: ...

class ObligationInsightResponse:
    mechanism_id: int
    status: str
    status_key: str
    count: int
    total_count: int
    error: str
    obligations: list[Any]  # Replace Any with the specific type when known

    def __init__(self) -> None: ...

class ObligationStatus:
    STATUS_UNKNOWN: int
    STATUS_NOT_STARTED: int
    STATUS_IN_PROGRESS: int
    STATUS_COMPLETED: int
    STATUS_OVERDUE: int
