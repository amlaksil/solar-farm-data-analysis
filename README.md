# Solar Farm Data Analysis

This project analyzes solar farm datasets from Benin Malanville, Sierra Leone Bumbuna, and Togo Dapaong QC. The analysis includes various aspects such as summary statistics, data quality check, time series analysis, correlation analysis, wind analysis, temperature analysis, histograms, box plots, scatter plots, and data cleaning.

## Project Structure

- `app.py`: Main Streamlit application code.
- `data`: Contains CSV files for analysis: `benin-malanville.csv`, `sierraleone-bumbuna.csv`, and `togo-dapaong_qc.csv`.
- `notebooks`: Contains notes for the analysis.
- `requirements.txt`: Dependencies used.
- `scripts`: Contains script files for Exploratory Data Analysis (EDA).
- `tests`: Contains tests for each script.

## Analysis Steps

1. **Summary Statistics**: Calculate mean, median, standard deviation, and other statistical measures for each numeric column.
2. **Data Quality Check**: Look for missing values, outliers, or incorrect entries.
3. **Time Series Analysis**: Analyze how variables change over time.
4. **Correlation Analysis**: Determine the correlation between different variables.
5. **Wind Analysis**: Explore wind speed and wind direction data.
6. **Temperature Analysis**: Compare module temperatures with ambient temperature.
7. **Histograms**: Visualize the frequency distribution of variables.
8. **Box Plots**: Examine the spread and presence of outliers.
9. **Scatter Plots**: Explore relationships between pairs of variables.
10. **Data Cleaning**: Handle anomalies and missing values.

## Installation

1. Clone the repository to your local machine.
```
$ git clone https://github.com/amlaksil/solar-farm-data-analysis.git
```
2. Navigate to the project directory.
```
$ cd solar-farm-data-analysis
```
3. Create a virtual environment.
```
$ python3 -m venv solar-venv
```
4. Activate the virtual environment
```
$ source solar-venv/bin/activate
```
6. Install dependencies using pip
```
$ pip install -r requirements.txt.
```
7. Run `app.py` to start the Streamlit application.
```
$ streamlit run app.py
```

## Troubleshooting

- If you encounter any issues or have questions, please open an issue on the project's GitHub repository (https://github.com/amlaksil/solar-farm-data-analysis/issues).

## License

This project is licensed under the [MIT License](https://mit-license.org/amlaksil).
