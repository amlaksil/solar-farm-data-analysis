#!/usr/bin/python3
"""
Module to compare module temperatures with ambient temperature.

To compare module temperatures (TModA, TModB) with ambient temperature (Tamb)
and see how they are related or vary under different conditions, we can plot
these variables over time and analyze their relationships.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def temperature_analysis(path):
    """
    Plot module temperatures (TModA, TModB) and ambient temperature (Tamb)
    over time.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        matplotlib.figure.Figure: Matplotlib figure object containing the plot.

    Example:
        temperature_analysis('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")

    # Load the data
    data = pd.read_csv(path)

    # Convert 'Timestamp' column to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Create a new figure
    fig, ax = plt.subplots(figsize=(14, 7))

    # Plot module temperatures and ambient temperature over time
    ax.plot(data['Timestamp'], data['TModA'], label='Module Temperature A')
    ax.plot(data['Timestamp'], data['TModB'], label='Module Temperature B')
    ax.plot(data['Timestamp'], data['Tamb'], label='Ambient Temperature')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Analysis')
    ax.legend()

    return fig


if __name__ == '__main__':
    if len(sys.argv) > 1:
        temperature_analysis(sys.argv[1])
