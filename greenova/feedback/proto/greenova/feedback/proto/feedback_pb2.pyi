from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class BugReportCollection(_message.Message):
    __slots__ = ["reports"]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[BugReportProto]
    def __init__(
        self, reports: _Iterable[BugReportProto | _Mapping] | None = ...
    ) -> None: ...

class BugReportProto(_message.Message):
    __slots__ = [
        "actual_behavior",
        "additional_comments",
        "admin_comment",
        "admin_severity",
        "application_version",
        "browser",
        "created_at",
        "description",
        "device_type",
        "error_messages",
        "expected_behavior",
        "frequency",
        "github_issue_url",
        "id",
        "impact_severity",
        "operating_system",
        "status",
        "steps_to_reproduce",
        "title",
        "trace_report",
        "updated_at",
        "user_id",
        "user_impact",
        "username",
        "workarounds",
    ]
    class Frequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACTUAL_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_COMMENT_FIELD_NUMBER: _ClassVar[int]
    ADMIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    BROWSER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_ALWAYS: BugReportProto.Frequency
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FREQUENTLY: BugReportProto.Frequency
    FREQUENCY_OCCASIONALLY: BugReportProto.Frequency
    FREQUENCY_RARELY: BugReportProto.Frequency
    FREQUENCY_UNKNOWN_UNSPECIFIED: BugReportProto.Frequency
    GITHUB_ISSUE_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMPACT_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_CRITICAL: BugReportProto.Severity
    SEVERITY_HIGH: BugReportProto.Severity
    SEVERITY_LOW: BugReportProto.Severity
    SEVERITY_MEDIUM: BugReportProto.Severity
    SEVERITY_UNDEFINED_UNSPECIFIED: BugReportProto.Severity
    STATUS_CLOSED: BugReportProto.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_IN_PROGRESS: BugReportProto.Status
    STATUS_OPEN: BugReportProto.Status
    STATUS_REJECTED: BugReportProto.Status
    STATUS_RESOLVED: BugReportProto.Status
    STATUS_UNSPECIFIED: BugReportProto.Status
    STEPS_TO_REPRODUCE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TRACE_REPORT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IMPACT_FIELD_NUMBER: _ClassVar[int]
    WORKAROUNDS_FIELD_NUMBER: _ClassVar[int]
    actual_behavior: str
    additional_comments: str
    admin_comment: str
    admin_severity: BugReportProto.Severity
    application_version: str
    browser: str
    created_at: int
    description: str
    device_type: str
    error_messages: str
    expected_behavior: str
    frequency: BugReportProto.Frequency
    github_issue_url: str
    id: int
    impact_severity: BugReportProto.Severity
    operating_system: str
    status: BugReportProto.Status
    steps_to_reproduce: str
    title: str
    trace_report: str
    updated_at: int
    user_id: int
    user_impact: str
    username: str
    workarounds: str
    def __init__(
        self,
        id: int | None = ...,
        title: str | None = ...,
        description: str | None = ...,
        application_version: str | None = ...,
        operating_system: str | None = ...,
        browser: str | None = ...,
        device_type: str | None = ...,
        steps_to_reproduce: str | None = ...,
        expected_behavior: str | None = ...,
        actual_behavior: str | None = ...,
        error_messages: str | None = ...,
        trace_report: str | None = ...,
        frequency: BugReportProto.Frequency | str | None = ...,
        impact_severity: BugReportProto.Severity | str | None = ...,
        admin_severity: BugReportProto.Severity | str | None = ...,
        user_impact: str | None = ...,
        workarounds: str | None = ...,
        additional_comments: str | None = ...,
        user_id: int | None = ...,
        username: str | None = ...,
        created_at: int | None = ...,
        updated_at: int | None = ...,
        github_issue_url: str | None = ...,
        status: BugReportProto.Status | str | None = ...,
        admin_comment: str | None = ...,
    ) -> None: ...
