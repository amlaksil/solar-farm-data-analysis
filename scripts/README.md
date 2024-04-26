# Solar Farm Data Analysis Scripts

This repository contains scripts for performing exploratory data analysis (EDA) on solar farm data. Each script focuses on a specific aspect of the analysis:

- `summary_statistics.py`: Calculates the mean, median, standard deviation, and other statistical measures for each numeric column to understand data distribution.
- `data_quality_check.py`: Looks for missing values, outliers, or incorrect entries, especially in columns like GHI, DNI, and DHI.
- `time_series_analysis.py`: Analyzes how variables like GHI, DNI, DHI, and Tamb change over time by plotting these metrics across the 'Timestamp' to identify patterns or anomalies.
- `correlation_analysis.py`: Determines the correlation between different variables like solar radiation components (GHI, DHI, DNI) and temperature measures (TModA, TModB) to uncover relationships.
- `wind_analysis.py`: Explores wind speed (WS, WSgust, WSstdev) and wind direction (WD, WDstdev) data to identify trends or notable wind events.
- `temperature_analysis.py`: Compares module temperatures (TModA, TModB) with ambient temperature (Tamb) to see how they are related or vary under different conditions.
- `histograms.py`: Creates histograms for variables like GHI, DNI, DHI, WS, and temperatures to visualize the frequency distribution of these variables.
- `box_plots.py`: Uses box plots to examine the spread and presence of outliers in the solar radiation and temperature data.
- `scatter_plots.py`: Generates scatter plots to explore the relationships between pairs of variables, such as GHI vs. Tamb, WS vs. WSgust, or any other potentially interesting pairs.
- `data_cleaning.py`: Cleans the dataset by handling anomalies and missing values, especially in columns like Comments which appear entirely null.
