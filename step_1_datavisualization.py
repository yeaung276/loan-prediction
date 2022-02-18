import pandas as pd
import matplotlib.pyplot as plt

from config import TRAINING_FILE

train_data = pd.read_csv(TRAINING_FILE)

def graph_data(data: pd.DataFrame,column_no:int) -> None:
    graph_data = data.copy()
    graph_data[column_no].fillna('NULL').value_counts().plot(kind='pie', subplots=True, autopct='%.2f')
    plt.show()
    
def graph_null(data: pd.DataFrame) -> None:
    graph_data = data.copy()
    graph_data \
    .isnull() \
    .sum(axis=1) \
    .value_counts() \
    .plot(kind='pie', 
        title="Null Count Chart",
        label='Number of null value',
        autopct='%.2f')
    plt.show()

def main():
    print('mainfunction')
    # graph_data(train_data)
    graph_null(train_data)

if __name__ == '__main__':
    main()