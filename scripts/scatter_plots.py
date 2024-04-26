#!/usr/bin/python3
"""
Module for generating scatter plots to explore relationships between
pairs of variables.

To generate scatter plots to explore the relationships between pairs of
variables, such as GHI vs. Tamb, WS vs. WSgust, or any other potentially
interesting pairs, you can use the scatter() method in Matplotlib.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def scatter_plots(path):
    """
    Create scatter plots to explore relationships between pairs of variables.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Example:
        scatter_plots('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError

    # Load the data
    data = pd.read_csv(path)

    # Create scatter plots
    plt.figure(figsize=(14, 7))

    # GHI vs. Tamb
    plt.subplot(2, 2, 1)
    plt.scatter(data['GHI'], data['Tamb'])
    plt.title('GHI vs. Tamb')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Tamb (°C)')

    # WS vs. WSgust
    plt.subplot(2, 2, 2)
    plt.scatter(data['WS'], data['WSgust'])
    plt.title('WS vs. WSgust')
    plt.xlabel('WS (m/s)')
    plt.ylabel('WSgust (m/s)')

    # DNI vs. DHI
    plt.subplot(2, 2, 3)
    plt.scatter(data['DNI'], data['DHI'])
    plt.title('DNI vs. DHI')
    plt.xlabel('DNI (W/m²)')
    plt.ylabel('DHI (W/m²)')

    # TModA vs. TModB
    plt.subplot(2, 2, 4)
    plt.scatter(data['TModA'], data['TModB'])
    plt.title('TModA vs. TModB')
    plt.xlabel('TModA (°C)')
    plt.ylabel('TModB (°C)')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        scatter_plots(sys.argv[1])
