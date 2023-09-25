# Assessing the Impact of ULEZ on Air Quality in London
## Project Overview

The main goal of this project is to analyse and assess the impact of the Ultra Low Emission Zone (ULEZ) on air quality in London. The project will involve collecting and analysing relevant datasets to understand how the implementation of ULEZ has influenced the pollution levels present in London's air.

## Features

- API data retrieval
- Data collection from various sources
- Data cleaning and preprocessing
- Data analysis to derive insights
- Creation of visualisations to present data
- Implementation of models for predictions
- Integration of maps to visualise geographic data

## Technologies Used

- Python
- Requests
- Pandas
- Meteostat
- Numpy
- Matplotlib
- Seaborn
- Sklearn
- Geopandas 
- Prophet
- Pystan
- Fbprophet

## Usage

1. `sites.py` - uses API to get monitoring sites data and saves it to `sites.csv`.
2. `ULEZ_project_collect_clean.ipynb` - preprocessing monitoring sites.
3. `No2_ulez.py` - uses API to get daily average NO2 data for all monitoring sites we preprocessed and saves the data to `no2_in_ulez.csv` and `no2_exp_ulez.csv`.
4. `ULEZ_project_collect_clean.ipynb` - preprocessing NO2 data, merging it with the weather data, cleaning merged data and getting it ready for the analysis, visualisation and modelling, saves clean files to `merged_data_ulez_1.csv` and `merged_data_ulez_2.csv` (merged data before preprocessing), `in_ulez_clean.csv` and `exp_ulez_clean.csv` (data prepared for analysis), `exp_ulez_only_sites_clean.csv` (clean data for expanded ULEZ, without sites from initial). 
5. `ULEZ_project_analysis_visualisation.ipynb` - analysis, visualisations and forecast.
6. `modelling_experiments.ipynb` - regression models we tried on our dataset.
7. `maps.ipynb` - map of London and initial/expanded ULEZ, three choropleth maps showing average NO2 levels by boroughs before ULEZ introduction, after initial introduction and before expansion, after expansion.


All our files, starting from the collection and ending with maps, include extensive comments for each step of the process.
