#!/usr/bin/python3
"""
Module to explore wind speed and wind direction data.

To explore the wind speed (WS, WSgust, WSstdev) and wind direction
(WD, WDstdev) data to identify trends or notable wind events, we can
plot these variables over time and analyze their distributions.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def wind_analysis(path):
    """
    Explore wind speed and wind direction data.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Example:
        wind_analysis('data.csv')
    """
    if os.path.exists(path):
        # Load the data
        data = pd.read_csv(path)

        # Convert 'Timestamp' column to datetime format
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Plot wind speed and wind direction over time
        plt.figure(figsize=(14, 7))
        plt.plot(data['Timestamp'], data['WS'], label='Wind Speed')
        plt.plot(data['Timestamp'], data['WSgust'], label='Wind Gust Speed')
        plt.plot(
            data['Timestamp'], data['WSstdev'], label='Wind Speed Std Dev')
        plt.xlabel('Timestamp')
        plt.ylabel('Value')
        plt.title('Wind Speed Analysis')
        plt.legend()
        plt.show()

        plt.figure(figsize=(14, 7))
        plt.plot(data['Timestamp'], data['WD'], label='Wind Direction')
        plt.plot(
            data['Timestamp'], data['WDstdev'], label='Wind Direction Std Dev')
        plt.xlabel('Timestamp')
        plt.ylabel('Value')
        plt.title('Wind Direction Analysis')
        plt.legend()
        plt.show()
    else:
        raise FileNotFoundError("File not found")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        wind_analysis(sys.argv[1])
