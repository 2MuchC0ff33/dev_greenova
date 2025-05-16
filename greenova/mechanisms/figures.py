"""Mechanism chart generation using matplotlib for SVG output.

This module provides functions to generate pie charts for environmental
mechanisms using matplotlib, exporting them as SVG for integration into the
Greenova dashboard.
"""

import io
import logging

import matplotlib.pyplot as plt
from beartype import beartype
from matplotlib.figure import Figure

from .models import EnvironmentalMechanism

logger = logging.getLogger(__name__)


@beartype  # type: ignore[misc]
def generate_pie_chart(
    data: list[int],
    labels: list[str],
    colors: list[str],
    fig_width: int = 400,  # Adjusted to better fit containers
    fig_height: int = 320,  # Adjusted height for better aspect ratio
) -> Figure:
    """Generate a pie chart for given data and labels with a legend.

    Args:
        data: List of values for the pie chart.
        labels: List of labels for each segment.
        colors: List of colors for each segment.
        fig_width: Width of the figure in pixels.
        fig_height: Height of the figure in pixels.

    Returns:
        Matplotlib Figure object.
    """
    # Calculate figure size in inches with better scaling factor
    fig = plt.figure(figsize=(fig_width / 100, fig_height / 100), dpi=100)

    # Create the subplot with proper space for the legend below
    plt.subplots_adjust(bottom=0.15, top=0.9)

    ax = fig.add_subplot(1, 1, 1)
    wedges, _, autotexts = ax.pie(
        data,
        labels=None,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white"},
        textprops={"fontsize": 10, "weight": "bold"},
        pctdistance=0.75,
        radius=0.8,  # Slightly smaller pie to fit better
    )

    # Set text colors to black and ensure consistent font size
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")  # Changed from set_weight to set_fontweight
        autotext.set_color("black")

    ax.axis("equal")

    # Place legend below the chart with 2 columns (2 items per row)
    # Adjust legend position to ensure it fits within the container
    ax.legend(
        wedges,
        labels,
        title="Status",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.05),
        fontsize=9,
        title_fontsize=10,
        frameon=False,
        ncol=2,  # Fixed at 2 columns for the desired layout
        borderaxespad=0.0,
        labelspacing=0.2,
        handlelength=1.0,
        handletextpad=0.4,
        columnspacing=1.0,
    )

    # Use tight_layout with adjusted parameters to ensure proper fit
    fig.tight_layout(pad=0.8, rect=(0, 0, 1, 0.95))  # Changed list to tuple
    return fig


def encode_figure_to_svg(fig: Figure) -> str:
    """Convert a matplotlib figure to an SVG string.

    Args:
        fig: Matplotlib Figure object.

    Returns:
        SVG image as a string.
    """
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    svg_data = buf.getvalue()
    buf.close()
    return svg_data


def get_mechanism_chart(
    mechanism_id: int, fig_width: int = 320, fig_height: int = 280
) -> tuple[Figure, str]:
    """Get pie chart for a specific mechanism as SVG.

    Returns both the figure and SVG image data.

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

        fig = generate_pie_chart(data, labels, colors, fig_width, fig_height)
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image
    except EnvironmentalMechanism.DoesNotExist:
        logger.error("Mechanism with ID %s does not exist.", mechanism_id)
        fig = generate_pie_chart(
            [0, 0, 0, 0],
            ["None", "None", "None", "None"],
            ["#ccc", "#ccc", "#ccc", "#ccc"],
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

        fig = generate_pie_chart(data, labels, colors, fig_width, fig_height)
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image
    except Exception as e:
        logger.error("Error generating overall chart: %s", str(e))
        fig = generate_pie_chart(
            [0, 0, 0, 0],
            ["None", "None", "None", "None"],
            ["#ccc", "#ccc", "#ccc", "#ccc"],
            fig_width,
            fig_height,
        )
        svg_image = encode_figure_to_svg(fig)
        return fig, svg_image
