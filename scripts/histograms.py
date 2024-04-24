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

    Example:
        histograms('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError
    # Load the data
    data = pd.read_csv(path)

    # Plot histograms for GHI, DNI, DHI, WS, and temperatures
    plt.figure(figsize=(14, 7))
    plt.subplot(2, 3, 1)
    data['GHI'].hist(bins=30, color='skyblue')
    plt.title('GHI Histogram')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 2)
    data['DNI'].hist(bins=30, color='salmon')
    plt.title('DNI Histogram')
    plt.xlabel('DNI (W/m²)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 3)
    data['DHI'].hist(bins=30, color='lightgreen')
    plt.title('DHI Histogram')
    plt.xlabel('DHI (W/m²)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 4)
    data['WS'].hist(bins=30, color='gold')
    plt.title('Wind Speed Histogram')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 5)
    data['Tamb'].hist(bins=30, color='orange')
    plt.title('Ambient Temperature Histogram')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        histograms(sys.argv[1])
