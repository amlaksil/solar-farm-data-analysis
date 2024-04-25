#!/usr/bin/python3
"""
Module to calculate statistical measures for each numeric column in a dataset.

To calculate the mean, median, standard deviation, and other statistical
measures for each numeric column in the dataset to understand the data
distribution, we can use the describe() method in Pandas.
"""
import pandas as pd
import os
import sys


def calculate_statistical_measures(path):
    """
    Calculate and display the mean, median, standard deviation, minimum,
    maximum, and quartile values for each numeric column in the dataset.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        numeric statistics as a dictionary

    Example:
        calculate_statistical_measures('data.csv')
    """
    if os.path.exists(path):
        # Load the data
        data = pd.read_csv(path)
        numeric_stats = data.describe().to_dict()
        return numeric_stats
    else:
        raise FileNotFoundError("File not found")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(calculate_statistical_measures(sys.argv[1]))
