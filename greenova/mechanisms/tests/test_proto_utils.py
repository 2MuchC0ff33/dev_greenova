"""Pytest test cases for proto_utils.py in mechanisms app."""

from datetime import date

import pytest

from greenova.mechanisms import proto_utils
from greenova.mechanisms.models import EnvironmentalMechanism


class DummyObligation:
    def __init__(self, number, due=None, close=None):
        self.obligation_number = number
        self.action_due_date = due
        self.close_out_date = close


@pytest.mark.django_db
def test_serialize_obligation_insights_basic():
    obligations = [
        DummyObligation("OBL001", date(2024, 1, 1), date(2024, 2, 1)),
        DummyObligation("OBL002", date(2024, 3, 1), None),
    ]
    resp = proto_utils.serialize_obligation_insights(
        mechanism_id=1,
        status="Not Started",
        status_key="not_started",
        obligations=obligations,
        total_count=2,
    )
    assert resp.mechanism_id == 1
    assert resp.status == "Not Started"
    assert resp.status_key == "not_started"
    assert resp.count == 2
    assert resp.total_count == 2
    assert resp.obligations[0].obligation_number == "OBL001"
    assert resp.obligations[0].due_date == "2024-01-01"
    assert resp.obligations[0].close_out_date == "2024-02-01"
    assert resp.obligations[1].obligation_number == "OBL002"
    assert resp.obligations[1].due_date == "2024-03-01"
    assert resp.obligations[1].close_out_date == ""


@pytest.mark.django_db
def test_serialize_obligation_insights_error():
    resp = proto_utils.serialize_obligation_insights(
        mechanism_id=2,
        status="Completed",
        status_key="completed",
        obligations=[],
        total_count=0,
        error="Some error occurred",
    )
    assert resp.error == "Some error occurred"
    assert resp.count == 0


@pytest.mark.django_db
def test_serialize_mechanism_chart_data():
    mech = EnvironmentalMechanism(
        id=1,
        name="Test Mechanism",
        not_started_count=1,
        in_progress_count=2,
        completed_count=3,
        overdue_count=4,
    )
    chart_data = proto_utils.serialize_mechanism_chart_data(mech)
    assert chart_data.mechanism_id == 1
    assert chart_data.mechanism_name == "Test Mechanism"
    assert len(chart_data.segments) == 4
    assert chart_data.segments[0].label == "Not Started"
    assert chart_data.segments[0].value == 1
    assert chart_data.segments[3].label == "Overdue"
    assert chart_data.segments[3].value == 4
