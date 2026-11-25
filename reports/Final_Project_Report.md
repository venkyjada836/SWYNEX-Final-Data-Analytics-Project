\# Final Data Analytics Project – Titanic Survival Analysis



\## 1. Project Overview



This project presents an end-to-end data analytics workflow using the Titanic passenger dataset. It combines data cleaning, exploratory data analysis (EDA), data visualization, and an interactive Power BI dashboard to identify patterns and factors associated with passenger survival.



\## 2. Project Objectives



\- Clean and prepare the raw Titanic dataset.

\- Identify and handle missing values and duplicate-looking records.

\- Perform exploratory data analysis.

\- Analyze survival patterns based on gender, passenger class, age group, and embarkation town.

\- Create visualizations to communicate analytical findings.

\- Develop an interactive dashboard using Power BI.



\## 3. Tools and Technologies



\- Python 3.13

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Power BI Desktop

\- Git and GitHub

\- Visual Studio Code



\## 4. Dataset Description



The original dataset contains 891 records and 15 columns, including passenger survival status, passenger class, gender, age, fare, family information, and embarkation details.



After the cleaning process, the dataset contains 784 records and 15 columns.



\## 5. Data Cleaning and Preparation



The following operations were performed:



\- Inspected the original dataset.

\- Identified and removed 107 exact duplicate-looking records.

\- Handled missing values.

\- Standardized categorical values.

\- Corrected appropriate data types.

\- Verified the cleaned dataset.



\### Cleaning Results



| Metric | Result |

|---|---:|

| Original records | 891 |

| Records after cleaning | 784 |

| Columns | 15 |

| Missing values remaining | 0 |

| Duplicate rows remaining | 0 |



\## 6. Exploratory Data Analysis



Exploratory analysis was performed to understand passenger characteristics and survival patterns.



\### Overall Survival



\- Total passengers analyzed: 784

\- Survivors: 323

\- Non-survivors: 461

\- Overall survival rate: 41.20%



\### Survival by Gender



| Gender | Passengers | Survivors | Survival Rate |

|---|---:|---:|---:|

| Female | 293 | 217 | 74.06% |

| Male | 491 | 106 | 21.59% |



Female passengers had a higher observed survival rate than male passengers.



\### Survival by Passenger Class



| Class | Passengers | Survivors | Survival Rate |

|---|---:|---:|---:|

| First | 214 | 135 | 63.08% |

| Second | 165 | 84 | 50.91% |

| Third | 405 | 104 | 25.68% |



First-class passengers had the highest observed survival rate, while third-class passengers had the lowest.



\### Survival by Age Group



| Age Group | Passengers | Survivors | Survival Rate |

|---|---:|---:|---:|

| Child | 68 | 39 | 57.35% |

| Teenager | 67 | 30 | 44.78% |

| Young Adult | 435 | 172 | 39.54% |

| Adult | 192 | 77 | 40.10% |

| Senior | 22 | 5 | 22.73% |



Children had the highest observed survival rate among the age groups, while seniors had the lowest.



\### Survival by Embarkation Town



| Embarkation Town | Passengers | Survival Rate |

|---|---:|---:|

| Cherbourg | 155 | 58.06% |

| Queenstown | 59 | 33.90% |

| Southampton | 570 | 37.37% |



Cherbourg had the highest observed survival rate among the three embarkation towns.



\## 7. Data Visualization



Four charts were generated using Python:



1\. Survival by Gender

2\. Survival by Passenger Class

3\. Survival by Age Group

4\. Survival by Embarkation Town



The chart images are stored in the `charts` directory.



\## 8. Power BI Dashboard



An interactive Titanic Survival Dashboard was developed using Power BI Desktop.



\### Dashboard Components



\- Total Passengers

\- Total Survivors

\- Survival Rate

\- Total Non-Survivors

\- Survival rate by gender

\- Survival rate by passenger class

\- Survival rate by age group

\- Filters for gender, passenger class, and embarkation town



The dashboard is saved as `dashboard/Titanic\_Survival\_Dashboard.pbix`.



\## 9. Key Insights



\- The overall survival rate in the cleaned dataset was 41.20%.

\- Female passengers had a substantially higher observed survival rate than male passengers.

\- First-class passengers had a higher observed survival rate than second- and third-class passengers.

\- Children had the highest survival rate among the analyzed age groups.

\- Cherbourg had the highest observed survival rate among the embarkation towns.



\## 10. Limitations



The cleaning process removed 107 exact duplicate-looking records. The available dataset does not provide a unique passenger identifier for distinguishing passengers with identical recorded attributes. Therefore, some removed records may represent different passengers rather than erroneous duplicates.



The findings describe associations in the cleaned dataset and do not establish that any particular characteristic caused survival.



\## 11. Conclusion



This project demonstrates an end-to-end data analytics process, from raw dataset preparation to exploratory analysis, visualization, and interactive dashboard development.



The analysis identifies differences in survival rates across gender, passenger class, age group, and embarkation town. Python and Power BI were used to transform the dataset into understandable analytical findings and visual insights.

