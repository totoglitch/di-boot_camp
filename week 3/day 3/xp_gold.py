# -*- coding: utf-8 -*-
"""xp gold

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u3s7RuPUBbwGqW6PmNfWCwPsqoLOV9M4

Exercise 1: Data Scaling and Normalization
Instructions
Identify numerical columns in the dataset like ‘Fare’ and ‘Age’.
Apply standardization (Z-score scaling) to features with a Gaussian distribution.
Apply Min-Max normalization to features that require bounded ranges.
Analyze the effect of scaling and normalization on model performance.
Hint: Use StandardScaler and MinMaxScaler from scikit-learn.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # Example model

# Assuming your data is in a pandas DataFrame called 'df'
# and you have already loaded it.

# 1. Identify numerical columns
numerical_cols = ['Fare', 'Age']  # Replace with actual numerical column names

# 2. Separate features and target variable (if applicable)
X = df[numerical_cols]
y = df['Survived']  # Replace 'Survived' with your target variable column

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 4. Apply Standardization (Z-score scaling) to 'Fare' (assuming Gaussian distribution)
scaler_standard = StandardScaler()
X_train['Fare_scaled'] = scaler_standard.fit_transform(X_train[['Fare']])
X_test['Fare_scaled'] = scaler_standard.transform(X_test[['Fare']])

# 5. Apply Min-Max normalization to 'Age' (bounded range)
scaler_minmax = MinMaxScaler()
X_train['Age_scaled'] = scaler_minmax.fit_transform(X_train[['Age']])
X_test['Age_scaled'] = scaler_minmax.transform(X_test[['Age']])

# 6. Drop original columns and use the scaled columns for training
X_train = X_train.drop(['Fare', 'Age'], axis=1)
X_test = X_test.drop(['Fare', 'Age'], axis=1)

# 7. Model training and evaluation (example with Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"Accuracy after scaling and normalization: {accuracy}")

# Alternatively, you could perform cross-validation here for more robust evaluation

"""Exercise 2: Creating Composite Features
Instructions
Create a new feature, ‘Family Size’, by combining ‘SibSp’ (siblings and spouses) and ‘Parch’ (parents and children).
Create a ‘IsAlone’ feature to indicate whether a passenger is traveling alone.
Explore the relationship between these new features and the survival rate.
Hint: Use basic arithmetic operations and conditional statements in Pandas.


"""

# 1. Create 'FamilySize' feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # Add 1 to include the passenger themselves

# 2. Create 'IsAlone' feature
df['IsAlone'] = 0
df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1

# 3. Explore the relationship between new features and survival rate
# Example: Group by 'FamilySize' and calculate survival rate
survival_rate_by_family_size = df.groupby('FamilySize')['Survived'].mean()
print(survival_rate_by_family_size)

# Example: Group by 'IsAlone' and calculate survival rate
survival_rate_by_alone = df.groupby('IsAlone')['Survived'].mean()
print(survival_rate_by_alone)

# Further analysis: You can visualize these relationships using bar plots or other visualizations
# to gain more insights into the impact of family size and alone status on survival.

# Example Visualization (requires matplotlib)
import matplotlib.pyplot as plt
survival_rate_by_family_size.plot(kind='bar')
plt.title('Survival Rate by Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')
plt.show()


survival_rate_by_alone.plot(kind='bar')
plt.title('Survival Rate by Alone Status')
plt.xlabel('Is Alone')  # 0 for not alone, 1 for alone
plt.ylabel('Survival Rate')
plt.show()

"""
Exercise 3: Data Normalization on the Titanic Dataset
Instructions
Import the titanic dataset using Pandas in Python.
Apply Min-Max normalization and Z-score normalization to these columns : Age and Fare
Compare the distributions before and after normalization using histograms.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# Load the Titanic dataset (replace 'titanic.csv' with your actual file path)
try:
    df = pd.read_csv('titanic.csv')
except FileNotFoundError:
    print("Error: 'titanic.csv' not found. Please make sure the file is in the current directory or provide the correct path.")
    exit()


# Select the 'Age' and 'Fare' columns
numerical_cols = ['Age', 'Fare']
df_numerical = df[numerical_cols].copy()  # Create a copy to avoid SettingWithCopyWarning


# Handle missing values (replace with mean for simplicity)
df_numerical['Age'].fillna(df_numerical['Age'].mean(), inplace=True)
df_numerical['Fare'].fillna(df_numerical['Fare'].mean(), inplace=True)


# Apply Min-Max normalization
min_max_scaler = MinMaxScaler()
df_numerical_minmax = min_max_scaler.fit_transform(df_numerical)
df_numerical_minmax = pd.DataFrame(df_numerical_minmax, columns=['Age_minmax', 'Fare_minmax'])


# Apply Z-score normalization
standard_scaler = StandardScaler()
df_numerical_standard = standard_scaler.fit_transform(df_numerical)
df_numerical_standard = pd.DataFrame(df_numerical_standard, columns=['Age_standard', 'Fare_standard'])

# Combine all data for plotting
df_normalized = pd.concat([df_numerical, df_numerical_minmax, df_numerical_standard], axis=1)

# Create histograms
for col in ['Age', 'Fare', 'Age_minmax', 'Fare_minmax', 'Age_standard', 'Fare_standard']:
    plt.figure()  # Create a new figure for each histogram
    plt.hist(df_normalized[col], bins=30)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

"""Exercise 4 : Data Reduction and Aggregation
Instructions
Perform data reduction on the titanic dataset by implementing dimensionality reduction techniques like Principal Component Analysis (PCA).
Aggregate the data by a categorical column (like date or region) and calculate summary statistics (mean, sum, etc.).
Visualize the aggregated data using appropriate plots.

"""

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('titanic.csv')
except FileNotFoundError:
    print("Error: 'titanic.csv' not found. Please make sure the file is in the current directory or provide the correct path.")
    exit()

# Data Reduction using PCA
# Select numerical features for PCA
numerical_features = ['Age', 'Fare', 'SibSp', 'Parch']
X_numerical = df[numerical_features].copy()

# Handle missing values (replace with the mean for simplicity)
X_numerical.fillna(X_numerical.mean(), inplace=True)

# Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
principal_components = pca.fit_transform(X_numerical)
df['PC1'] = principal_components[:, 0]
df['PC2'] = principal_components[:, 1]


# Data Aggregation
# Example aggregation: Calculate the mean survival rate and mean fare for each passenger class
aggregation_results = df.groupby('Pclass').agg({'Survived': 'mean', 'Fare': 'mean'})

# Print the aggregated results
print(aggregation_results)


# Visualization
# Scatter plot of principal components colored by survival
plt.figure(figsize=(8, 6))
plt.scatter(df['PC1'], df['PC2'], c=df['Survived'], cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Titanic Dataset Colored by Survival')
plt.colorbar(label='Survived')
plt.show()

# Bar plot of aggregated data
plt.figure(figsize=(8, 6))
aggregation_results['Survived'].plot(kind='bar')
plt.xlabel('Passenger Class')
plt.ylabel('Mean Survival Rate')
plt.title('Mean Survival Rate by Passenger Class')
plt.show()

"""Exercise 5: Normalizing E-Commerce Sales Data
Instructions
Dataset: Use the Superstore Sales Data.

Load the Superstore Sales dataset.
Perform Min-Max normalization on the ‘Sales’ and ‘Profit’ columns.
Create new columns, e.g., ‘Sales_normalized’ and ‘Profit_normalized’, to store the normalized values.

"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

try:
    df = pd.read_csv('superstore_sales.csv')
except FileNotFoundError:
    print("Error: 'superstore_sales.csv' not found. Please make sure the file is in the current directory or provide the correct path.")
    exit()

# Select the 'Sales' and 'Profit' columns
numerical_cols = ['Sales', 'Profit']
df_numerical = df[numerical_cols].copy()

# Handle missing values (if any) - replace with 0 for demonstration
df_numerical.fillna(0, inplace=True)

# Apply Min-Max normalization
min_max_scaler = MinMaxScaler()
df_numerical_minmax = min_max_scaler.fit_transform(df_numerical)

# Create new columns for normalized values
df['Sales_normalized'] = df_numerical_minmax[:, 0]
df['Profit_normalized'] = df_numerical_minmax[:, 1]

# Display the first few rows to verify the new columns
print(df.head())

"""Exercise 6: Aggregating Air Quality Data
Instructions
Dataset: Use the Air Quality Data in India.

Load the Air Quality dataset.
Convert the ‘Date’ column to a datetime format.
Group the data by location and month, calculating the average of key measurements (e.g., PM2.5, PM10, NO2) for each month.
Store the aggregated data in a new DataFrame and analyze trends in air quality over time.

"""

import pandas as pd

try:
    df = pd.read_csv('air_quality_data.csv')
except FileNotFoundError:
    print("Error: 'air_quality_data.csv' not found. Please make sure the file is in the current directory or provide the correct path.")
    exit()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract month and year
df['Month'] = df['Date'].dt.month

# Group data by location and month, calculate mean of relevant columns
aggregated_data = df.groupby(['Location', 'Month'])[['PM2.5', 'PM10', 'NO2']].mean().reset_index()

# Display the aggregated data
aggregated_data

# Further analysis and visualization
# ...