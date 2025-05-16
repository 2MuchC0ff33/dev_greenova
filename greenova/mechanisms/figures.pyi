# Stub file for mechanisms.figures

from matplotlib.figure import Figure

# New Plotly functions
def generate_plotly_pie_chart(
    data: list[int],
    labels: list[str],
    colors: list[str],
    mechanism_id: int | None = None,
    chart_title: str | None = None,
) -> str: ...
def get_mechanism_plotly_chart(
    mechanism_id: int,
) -> str | None: ...
def get_overall_plotly_chart(
    project_id: int,
) -> str | None: ...

# Legacy matplotlib functions
def generate_pie_chart(
    data: list[int],
    labels: list[str],
    colors: list[str],
    mechanism_id: int | None = None,
    fig_width: int = ...,
    fig_height: int = ...,
) -> Figure: ...
def encode_figure_to_svg(fig: Figure) -> str: ...
def get_mechanism_chart(
    mechanism_id: int, fig_width: int = ..., fig_height: int = ...
) -> tuple[Figure, str]: ...
def get_overall_chart(
    project_id: int, fig_width: int = ..., fig_height: int = ...
) -> tuple[Figure, str]: ...
