"""Pytest test cases for figures.py in mechanisms app."""

from beartype import beartype

from greenova.mechanisms import figures


@beartype
def test_generate_plotly_pie_chart_basic():
    data = [10, 20, 30]
    labels = ["Not Started", "In Progress", "Completed"]
    colors = ["#f9c74f", "#90be6d", "#43aa8b"]
    html = figures.generate_plotly_pie_chart(
        data, labels, colors, mechanism_id=1, chart_title="Test Chart"
    )
    assert isinstance(html, str)
    assert "plotly" in html or "<div" in html
    for label in labels:
        assert label in html


@beartype
def test_generate_plotly_pie_chart_empty():
    data = []
    labels = []
    colors = []
    html = figures.generate_plotly_pie_chart(data, labels, colors)
    assert isinstance(html, str)
    assert "plotly" in html or "<div" in html
