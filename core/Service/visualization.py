from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt

from core.Entity.graph import Graph
from core.Exception.ColumnNotFound import ColumnNotFound


class Visualizer:
    """Visualization Service for graphing user data"""

    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    def graph_null(self) -> Graph:
        """graph amount of null number in each row as pie chart

        Returns:
          Graph: Graph obj holding exported figure
        """
        figure = plt.figure()
        self.dataframe \
            .isnull() \
            .sum(axis=1) \
            .value_counts() \
            .plot(kind='pie',
                  title="Null Count Chart",
                  label='Number of null value',
                  autopct='%.2f')
        return Graph(figure)

    def graph_column(self, column: str) -> Graph:
        """graph null and value counts of column if it is categorical column
        show normal graph if it is numerical column

        Args:
          column (str): column name of dataframe

        Returns:
          BytesIO: png file
        """
        figure = plt.figure(column)
        try:
            graph_data = self.dataframe[column].copy()
        except KeyError as error:
            raise ColumnNotFound from error
        if self.is_categorical(graph_data):
            self.plot_categorical(graph_data, figure)
        else:
            self.plot_numerical(graph_data, figure)
        return Graph(figure)

    @staticmethod
    def is_categorical(column: pd.Series) -> bool:
        for value in column.unique():
            try:
                float(value)
            except ValueError:
                return True
        return False

    @staticmethod
    def plot_categorical(column: pd.Series, figure: Figure) -> None:
        axes = figure.add_subplot(111)
        column.fillna('NULL').value_counts().plot(
            kind='pie', subplots=True, autopct='%.2f', ax=axes)

    def plot_numerical(self, column: pd.Series, figure: Figure) -> None:
        axes1 = figure.add_subplot(211)
        axes2 = figure.add_subplot(212)
        self.plot_numerical_nulls(column, axes1)
        self.plot_numerical_statistics(column, axes2)

    @staticmethod
    def plot_numerical_nulls(column: pd.Series, axis: plt.Axes) -> None:
        null_count = column.copy()
        null_count[null_count.notnull()] = 'Not Null'
        null_count = null_count.fillna('Null')
        null_count.value_counts().plot(kind='pie', autopct='%.2f', ax=axis)

    @staticmethod
    def plot_numerical_statistics(column: pd.Series, axis: plt.Axes) -> None:
        new_column = column.copy()
        new_column.plot.density(ax=axis)
