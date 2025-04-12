# -*- coding: utf-8 -*-
"""xp

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oKjDPpuOYQ5yMh1sQdeSteu-Ib4kypgS

Exercise 1: Duplicate Detection and Removal
Instructions
Objective: Identify and remove duplicate entries in the Titanic dataset.

Load the Titanic dataset.
Identify if there are any duplicate rows based on all columns.
Remove any duplicate rows found in the dataset.
Verify the removal of duplicates by checking the number of rows before and after the duplicate removal.
Hint: Use the duplicated() and drop_duplicates() functions in Pandas.
"""

import pandas as pd
try:
    titanic_df = pd.read_csv('titanic.csv')
except FileNotFoundError:
    print("Error: 'titanic.csv' not found. Please provide the correct file path.")
    exit()


# Identify duplicate rows
duplicate_rows = titanic_df.duplicated()

# Count the number of duplicate rows
num_duplicates = duplicate_rows.sum()

print(f"Number of duplicate rows before removal: {num_duplicates}")

# Remove duplicate rows
titanic_df_no_duplicates = titanic_df.drop_duplicates()

# Verify the removal of duplicates
num_rows_original = len(titanic_df)
num_rows_no_duplicates = len(titanic_df_no_duplicates)

print(f"Number of rows before duplicate removal: {num_rows_original}")
print(f"Number of rows after duplicate removal: {num_rows_no_duplicates}")
print(f"Number of duplicates removed: {num_rows_original-num_rows_no_duplicates}")

# Display the DataFrame without duplicates (optional)
# print(titanic_df_no_duplicates)

""" Exercise 2: Handling Missing Values
Instructions
Identify columns in the Titanic dataset with missing values.
Explore different strategies for handling missing data, such as removal, imputation, and filling with a constant value.
Apply each strategy to different columns based on the nature of the data.
Hint: Review methods like dropna(), fillna(), and SimpleImputer from scikit-learn.


"""

import pandas as pd
from sklearn.impute import SimpleImputer

try:
    titanic_df = pd.read_csv('titanic.csv')
except FileNotFoundError:
    print("Error: 'titanic.csv' not found. Please provide the correct file path.")
    exit()

# Identify columns with missing values
missing_values = titanic_df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Handling missing values
# 1. Removal: Remove rows or columns with missing values
#titanic_df_dropped = titanic_df.dropna() #remove all rows with any missing values
#titanic_df_dropped_age = titanic_df.dropna(subset=['Age']) #remove rows with missing age

# 2. Imputation: Fill missing values using different strategies
# Mean imputation for numerical columns
imputer_mean = SimpleImputer(strategy='mean')
titanic_df['Age'] = imputer_mean.fit_transform(titanic_df[['Age']])
#titanic_df['Fare'] = imputer_mean.fit_transform(titanic_df[['Fare']])

# Median imputation
imputer_median = SimpleImputer(strategy='median')
#titanic_df['Age'] = imputer_median.fit_transform(titanic_df[['Age']])

# Most frequent imputation for categorical columns
imputer_most_frequent = SimpleImputer(strategy='most_frequent')
titanic_df['Embarked'] = imputer_most_frequent.fit_transform(titanic_df[['Embarked']])
titanic_df['Cabin'] = imputer_most_frequent.fit_transform(titanic_df[['Cabin']])

# 3. Filling with a constant value
titanic_df['Cabin'].fillna('Unknown', inplace=True)

# Verify the handling of missing values
missing_values_after = titanic_df.isnull().sum()
print("\nMissing values after handling:\n", missing_values_after)

"""🌟 Exercise 3: Feature Engineering
Instructions
Create new features, such as Family Size from SibSp and Parch, and Title extracted from the Name column.
Convert categorical variables into numerical form using techniques like one-hot encoding or label encoding.
Normalize or standardize numerical features if required.
Hint: Utilize Pandas for data manipulation and scikit-learn’s preprocessing module for encoding.


"""

import pandas as pd
# Create 'FamilySize' feature
titanic_df['FamilySize'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1

# Extract 'Title' from 'Name'
titanic_df['Title'] = titanic_df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
# Replace rare titles with a common label
titanic_df['Title'] = titanic_df['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
titanic_df['Title'] = titanic_df['Title'].replace('Mlle', 'Miss')
titanic_df['Title'] = titanic_df['Title'].replace('Ms', 'Miss')
titanic_df['Title'] = titanic_df['Title'].replace('Mme', 'Mrs')

# One-hot encode 'Title' and 'Embarked'
title_dummies = pd.get_dummies(titanic_df['Title'], prefix='Title')
embarked_dummies = pd.get_dummies(titanic_df['Embarked'], prefix='Embarked')

# Concatenate the one-hot encoded features with the original DataFrame
titanic_df = pd.concat([titanic_df, title_dummies, embarked_dummies], axis=1)

# Drop original 'Title' and 'Embarked' columns
titanic_df.drop(['Title', 'Embarked', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Display the updated DataFrame
print(titanic_df.head())

""" Exercise 4: Outlier Detection and Handling
Instructions
Use statistical methods to detect outliers in columns like Fare and Age.
Decide on a strategy to handle the identified outliers, such as capping, transformation, or removal.
Implement the chosen strategy and assess its impact on the dataset.
Hint: Explore methods like IQR (Interquartile Range) and Z-score for outlier detection.


"""

import numpy as np

# Function to detect outliers using IQR
def detect_outliers_iqr(data, column):
    Q1 = np.percentile(data[column], 25)
    Q3 = np.percentile(data[column], 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

# Detect outliers in 'Fare'
fare_outliers = detect_outliers_iqr(titanic_df, 'Fare')
print("Fare Outliers:\n", fare_outliers)

# Detect outliers in 'Age'
age_outliers = detect_outliers_iqr(titanic_df, 'Age')
print("\nAge Outliers:\n", age_outliers)

# Handling outliers (capping example for 'Fare')
upper_bound_fare = np.percentile(titanic_df['Fare'], 95)  #Using 95th percentile as upper bound

titanic_df['Fare'] = np.where(titanic_df['Fare'] > upper_bound_fare, upper_bound_fare, titanic_df['Fare'])

# Verify outlier handling
fare_outliers_after_capping = detect_outliers_iqr(titanic_df, 'Fare')
print("\nFare Outliers after capping:\n", fare_outliers_after_capping)

"""🌟 Exercise 5: Data Standardization and Normalization
Instructions
Assess the scale and distribution of numerical columns in the dataset.
Apply standardization to features with a wide range of values.
Normalize data that requires a bounded range, like [0, 1].
Hint: Consider using StandardScaler and MinMaxScaler from scikit-learn’s preprocessing module.


"""

from sklearn.preprocessing import StandardScaler, MinMaxScaler

numerical_features = ['Age', 'Fare', 'FamilySize']

# Standardization
scaler = StandardScaler()
titanic_df[numerical_features] = scaler.fit_transform(titanic_df[numerical_features])

# Normalization (optional, if needed)
# For example, if you want to normalize 'FamilySize' to be between 0 and 1:
# normalizer = MinMaxScaler()
# titanic_df[['FamilySize']] = normalizer.fit_transform(titanic_df[['FamilySize']])

print(titanic_df.head())

"""
🌟 Exercise 6: Feature Encoding
Instructions
Identify categorical columns in the Titanic dataset, such as Sex and Embarked.
Use one-hot encoding for nominal variables and label encoding for ordinal variables.
Integrate the encoded features back into the main dataset.
Hint: Utilize pandas.get_dummies() for one-hot encoding and LabelEncoder from scikit-learn for label encoding.

"""

import pandas as pd
# One-hot encode 'Sex'
sex_dummies = pd.get_dummies(titanic_df['Sex'], prefix='Sex')
titanic_df = pd.concat([titanic_df, sex_dummies], axis=1)
titanic_df.drop(['Sex'], axis=1, inplace=True)

print(titanic_df.head())

"""
🌟 Exercise 7: Data Transformation for Age Feature
Instructions
Create age groups (bins) from the Age column to categorize passengers into different age categories.
Apply one-hot encoding to the age groups to convert them into binary features.
Hint: Use pd.cut() for binning the Age column and pd.get_dummies() for one-hot encoding.

"""

import pandas as pd
# Create age groups (bins)
bins = [0, 10, 20, 30, 40, 50, 60, 70, float('inf')]  # Adjust bins as needed
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71+']
titanic_df['AgeGroup'] = pd.cut(titanic_df['Age'], bins=bins, labels=labels, right=False)

# One-hot encode the age groups
age_group_dummies = pd.get_dummies(titanic_df['AgeGroup'], prefix='AgeGroup')
titanic_df = pd.concat([titanic_df, age_group_dummies], axis=1)

# Drop the original 'AgeGroup' column and 'Age' column
titanic_df.drop(['AgeGroup', 'Age'], axis=1, inplace=True)

print(titanic_df.head())