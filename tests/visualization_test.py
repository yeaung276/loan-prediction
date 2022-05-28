from PIL import Image
import pandas as pd
from LoanPrediction.core.Service.visualization import Visualizer


def test_whole_graph() -> None:
    dataframe = pd.read_csv("data/train_.csv")
    visualizer = Visualizer(dataframe)
    return_image = visualizer.graph_null()
    img = Image.open(return_image.export())
    img.show()


def test_column_graph() -> None:
    dataframe = pd.read_csv("data/train_.csv")
    visualizer = Visualizer(dataframe)
    return_image = visualizer.graph_column("Gender")
    img = Image.open(return_image.export())
    img.show()


def test() -> None:
    test_column_graph()
    test_whole_graph()
