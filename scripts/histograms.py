#!/usr/bin/python3
"""
Module to create histograms for variables like GHI, DNI, DHI, WS, and
temperatures.

To create histograms for variables like GHI, DNI, DHI, WS, and temperatures
to visualize
their frequency distribution, we can use the hist() method in Pandas.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def histograms(path):
    """
    Plot histograms for variables GHI, DNI, DHI, WS, and temperatures.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        matplotlib.figure.Figure: Matplotlib figure object containing
    the plots.

    Example:
        histograms('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError
    # Load the data
    data = pd.read_csv(path)

    # Create a new figure
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    # Plot histograms for GHI, DNI, DHI, WS, and temperatures
    data['GHI'].hist(bins=30, color='skyblue', ax=axs[0, 0])
    axs[0, 0].set_title('GHI Histogram')
    axs[0, 0].set_xlabel('GHI (W/m²)')
    axs[0, 0].set_ylabel('Frequency')

    data['DNI'].hist(bins=30, color='salmon', ax=axs[0, 1])
    axs[0, 1].set_title('DNI Histogram')
    axs[0, 1].set_xlabel('DNI (W/m²)')
    axs[0, 1].set_ylabel('Frequency')

    data['DHI'].hist(bins=30, color='lightgreen', ax=axs[0, 2])
    axs[0, 2].set_title('DHI Histogram')
    axs[0, 2].set_xlabel('DHI (W/m²)')
    axs[0, 2].set_ylabel('Frequency')

    data['WS'].hist(bins=30, color='gold', ax=axs[1, 0])
    axs[1, 0].set_title('Wind Speed Histogram')
    axs[1, 0].set_xlabel('Wind Speed (m/s)')
    axs[1, 0].set_ylabel('Frequency')

    data['Tamb'].hist(bins=30, color='orange', ax=axs[1, 1])
    axs[1, 1].set_title('Ambient Temperature Histogram')
    axs[1, 1].set_xlabel('Ambient Temperature (°C)')
    axs[1, 1].set_ylabel('Frequency')

    # Remove the empty subplot
    fig.delaxes(axs[1, 2])

    # Adjust layout
    fig.tight_layout()

    return fig


if __name__ == '__main__':
    if len(sys.argv) > 1:
        histograms(sys.argv[1])
