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

    # Plot GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(14, 7))
    plt.plot(data['GHI'], label='GHI')
    plt.plot(data['DNI'], label='DNI')
    plt.plot(data['DHI'], label='DHI')
    plt.plot(data['Tamb'], label='Tamb')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Solar Farm Variables Over Time')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        time_series_analysis(sys.argv[1])
