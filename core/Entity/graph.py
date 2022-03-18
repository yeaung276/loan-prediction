from io import BytesIO
from matplotlib.figure import Figure


class Graph:
    def __init__(self, figure: Figure) -> None:
        self.data = BytesIO()
        figure.savefig(self.data, format="png")

    def export(self) -> BytesIO:
        return self.data
