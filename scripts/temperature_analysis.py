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

    Example:
        temperature_analysis('data.csv')
    """
    if os.path.exists(path):
        # Load the data
        data = pd.read_csv(path)

        # Convert 'Timestamp' column to datetime format
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Plot module temperatures and ambient temperature over time
        plt.figure(figsize=(14, 7))
        plt.plot(
            data['Timestamp'], data['TModA'], label='Module Temperature A')
        plt.plot(
            data['Timestamp'], data['TModB'], label='Module Temperature B')
        plt.plot(data['Timestamp'], data['Tamb'], label='Ambient Temperature')
        plt.xlabel('Timestamp')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Analysis')
        plt.legend()
        plt.show()
    else:
        raise FileNotFoundError("File not found")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        temperature_analysis(sys.argv[1])
