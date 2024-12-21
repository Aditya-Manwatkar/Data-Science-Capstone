# Data Science Capstone
In this capstone, we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website, with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

## 📂 Repository Overview

This repository includes various Python notebooks, scripts, and datasets that demonstrate my approach to solving real-world data science problems.

### **Key Components**:

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">

  <!-- Box 1 -->
  <div style="border: 1px solid #ccc; padding: 10px; width: 48%; margin-bottom: 10px;">
    <h3>Data Collection</h3>
    <p>Techniques to collect data via <strong>web scraping</strong> and <strong>API</strong> usage.</p>
    <p>Objective: Extract and clean data from multiple websites for further analysis.</p>
  </div>

  <!-- Box 2 -->
  <div style="border: 1px solid #ccc; padding: 10px; width: 48%; margin-bottom: 10px;">
    <h3>Exploratory Data Analysis (EDA)</h3>
    <p>Discovering patterns and insights using <strong>SQL</strong> queries.</p>
    <p>Objective: Use SQL queries to analyze and manipulate datasets stored in relational databases.</p>
  </div>

</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">

  <!-- Box 3 -->
  <div style="border: 1px solid #ccc; padding: 10px; width: 48%; margin-bottom: 10px;">
    <h3>Machine Learning</h3>
    <p>Building predictive models with <strong>Logistic Regression</strong>, <strong>KNN</strong>, and <strong>SVM</strong>.</p>
    <p>Objective: Predict various outcomes (e.g., launch success) using classification algorithms.</p>
  </div>

  <!-- Box 4 -->
  <div style="border: 1px solid #ccc; padding: 10px; width: 48%; margin-bottom: 10px;">
    <h3>Interactive Visual Analytics</h3>
    <p><strong>Folium</strong> maps for geospatial data and an interactive <strong>SpaceX Launch Dashboard</strong> built with <strong>Dash</strong>.</p>
    <p>Objective: Create interactive maps and dashboards to analyze the data visually.</p>
  </div>

</div>


This repository contains the final project for the Data Science Capstone course. The project focuses on multiple aspects of data science, including data collection, exploratory data analysis (EDA), machine learning, and interactive visual analytics. The key tasks and techniques applied in this repository are:

## Contents:

1. **Data Collection with Web Scraping**:
   - Web scraping techniques to collect data from various sources.

2. **Data Collection using API**:
   - Utilizing APIs to gather datasets for analysis and processing.

3. **EDA with SQL**:
   - Performing exploratory data analysis using SQL queries on the provided datasets.

4. **Interactive Visual Analytics with Folium**:
   - Creating interactive maps and visualizations using Folium for geospatial data insights.

5. **Machine Learning Prediction**:
   - Building and evaluating machine learning models to predict outcomes based on the collected data.

6. **SpaceX Dash App**:
   - A SpaceX launch dashboard application that visualizes data about SpaceX launches and provides insights into the performance of different launches.

## Repository Files:

- **Data Collection with Web Scraping.ipynb**: Jupyter notebook for web scraping data.
- **Data collection using API.ipynb**: Jupyter notebook for API-based data collection.
- **EDA with SQL.ipynb**: Jupyter notebook for performing SQL-based exploratory data analysis.
- **Interactive Visual Analytics with Folium.ipynb**: Jupyter notebook for creating interactive maps using Folium.
- **Machine Learning Prediction.ipynb**: Jupyter notebook for building machine learning models.
- **spacex_dash_app.py**: Python script for the SpaceX dashboard app.
- **spacex_launch_dash.csv**: Data file used for SpaceX launch analysis.
- **README.md**: Project description and instructions.

## Setup and Installation

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/Aditya-Manwatkar/Data-Science-Capstone.git
   ```

2. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebooks or Python scripts as needed to explore and run the analyses.

## Usage

- Explore data collection techniques, including web scraping and API data extraction.
- Perform data analysis using SQL queries and machine learning algorithms.
- Interact with visualizations via the SpaceX dashboard application and Folium maps.
