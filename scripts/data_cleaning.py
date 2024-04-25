#!/usr/bin/python3
"""
Module for cleaning the dataset by handling anomalies and missing values.

To clean the dataset by handling anomalies and missing values, especially in
columns like Comments which appear entirely null, you can use the following
approach:

1. Drop columns with entirely null values (e.g., Comments).
2. Handle missing values in other columns (e.g., fill with the mean or median).
3. Remove outliers or incorrect entries.
"""
import pandas as pd
import os
import sys


def data_cleaning(path):
    """
    Clean the dataset by handling anomalies and missing values.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        pd.DataFrame: The cleaned dataset.

    Example:
        data_cleaning('data.csv')
    """
    if not os.path.exists(path):
        raise FileNotFoundError

    # Load the data
    data = pd.read_csv(
        path, parse_dates=['Timestamp'], date_format='%Y-%m-%d %H:%M')

    # Drop columns with entirely null values
    data.dropna(axis=1, how='all', inplace=True)

    # Handle missing values in other columns
    data.fillna(data.mean(), inplace=True)  # Fill missing values with the mean

    # Remove outliers or incorrect entries
    # (example: removing negative values from GHI, DNI, DHI)
    data = data[(data['GHI'] >= 0) & (data['DNI'] >= 0) & (data['DHI'] >= 0)]

    return data


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data_cleaning(sys.argv[1])
