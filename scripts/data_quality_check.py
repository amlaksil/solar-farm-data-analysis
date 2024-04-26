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

    Example:
        data_quality_check('data.csv')
    """
    if os.path.exists(path):
        # Load the data
        data = pd.read_csv(path)

        # Check for missing values
        missing_values = data.isnull().sum()
        print(f"Missing values:\n{missing_values}")

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

        if negative_values:
            print(f"Negative values in columns where only positive values" +
                  f"should exist:\n{negative_values}")

        # Check for incorrect entries in cleaning column
        cleaning_values = data['Cleaning'].unique()
        print(f"Cleaning column values:\n{cleaning_values}")

        # Check for outliers using box plots
        plt.figure(figsize=(14, 7))
        data[['GHI', 'DNI', 'DHI']].boxplot()
        plt.title('Box Plot of GHI, DNI, and DHI')
        plt.ylabel('Value')
        plt.show()
    else:
        raise FileNotFoundError("File not found")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data_quality_check(sys.argv[1])
