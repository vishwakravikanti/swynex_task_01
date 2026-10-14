Titanic Dataset Cleaning and Preprocessing
Project Overview

This project demonstrates data cleaning and preprocessing using Python. The Titanic dataset is imported directly from Seaborn, eliminating the need to download the original CSV manually.

Objectives
Import a public dataset.
Identify and handle missing values.
Inspect duplicate records.
Convert appropriate columns to categorical data types.
Validate the cleaned dataset.
Export the cleaned data to CSV.
Technologies Used
Python
Pandas
NumPy
Seaborn
VS Code
Data Cleaning Techniques
Median imputation: Used for missing numerical values such as age and fare.
Mode imputation: Used for missing embarkation categories.
Unknown category: Used to represent unavailable deck and embarkation-town information.
Data type conversion: Selected categorical columns are converted to category types.
Duplicate inspection: Duplicate-looking records are counted but retained unless evidence establishes that they are erroneous.
Assumptions
The median is suitable for filling missing age and fare values.
The most frequent embarkation category is a reasonable replacement for missing values in that column.
Missing deck information should be preserved as Unknown.
Duplicate-looking rows are not automatically errors.
The original dataset is preserved in memory while cleaning is performed on a separate copy.
Output

The cleaned dataset is saved to output/titanic_cleaned.csv.

How to Run

Install the required libraries:

python -m pip install -r requirements.txt

Execute the script:

python data_cleaning.py

An internet connection is required when Seaborn needs to retrieve the dataset.

Conclusion

This project demonstrates basic data-cleaning techniques, missing-value treatment, data-type conversion, duplicate inspection, and CSV export using Python.