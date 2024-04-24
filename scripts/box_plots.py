#!/usr/bin/python3
"""
Module for creating box plots for solar radiation and temperature data.

To use box plots to examine the spread and presence of outliers in the solar
radiation (GHI, DNI, DHI) and temperature (Tamb, TModA, TModB) data, you can
use the boxplot() method in Pandas.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def box_plot(path):
    """
    Create box plots for solar radiation and temperature data.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Example:
        box_plot('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError

    # Load the data
    data = pd.read_csv(path)

    # Select the columns for box plots
    columns = ['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']

    # Create box plots
    plt.figure(figsize=(14, 7))
    data[columns].boxplot()
    plt.title('Box Plot of Solar Radiation and Temperature Data')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        box_plot(sys.argv[1])
