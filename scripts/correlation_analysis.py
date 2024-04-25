#!/usr/bin/python3

"""
Module to determine the correlation between different variables.

To determine the correlation between different variables like GHI, DHI, DNI,
TModA, and TModB, we can use the `corr()` method in Pandas. This method
calculates the Pearson correlation coefficient, which measures the linear
correlation between two variables. A value of 1 indicates a perfect positive
correlation, -1 indicates a perfect negative correlation, and 0 indicates no
correlation.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys


def correlation_analysis(path):
    """
    Generate a heatmap showing the correlation between GHI, DNI, DHI, TModA
    and TModB.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        matplotlib.figure.Figure: Matplotlib figure object containing the plot.

    Example:
        correlation_analysis('data.csv')
    """
    if os.path.exists(path):
        # Load the data
        data = pd.read_csv(path)

        # Select the columns for correlation analysis
        columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']

        # Calculate the correlation matrix
        correlation_matrix = data[columns].corr()

        # Create a new figure
        fig, ax = plt.subplots(figsize=(10, 8))

        # Plot the correlation matrix as a heatmap
        sns.heatmap(
            correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        ax.set_title('Correlation Matrix')
        return fig
    else:
        raise FileNotFoundError("File not found")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        correlation_analysis(sys.argv[1])
