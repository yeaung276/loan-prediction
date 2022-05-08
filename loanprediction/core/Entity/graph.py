from io import BytesIO
from matplotlib.figure import Figure


class Graph:
    def __init__(self, figure: Figure) -> None:
        self._data = BytesIO()
        figure.savefig(self._data, format="png")

    def export(self) -> BytesIO:
        return self._data
