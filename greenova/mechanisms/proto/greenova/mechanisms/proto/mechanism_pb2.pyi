from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
STATUS_COMPLETED: ObligationStatus
STATUS_IN_PROGRESS: ObligationStatus
STATUS_NOT_STARTED: ObligationStatus
STATUS_OVERDUE: ObligationStatus
STATUS_UNKNOWN: ObligationStatus

class ChartData(_message.Message):
    __slots__ = ["mechanism_id", "mechanism_name", "segments"]
    MECHANISM_ID_FIELD_NUMBER: _ClassVar[int]
    MECHANISM_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    mechanism_id: int
    mechanism_name: str
    segments: _containers.RepeatedCompositeFieldContainer[ChartSegment]
    def __init__(
        self,
        segments: _Iterable[ChartSegment | _Mapping] | None = ...,
        mechanism_id: int | None = ...,
        mechanism_name: str | None = ...,
    ) -> None: ...

class ChartResponse(_message.Message):
    __slots__ = ["charts", "error"]
    CHARTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    charts: _containers.RepeatedCompositeFieldContainer[ChartData]
    error: str
    def __init__(
        self,
        charts: _Iterable[ChartData | _Mapping] | None = ...,
        error: str | None = ...,
    ) -> None: ...

class ChartSegment(_message.Message):
    __slots__ = ["color", "label", "value"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    color: str
    label: str
    value: int
    def __init__(
        self, label: str | None = ..., value: int | None = ..., color: str | None = ...
    ) -> None: ...

class ObligationInsight(_message.Message):
    __slots__ = ["close_out_date", "due_date", "obligation_number"]
    CLOSE_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    OBLIGATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    close_out_date: str
    due_date: str
    obligation_number: str
    def __init__(
        self,
        obligation_number: str | None = ...,
        due_date: str | None = ...,
        close_out_date: str | None = ...,
    ) -> None: ...

class ObligationInsightResponse(_message.Message):
    __slots__ = [
        "count",
        "error",
        "mechanism_id",
        "obligations",
        "status",
        "status_key",
        "total_count",
    ]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MECHANISM_ID_FIELD_NUMBER: _ClassVar[int]
    OBLIGATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_KEY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    error: str
    mechanism_id: int
    obligations: _containers.RepeatedCompositeFieldContainer[ObligationInsight]
    status: str
    status_key: str
    total_count: int
    def __init__(
        self,
        mechanism_id: int | None = ...,
        status: str | None = ...,
        status_key: str | None = ...,
        count: int | None = ...,
        total_count: int | None = ...,
        obligations: _Iterable[ObligationInsight | _Mapping] | None = ...,
        error: str | None = ...,
    ) -> None: ...

class ObligationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
