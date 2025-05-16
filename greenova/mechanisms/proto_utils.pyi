# Stub file for mechanisms.proto_utils
from collections.abc import Sequence

from django.db.models import QuerySet
from obligations.models import Obligation

from .models import EnvironmentalMechanism
from .proto.mechanism_pb2 import (
    ChartData,
    ChartResponse,
    ObligationInsightResponse,
    ObligationStatus,
)

def serialize_obligation_insights(
    mechanism_id: int,
    status: str,
    status_key: str,
    obligations: Sequence[Obligation],
    total_count: int,
    error: str | None = None,
) -> ObligationInsightResponse: ...
def serialize_mechanism_chart_data(
    mechanism: EnvironmentalMechanism,
) -> ChartData: ...
def serialize_overall_chart_data(
    project_id: int,
    mechanisms: QuerySet[EnvironmentalMechanism],
) -> ChartData: ...
def serialize_chart_response(
    charts: list[ChartData],
    error: str | None = None,
) -> ChartResponse: ...
def status_string_to_enum(status: str) -> ObligationStatus: ...
def status_enum_to_string(status: ObligationStatus) -> str: ...
