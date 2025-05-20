"""Type stubs for proto_utils.py."""

from collections.abc import Sequence
from dataclasses import dataclass

from django.db.models import QuerySet
from obligations.models import Obligation

from ...mechanisms.models import EnvironmentalMechanism
from ...mechanisms.proto.mechanism_pb2 import (
    ChartData,
    ChartResponse,
    ObligationInsightResponse,
    ObligationStatus,
)

@dataclass
class ObligationInsightParams:
    mechanism_id: int
    status: str
    status_key: str
    obligations: Sequence[Obligation]
    total_count: int
    error: str | None = None

def serialize_obligation_insights(
    params: ObligationInsightParams,
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
