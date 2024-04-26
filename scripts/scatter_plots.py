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

    Returns:
        matplotlib.figure.Figure: Matplotlib figure object containing the
    scatter plots.

    Example:
        scatter_plots('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError

    # Load the data
    data = pd.read_csv(path)

    # Create scatter plots
    fig, axs = plt.subplots(2, 2, figsize=(14, 7))

    # GHI vs. Tamb
    axs[0, 0].scatter(data['GHI'], data['Tamb'])
    axs[0, 0].set_title('GHI vs. Tamb')
    axs[0, 0].set_xlabel('GHI (W/m²)')
    axs[0, 0].set_ylabel('Tamb (°C)')

    # WS vs. WSgust
    axs[0, 1].scatter(data['WS'], data['WSgust'])
    axs[0, 1].set_title('WS vs. WSgust')
    axs[0, 1].set_xlabel('WS (m/s)')
    axs[0, 1].set_ylabel('WSgust (m/s)')

    # DNI vs. DHI
    axs[1, 0].scatter(data['DNI'], data['DHI'])
    axs[1, 0].set_title('DNI vs. DHI')
    axs[1, 0].set_xlabel('DNI (W/m²)')
    axs[1, 0].set_ylabel('DHI (W/m²)')

    # TModA vs. TModB
    axs[1, 1].scatter(data['TModA'], data['TModB'])
    axs[1, 1].set_title('TModA vs. TModB')
    axs[1, 1].set_xlabel('TModA (°C)')
    axs[1, 1].set_ylabel('TModB (°C)')

    # Adjust layout
    plt.tight_layout()

    return fig


if __name__ == '__main__':
    if len(sys.argv) > 1:
        scatter_plots(sys.argv[1])
