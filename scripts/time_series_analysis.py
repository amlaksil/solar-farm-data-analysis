#!/usr/bin/python3
"""
Module to perform time series analysis and plot how variables change over time.

To perform a time series analysis and plot how variables like GHI, DNI, DHI
and Tamb
change over time, we can use the following approach:
    1. Convert the `Timestamp` column to a datetime format.
    2. Set the `Timestamp` column as the index of the DataFrame.
    3. Plot the variables against the `Timestamp` index.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def time_series_analysis(path):
    """
    Perform time series analysis and plot how variables change over time.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        matplotlib.figure.Figure: Matplotlib figure object containing the plot.

    Example:
        time_series_analysis('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")

    # Load the data
    data = pd.read_csv(path)

    # Convert the `Timestamp` column to datetime format and set it as the index
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)

    # Create a new figure
    fig, ax = plt.subplots(figsize=(14, 7))

    ax.plot(data.index, data['GHI'], label='GHI')
    ax.plot(data.index, data['DNI'], label='DNI')
    ax.plot(data.index, data['DHI'], label='DHI')
    ax.plot(data.index, data['Tamb'], label='Tamb')

    # Set labels and title
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Value')
    ax.set_title('Solar Farm Variables Over Time')

    # Add legend
    ax.legend()

    return fig


if __name__ == '__main__':
    if len(sys.argv) > 1:
        time_series_analysis(sys.argv[1])
