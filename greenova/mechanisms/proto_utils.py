"""Protobuf utilities for mechanism data.

This module provides utility functions for serializing and deserializing data
between Django models and Protocol Buffers for the mechanisms app.
"""

import logging
from collections.abc import Sequence

from django.db.models import QuerySet
from obligations.models import Obligation

from .models import EnvironmentalMechanism
from .proto.mechanism_pb2 import (  # type: ignore
    ChartData,
    ChartResponse,
    ObligationInsightResponse,
    ObligationStatus,
)

logger = logging.getLogger(__name__)


def serialize_obligation_insights(
    mechanism_id: int,
    status: str,
    status_key: str,
    obligations: Sequence[Obligation],
    total_count: int,
    error: str | None = None,
) -> ObligationInsightResponse:
    """Serialize obligation data to protobuf for chart tooltips.

    Args:
        mechanism_id: ID of the mechanism
        status: Status label (e.g., "Not Started")
        status_key: Status key (e.g., "not_started")
        obligations: Sequence of Obligation objects
        total_count: Total count of matching obligations
        error: Optional error message

    Returns:
        ObligationInsightResponse protobuf message
    """
    response = ObligationInsightResponse()
    response.mechanism_id = mechanism_id
    response.status = status
    response.status_key = status_key
    response.count = len(obligations)
    response.total_count = total_count

    if error:
        response.error = error
        return response

    for obligation in obligations:
        insight = response.obligations.add()
        insight.obligation_number = obligation.obligation_number

        if obligation.action_due_date:
            insight.due_date = obligation.action_due_date.strftime("%Y-%m-%d")

        if obligation.close_out_date:
            insight.close_out_date = obligation.close_out_date.strftime("%Y-%m-%d")

    return response


def serialize_mechanism_chart_data(
    mechanism: EnvironmentalMechanism,
) -> ChartData:
    """Serialize mechanism data to protobuf for chart rendering.

    Args:
        mechanism: EnvironmentalMechanism object

    Returns:
        ChartData protobuf message
    """
    chart_data = ChartData()
    chart_data.mechanism_id = mechanism.id
    chart_data.mechanism_name = mechanism.name

    # Create chart segments for each status
    statuses = ["Not Started", "In Progress", "Completed", "Overdue"]
    values = [
        mechanism.not_started_count,
        mechanism.in_progress_count,
        mechanism.completed_count,
        mechanism.overdue_count,
    ]
    colors = ["#f9c74f", "#90be6d", "#43aa8b", "#f94144"]

    for i, (status, value, color) in enumerate(zip(statuses, values, colors)):
        segment = chart_data.segments.add()
        segment.label = status
        segment.value = value
        segment.color = color

    return chart_data


def serialize_overall_chart_data(
    project_id: int,
    mechanisms: QuerySet[EnvironmentalMechanism],
) -> ChartData:
    """Serialize overall project data to protobuf for chart rendering.

    Args:
        project_id: ID of the project
        mechanisms: QuerySet of EnvironmentalMechanism objects

    Returns:
        ChartData protobuf message
    """
    chart_data = ChartData()
    chart_data.mechanism_id = 0  # 0 indicates overall chart
    chart_data.mechanism_name = "Overall Status"

    # Aggregate data
    not_started = sum(m.not_started_count for m in mechanisms)
    in_progress = sum(m.in_progress_count for m in mechanisms)
    completed = sum(m.completed_count for m in mechanisms)
    overdue = sum(m.overdue_count for m in mechanisms)

    statuses = ["Not Started", "In Progress", "Completed", "Overdue"]
    values = [not_started, in_progress, completed, overdue]
    colors = ["#f9c74f", "#90be6d", "#43aa8b", "#f94144"]

    for i, (status, value, color) in enumerate(zip(statuses, values, colors)):
        segment = chart_data.segments.add()
        segment.label = status
        segment.value = value
        segment.color = color

    return chart_data


def serialize_chart_response(
    charts: list[ChartData],
    error: str | None = None,
) -> ChartResponse:
    """Serialize chart data to protobuf response.

    Args:
        charts: List of ChartData messages
        error: Optional error message

    Returns:
        ChartResponse protobuf message
    """
    response = ChartResponse()

    if error:
        response.error = error
        return response

    for chart in charts:
        response.charts.append(chart)

    return response


def status_string_to_enum(status: str) -> ObligationStatus:
    """Convert status string to ObligationStatus enum value.

    Args:
        status: Status string (e.g., "not_started")

    Returns:
        ObligationStatus enum value
    """
    status_map = {
        "not_started": ObligationStatus.STATUS_NOT_STARTED,
        "in_progress": ObligationStatus.STATUS_IN_PROGRESS,
        "completed": ObligationStatus.STATUS_COMPLETED,
        "overdue": ObligationStatus.STATUS_OVERDUE,
    }

    return status_map.get(status.lower(), ObligationStatus.STATUS_UNKNOWN)


def status_enum_to_string(status: ObligationStatus) -> str:
    """Convert ObligationStatus enum value to status string.

    Args:
        status: ObligationStatus enum value

    Returns:
        Status string (e.g., "not_started")
    """
    status_map = {
        ObligationStatus.STATUS_NOT_STARTED: "not_started",
        ObligationStatus.STATUS_IN_PROGRESS: "in_progress",
        ObligationStatus.STATUS_COMPLETED: "completed",
        ObligationStatus.STATUS_OVERDUE: "overdue",
    }

    return status_map.get(status, "unknown")
