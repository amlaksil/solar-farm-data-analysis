#!/usr/bin/python3
import sys
import streamlit as st
import pandas as pd
import os
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from scripts import summary_statistics, data_quality_check, \
    time_series_analysis, correlation_analysis, wind_analysis, \
    temperature_analysis, histograms, box_plots, scatter_plots, data_cleaning

if __name__ == '__main__':
    st.title('Solar Farm Data Analysis Dashboard')
    # Add a file uploader widget
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp.csv", "wb") as f:
            # Initialize progress bar
            progress = st.progress(0)
            # Read uploaded file in chunks to update progress bar
            for percent in range(0, 101, 5):
                f.write(uploaded_file.read(
                    int(len(uploaded_file.getvalue()) / 100 * 5)))
                progress.progress(percent)
        paths = [
            'README.md', 'notebooks/summary_note.md',
            'notebooks/benin_correlation_analysis.md',
            'notebooks/benin_quality_check.md',
            'notebooks/benin_statistics.md',
            'notebooks/benin_temperature_analysis.md',
            'notebooks/benin_time_series_analysis.md',
            'notebooks/benin_wind_analysis.md',
            'notebooks/sierraleone_correlation_analysis.md',
            'notebooks/sierraleone_quality_check.md',
            'notebooks/sierraleone_statistics.md',
            'notebooks/sierraleone_temperature_analysis.md',
            'notebooks/sierraleone_time_series_anlaysis.md',
            'notebooks/sierraleone_wind_analysis.md',
            'notebooks/togo_correlation_analysis.md',
            'notebooks/togo_quality_check.md',
            'notebooks/togo_statistics.md',
            'notebooks/togo_temperature_analysis.md',
            'notebooks/togo_time_series_anlaysis.md',
            'notebooks/togo_wind_analysis.md',
            'notebooks/correlation_analysis.md', 'notebooks/data_cleaning.md',
            'notebooks/scatter_plots.md', 'notebooks/temperature_analysis.md',
            'notebooks/time_series_anlaysis.md', 'notebooks/wind_analysis.md'
        ]
        contents = {}
        for path in paths:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    contents[path.split('/', 1)[-1]] = f.read()

        # Sidebar for selecting analysis
        analysis = st.sidebar.selectbox(
            'Select Exploratory Data Analysis (EDA)',
            ['Summary Statistics', 'Data Quality Check',
             'Time Series Analysis', 'Correlation Analysis',
             'Wind Analysis', 'Temperature Analysis',
             'Histograms', 'Box Plots', 'Scatter Plots', 'Data Cleaning']
        )

        # Run selected analysis
        if analysis == 'Summary Statistics':
            st.subheader('Summary Statistics')
            data = pd.DataFrame(
                summary_statistics.calculate_statistical_measures('temp.csv'))
            st.table(data)
            st.markdown(contents['summary_note.md'])

            if uploaded_file and uploaded_file.name == 'benin-malanville.csv':
                st.markdown(contents['benin_statistics.md'])
            elif uploaded_file and uploaded_file.name ==\
                    'sierraleone-bumbuna.csv':
                st.markdown(contents['sierraleone_statistics.md'])
            elif uploaded_file and uploaded_file.name == 'togo-dapaong_qc.csv':
                st.markdown(contents['togo_statistics.md'])

            # Add a download button
            if st.button('Download CSV'):
                csv = data.to_csv(index=False)
                st.download_button(
                    label='Download CSV', data=csv,
                    file_name='summary_statistics.csv', mime='text/csv')
        elif analysis == 'Data Quality Check':
            st.subheader('Data Quality Check')
            data = data_quality_check.data_quality_check('temp.csv')
            st.table(data)

            if uploaded_file and uploaded_file.name == 'benin-malanville.csv':
                st.markdown(contents['benin_quality_check.md'])
            elif uploaded_file and uploaded_file.name == \
                    'sierraleone-bumbuna.csv':
                st.markdown(contents['sierraleone_quality_check.md'])
            elif uploaded_file and uploaded_file.name == 'togo-dapaong_qc.csv':
                st.markdown(contents['togo_quality_check.md'])

            # Add a download button
            if st.button('Download CSV'):
                csv = data.to_csv(index=False)
                st.download_button(
                    label='Download CSV', data=csv,
                    file_name='data_quality_check.csv', mime='text/csv')
        elif analysis == 'Time Series Analysis':
            st.subheader('Time Series Analysis')
            plt = (time_series_analysis.time_series_analysis('temp.csv'))
            st.pyplot(plt)

            if uploaded_file and uploaded_file.name == 'benin-malanville.csv':
                st.markdown(contents['benin_time_series_analysis.md'])
            elif uploaded_file and uploaded_file.name == \
                    'sierraleone-bumbuna.csv':
                st.markdown(contents['sierraleone_time_series_anlaysis.md'])
            elif uploaded_file and uploaded_file.name == 'togo-dapaong_qc.csv':
                st.markdown(contents['togo_time_series_anlaysis.md'])
        elif analysis == 'Correlation Analysis':
            st.subheader('Correlation Analysis')
            plt = (correlation_analysis.correlation_analysis('temp.csv'))
            st.pyplot(plt)

            if uploaded_file and uploaded_file.name == 'benin-malanville.csv':
                st.markdown(contents['benin_correlation_analysis.md'])
            elif uploaded_file and uploaded_file.name == \
                    'sierraleone-bumbuna.csv':
                st.markdown(contents['sierraleone_correlation_analysis.md'])
            elif uploaded_file and uploaded_file.name == 'togo-dapaong_qc.csv':
                st.markdown(contents['togo_correlation_analysis.md'])
        elif analysis == 'Wind Analysis':
            st.subheader('Wind Analysis')
            fig_ws, fig_wd = wind_analysis.wind_analysis('temp.csv')
            st.pyplot(fig_ws)
            st.pyplot(fig_wd)

            if uploaded_file and uploaded_file.name == 'benin-malanville.csv':
                st.markdown(contents['benin_wind_analysis.md'])
            elif uploaded_file and uploaded_file.name == \
                    'sierraleone-bumbuna.csv':
                st.markdown(contents['sierraleone_wind_analysis.md'])
            elif uploaded_file and uploaded_file.name == 'togo-dapaong_qc.csv':
                st.markdown(contents['togo_wind_analysis.md'])
        elif analysis == 'Temperature Analysis':
            st.subheader('Temperature Analysis')
            fig_temp = temperature_analysis.temperature_analysis('temp.csv')
            st.pyplot(fig_temp)
            if uploaded_file and uploaded_file.name == 'benin-malanville.csv':
                st.markdown(contents['benin_temperature_analysis.md'])
            elif uploaded_file and uploaded_file.name == \
                    'sierraleone-bumbuna.csv':
                st.markdown(contents['sierraleone_temperature_analysis.md'])
            elif uploaded_file and uploaded_file.name == 'togo-dapaong_qc.csv':
                st.markdown(contents['togo_temperature_analysis.md'])
        elif analysis == 'Histograms':
            st.subheader('Histograms')
            fig_hist = histograms.histograms('temp.csv')
            st.pyplot(fig_hist)
        elif analysis == 'Box Plots':
            st.subheader('Box Plots')
            fig_boxplot = box_plots.box_plot('temp.csv')
            st.pyplot(fig_boxplot)
        elif analysis == 'Scatter Plots':
            st.subheader('Scatter Plots')
            fig_boxplot = scatter_plots.scatter_plots('temp.csv')
            st.pyplot(fig_boxplot)
        elif analysis == 'Data Cleaning':
            cleaned_data = data_cleaning.data_cleaning("temp.csv")
            st.write(cleaned_data.head())
        # Display README
        st.markdown(contents['README.md'])
