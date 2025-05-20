from dataclasses import dataclass

import matplotlib.figure
from _typeshed import Incomplete

from ...mechanisms import proto_utils as proto_utils
from ...mechanisms.models import EnvironmentalMechanism as EnvironmentalMechanism

Figure = matplotlib.figure.Figure
logger: Incomplete

def generate_plotly_pie_chart(
    data: list[int],
    labels: list[str],
    colors: list[str],
    mechanism_id: int | None = None,
    chart_title: str | None = None,
) -> str: ...
def encode_figure_to_svg(fig: Figure) -> str: ...
@dataclass
class PieChartParams:
    data: list[int]
    labels: list[str]
    colors: list[str]
    mechanism_id: int | None = ...
    fig_width: int = ...
    fig_height: int = ...

def get_mechanism_chart(
    mechanism_id: int, fig_width: int = 320, fig_height: int = 280
) -> tuple[Figure, str]: ...
def get_overall_chart(
    project_id: int, fig_width: int = 320, fig_height: int = 280
) -> tuple[Figure, str]: ...
def get_mechanism_plotly_chart(mechanism_id: int) -> str | None: ...
def get_overall_plotly_chart(project_id: int) -> str | None: ...
def generate_pie_chart(params: PieChartParams) -> Figure: ...
