"""Mechanism chart generation using plotly for interactive charts.

This module provides functions to generate interactive pie charts for environmental
mechanisms using plotly, for integration into the Greenova dashboard.
"""

import io
import logging

import matplotlib
import matplotlib.figure
import plotly.graph_objects as go
from beartype import beartype
from plotly.offline import plot

from . import proto_utils
from .models import EnvironmentalMechanism

# For type annotations
Figure = matplotlib.figure.Figure

logger = logging.getLogger(__name__)


@beartype
def generate_plotly_pie_chart(
    data: list[int],
    labels: list[str],
    colors: list[str],
    mechanism_id: int | None = None,
    chart_title: str | None = None,
) -> str:
    """Generate a plotly pie chart for given data and labels.

    Args:
        data: List of values for the pie chart.
        labels: List of labels for each segment.
        colors: List of colors for each segment.
        mechanism_id: Optional mechanism ID to associate with the chart.
        chart_title: Optional title for the chart.

    Returns:
        HTML string containing the interactive plotly chart.
    """
    # Create figure with custom data attributes
    fig = go.Figure()

    # Create custom data array for hover info
    custom_data = []
    for i, label in enumerate(labels):
        custom_data.append(
            {"status": label, "count": data[i], "mechanism_id": mechanism_id}
        )

    # Add pie chart
    fig.add_trace(
        go.Pie(
            labels=labels,
            values=data,
            marker=dict(colors=colors),
            textinfo="percent",
            hoverinfo="label+percent+value",
            textfont=dict(size=14, color="white"),
            customdata=custom_data,
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Count: %{value}<br>"
                "Percentage: %{percent:.1%}<br>"
                "<extra></extra>"
            ),
        )
    )

    # Update layout
    fig.update_layout(
        title=chart_title,
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.1,
            xanchor="center",
            x=0.5,
        ),
        autosize=True,
        height=320,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    # Add data attributes for interactivity
    for i, label in enumerate(labels):
        status_key = label.lower().replace(" ", "_")
        fig.data[0].customdata[i].update({"status_key": status_key, "color": colors[i]})

    # Convert to HTML with only supported arguments for plotly version
    return plot(fig, output_type="div", include_plotlyjs=False)


def encode_figure_to_svg(fig: Figure) -> str:
    """Convert a matplotlib figure to an SVG string with data attributes.

    Extracts data attributes from figure elements and adds them to the SVG output
    to enable interactive features.

    Args:
        fig: Matplotlib Figure object.

    Returns:
        SVG image as a string with data attributes preserved for interactivity.
    """
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    svg_data = buf.getvalue()
    buf.close()

    # Extract data attributes from wedges and add them to the SVG
    svg_modified = svg_data

    # Find all wedge elements with gid attributes
    for wedge in fig.gca().patches:
        if hasattr(wedge, "get_gid") and wedge.get_gid():
            gid = wedge.get_gid()

            # Check for the data attributes we added to wedges
            data_attrs = {}
            if hasattr(wedge, "_data_status"):
                data_attrs["data-status"] = wedge._data_status
            if hasattr(wedge, "_data_count"):
                data_attrs["data-count"] = str(wedge._data_count)
            if hasattr(wedge, "_data_mechanism_id"):
                data_attrs["data-mechanism-id"] = wedge._data_mechanism_id
            if hasattr(wedge, "_data_status_key"):
                data_attrs["data-status-key"] = wedge._data_status_key
            if hasattr(wedge, "_data_color"):
                data_attrs["data-color"] = wedge._data_color

            # Add the attributes to the SVG
            if data_attrs:
                # Create attribute string
                attrs_str = " ".join([f'{k}="{v}"' for k, v in data_attrs.items()])

                # Find the SVG element with this gid and add the attributes
                pattern = f'id="{gid}"'
                replacement = f'id="{gid}" {attrs_str}'
                svg_modified = svg_modified.replace(pattern, replacement)

    return svg_modified


def get_mechanism_chart(
    mechanism_id: int, fig_width: int = 320, fig_height: int = 280
) -> tuple[Figure, str]:
    """Get pie chart for a specific mechanism as SVG.

    Args:
        mechanism_id: The ID of the mechanism.
        fig_width: Width of the figure in pixels.
        fig_height: Height of the figure in pixels.

    Returns:
        Tuple of (matplotlib Figure, SVG image as string).
    """
    try:
        mechanism = EnvironmentalMechanism.objects.get(id=mechanism_id)
        labels = ["Not Started", "In Progress", "Completed", "Overdue"]
        data = [
            mechanism.not_started_count,
            mechanism.in_progress_count,
            mechanism.completed_count,
            mechanism.overdue_count,
        ]
        colors = ["#f9c74f", "#90be6d", "#43aa8b", "#f94144"]

        fig = generate_pie_chart(
            data, labels, colors, mechanism_id, fig_width, fig_height
        )
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image
    except EnvironmentalMechanism.DoesNotExist:
        logger.error("Mechanism with ID %s does not exist.", mechanism_id)
        fig = generate_pie_chart(
            [0, 0, 0, 0],
            ["None", "None", "None", "None"],
            ["#ccc", "#ccc", "#ccc", "#ccc"],
            None,
            fig_width,
            fig_height,
        )
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image


def get_overall_chart(
    project_id: int, fig_width: int = 320, fig_height: int = 280
) -> tuple[Figure, str]:
    """Get overall pie chart for all mechanisms in a project as SVG.

    Returns both the figure and SVG image data.

    Args:
        project_id: The ID of the project.
        fig_width: Width of the figure in pixels.
        fig_height: Height of the figure in pixels.

    Returns:
        Tuple of (matplotlib Figure, SVG image as string).
    """
    try:
        mechanisms = EnvironmentalMechanism.objects.filter(project_id=project_id)

        # Aggregate data
        not_started = sum(m.not_started_count for m in mechanisms)
        in_progress = sum(m.in_progress_count for m in mechanisms)
        completed = sum(m.completed_count for m in mechanisms)
        overdue = sum(m.overdue_count for m in mechanisms)

        labels = ["Not Started", "In Progress", "Completed", "Overdue"]
        data = [not_started, in_progress, completed, overdue]
        colors = ["#f9c74f", "#90be6d", "#43aa8b", "#f94144"]

        # Pass None for mechanism_id as this is an aggregated chart
        fig = generate_pie_chart(data, labels, colors, None, fig_width, fig_height)
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image
    except Exception as e:
        logger.error("Error generating overall chart: %s", str(e))
        fig = generate_pie_chart(
            [0, 0, 0, 0],
            ["None", "None", "None", "None"],
            ["#ccc", "#ccc", "#ccc", "#ccc"],
            None,
            fig_width,
            fig_height,
        )
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image


@beartype
def get_mechanism_plotly_chart(
    mechanism_id: int,
) -> str | None:
    """Plotly pie chart for a specific mechanism (protobuf serialization)."""
    try:
        mechanism = EnvironmentalMechanism.objects.get(id=mechanism_id)
        chart_data_pb = proto_utils.serialize_mechanism_chart_data(mechanism)
        # Type hint for mypy and linters
        from typing import Any, cast

        segments = cast(list[Any], getattr(chart_data_pb, "segments", []))
        labels: list[str] = [str(getattr(segment, "label", "")) for segment in segments]
        data: list[int] = [int(getattr(segment, "value", 0)) for segment in segments]
        colors: list[str] = [str(getattr(segment, "color", "")) for segment in segments]
        return generate_plotly_pie_chart(
            data, labels, colors, mechanism_id, mechanism.name
        )
    except EnvironmentalMechanism.DoesNotExist:
        logger.error("Mechanism with ID %s does not exist.", mechanism_id)
        return None


@beartype
def get_overall_plotly_chart(
    project_id: int,
) -> str | None:
    """Plotly pie chart for all mechanisms in a project (protobuf serialization)."""
    try:
        mechanisms = EnvironmentalMechanism.objects.filter(project_id=project_id)
        chart_data_pb = proto_utils.serialize_overall_chart_data(project_id, mechanisms)
        labels = [segment.label for segment in chart_data_pb.segments]
        data = [segment.value for segment in chart_data_pb.segments]
        colors = [segment.color for segment in chart_data_pb.segments]
        return generate_plotly_pie_chart(data, labels, colors, None, "Overall Status")
    except Exception as e:
        logger.error("Error generating overall chart: %s", str(e))
        return None


@beartype
def generate_pie_chart(
    data: list[int],
    labels: list[str],
    colors: list[str],
    mechanism_id: int | None = None,
    fig_width: int = 320,
    fig_height: int = 280,
) -> Figure:
    """Generate a static matplotlib pie chart for mechanism status.

    Args:
        data: List of values for the pie chart.
        labels: List of labels for each segment.
        colors: List of colors for each segment.
        mechanism_id: Optional mechanism ID for context (unused in chart).
        fig_width: Width of the figure in pixels.
        fig_height: Height of the figure in pixels.

    Returns:
        Matplotlib Figure object containing the pie chart.
    """
    fig = matplotlib.figure.Figure(figsize=(fig_width / 100, fig_height / 100), dpi=100)
    ax = fig.add_subplot(111)
    if data and any(data):
        wedges, _ = ax.pie(
            data,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={"edgecolor": "w", "linewidth": 1},
            textprops={"fontsize": 10},
        )
        ax.axis("equal")
        ax.set_title("Status Distribution", fontsize=12)
        # Optionally add data attributes for interactivity (if needed)
        for i, wedge in enumerate(wedges):
            wedge.set_gid(f"wedge_{i}")
            wedge._data_status = labels[i] if i < len(labels) else ""
            wedge._data_count = data[i] if i < len(data) else 0
            wedge._data_mechanism_id = mechanism_id if mechanism_id is not None else ""
            wedge._data_status_key = (
                labels[i].lower().replace(" ", "_") if i < len(labels) else ""
            )
            wedge._data_color = colors[i] if i < len(colors) else ""
    else:
        ax.text(
            0.5,
            0.5,
            "No data available",
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
        )
        ax.axis("off")
    fig.tight_layout()
    return fig
