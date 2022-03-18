from PIL import Image
import pandas as pd
from core.Service.visualization import Visualizer


def test_whole_graph():
    dataframe = pd.read_csv('data/train_.csv')
    visualizer = Visualizer(dataframe)
    return_image = visualizer.graph_null()
    img = Image.open(return_image.export())
    img.show()


def test_column_graph():
    dataframe = pd.read_csv('data/train_.csv')
    visualizer = Visualizer(dataframe)
    return_image = visualizer.graph_column('Gender')
    img = Image.open(return_image.export())
    img.show()


if __name__ == '__main__':
    test_column_graph()
