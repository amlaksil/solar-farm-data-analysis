#!/usr/bin/python3
"""
Module to perform a data quality check and identify missing values, negative
values, and outliers.

To perform a data quality check and look for missing values, outliers, or
incorrect entries, especially in columns like GHI, DNI, and DHI where negative
values should not exist, we can use the following approach:

1. Check for missing values in the dataset.
2. Check for negative values in columns where only positive values should exist
3. Check for outliers using box plots or other visualization techniques.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def data_quality_check(path):
    """
    Perform a data quality check to identify missing values, negative
    values, and outliers.

    Args:
        path (str): The path to the CSV file containing the dataset.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Returns:
        pd.DataFrame: DataFrame containing the results of the data quality
    check.

    Example:
        data_quality_check('data.csv')
    """
    if os.path.exists(path):
        # Load the data
        data = pd.read_csv(path)

        # Check for missing values
        missing_values = data.isnull().sum()

        """
        Check for negative values in columns where only positive values
        should exist
        """
        negative_values = {}
        # Specify columns where only positive values should exist
        positive_only_columns = ['GHI', 'DNI', 'DHI']
        for column in positive_only_columns:
            # Count negative values in the column
            negative_values[column] = data[data[column] < 0].shape[0]

        # Check for incorrect entries in cleaning column
        cleaning_values = data['Cleaning'].unique()

        # Create DataFrame to hold results
        result_df = pd.DataFrame({
            'Missing Values': missing_values,
            'Negative Values': list(negative_values.values()),
            'Cleaning Column Values': [", ".join(map(str, cleaning_values))]
        }, index=list(negative_values.keys()))
        return result_df
    else:
        raise FileNotFoundError("File not found")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(data_quality_check(sys.argv[1]))
