\# Titanic Survival Analysis – Final Data Analytics Project



\## Project Overview

This project performs an end-to-end data analytics workflow using the Titanic passenger dataset. It combines data cleaning, exploratory data analysis (EDA), data visualization, and an interactive Power BI dashboard.



\## Project Objectives

\- Clean and prepare the Titanic dataset.

\- Identify missing values, duplicates, and data quality issues.

\- Explore passenger survival patterns.

\- Visualize survival trends using Python charts.

\- Build an interactive dashboard using Power BI.

\- Present meaningful insights from the analysis.



\## Tools and Technologies

\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Power BI Desktop

\- Git and GitHub

\- Visual Studio Code



\## Project Workflow

1\. Data Collection

2\. Data Cleaning and Preparation

3\. Exploratory Data Analysis

4\. Data Visualization

5\. Interactive Dashboard Development

6\. Final Reporting



\## Dataset Information

\- Original records: 891

\- Records after duplicate-looking rows were removed: 784

\- Columns: 15

\- Remaining missing values: 0

\- Remaining duplicate rows: 0



\## Key Findings

\- Overall survival rate: 41.20%.

\- Female survival rate: 74.06%.

\- Male survival rate: 21.59%.

\- First-class survival rate: 63.08%.

\- Second-class survival rate: 50.91%.

\- Third-class survival rate: 25.68%.

\- Child survival rate: 57.35%.



\## Visualizations

Four charts were generated:

\- Survival by Gender

\- Survival by Passenger Class

\- Survival by Age Group

\- Survival by Embarkation Town



Charts are available in the `charts` folder.



\## Power BI Dashboard

The interactive dashboard includes:

\- Total passengers

\- Total survivors

\- Survival rate

\- Non-survivors

\- Survival analysis by gender, class, and age group

\- Filters for gender, passenger class, and embarkation town



Dashboard file: `dashboard/Titanic\_Survival\_Dashboard.pbix`



\## Project Structure

```text

SWYNEX-Final-Data-Analytics-Project/

├── charts/

├── dashboard/

│   ├── screenshots/

│   └── Titanic\_Survival\_Dashboard.pbix

├── data/

│   ├── raw/

│   └── processed/

├── reports/

├── scripts/

│   ├── clean\_data.py

│   └── eda\_analysis.py

├── README.md

└── requirements.txt

