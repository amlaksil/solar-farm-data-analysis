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

    Returns:
        tuple: A tuple containing Matplotlib figure objects for wind speed
    and wind direction analysis.

    Example:
        wind_analysis('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")

    # Load the data
    data = pd.read_csv(path)

    # Convert 'Timestamp' column to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Create figures
    fig_ws, ax_ws = plt.subplots(figsize=(14, 7))
    fig_wd, ax_wd = plt.subplots(figsize=(14, 7))

    # Plot wind speed and wind direction over time
    ax_ws.plot(data['Timestamp'], data['WS'], label='Wind Speed')
    ax_ws.plot(data['Timestamp'], data['WSgust'], label='Wind Gust Speed')
    ax_ws.plot(data['Timestamp'], data['WSstdev'], label='Wind Speed Std Dev')
    ax_ws.set_xlabel('Timestamp')
    ax_ws.set_ylabel('Value')
    ax_ws.set_title('Wind Speed Analysis')
    ax_ws.legend()

    ax_wd.plot(data['Timestamp'], data['WD'], label='Wind Direction')
    ax_wd.plot(
        data['Timestamp'], data['WDstdev'], label='Wind Direction Std Dev')
    ax_wd.set_xlabel('Timestamp')
    ax_wd.set_ylabel('Value')
    ax_wd.set_title('Wind Direction Analysis')
    ax_wd.legend()

    return fig_ws, fig_wd


if __name__ == '__main__':
    if len(sys.argv) > 1:
        wind_analysis(sys.argv[1])
