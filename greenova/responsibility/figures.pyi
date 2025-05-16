# Stub file for responsibility.figures

from matplotlib.figure import Figure

def generate_responsibility_chart(
    responsibility_counts: dict[str, int], fig_width: int = ..., fig_height: int = ...
) -> Figure: ...
def get_responsibility_chart(
    mechanism_id: int,
    fig_width: int = ...,
    fig_height: int = ...,
    filtered_ids: list[int] | None = None,
) -> Figure: ...
