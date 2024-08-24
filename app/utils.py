import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import st

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"File {file_path} not found.")
        return None
    except pd.errors.EmptyDataError:
        st.error(f"File {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        st.error(f"Error parsing file {file_path}.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        return None


def calculate_average(data, column):
    if column in data.columns:
        return data[column].mean()
    else:
        raise ValueError(f"Column '{column}' does not exist in the data.")

def plot_distribution(data, column):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()
