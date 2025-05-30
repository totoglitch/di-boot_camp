# -*- coding: utf-8 -*-
"""xp ninja

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aipxepB_KX3g2r5jMl5fXkGK3RyppD7c

Exercise 1: Advanced Data Cleaning and Feature Engineering
Instructions
Dataset: Use the New York City Airbnb Open Data.

Load the NYC Airbnb dataset.
Identify and handle missing values in multiple columns using advanced imputation techniques.
Detect and treat outliers in key columns like ‘price’ and ‘number_of_reviews’.
Create new features based on existing data, such as ‘booking_rate’ (number of reviews divided by availability) and ‘price_per_person’ (price divided by the number of accommodated guests).
Perform exploratory data analysis to understand correlations between newly created features and the target variable.
Hint: For advanced data cleaning techniques, refer to this article on Data Cleaning.
"""

import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor


try:
    df = pd.read_csv('your_file.csv')
except FileNotFoundError:
    print("Error: 'your_file.csv' not found. Please provide the correct file path.")
    exit()


# Handle missing values using IterativeImputer for numerical columns
numerical_cols = ['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
imputer = IterativeImputer(estimator=RandomForestRegressor(), max_iter=10, random_state=0)
df[numerical_cols] = imputer.fit_transform(df[numerical_cols])


# Treat outliers in 'price' and 'number_of_reviews' using IQR method
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

df = remove_outliers(df, 'price')
df = remove_outliers(df, 'number_of_reviews')


# Create new features: booking_rate and price_per_person
df['booking_rate'] = df['number_of_reviews'] / df['availability_365']
df['price_per_person'] = df['price'] / df['accommodates']


# Handle potential errors in new feature calculations
df['booking_rate'].replace([np.inf, -np.inf], np.nan, inplace=True)
df['price_per_person'].replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0,inplace=True)


# Perform exploratory data analysis (EDA)
# Example: Correlation between 'price_per_person' and 'price'
correlation = df['price_per_person'].corr(df['price'])
print(f"Correlation between price_per_person and price: {correlation}")

# More EDA can be done, such as plotting distributions and relationships between other features
# ... your code for more EDA ...

print(df.head())

"""Exercise 2: Complex Data Integration and Transformation
Instructions
Datasets: World Happiness Report and Global Health and Population Statistics

Load both datasets.
Perform data integration by merging the two datasets on the ‘Country’ column.
Transform the integrated dataset by normalizing numerical columns like ‘GDP per Capita’ and ‘Life Expectancy’.
Apply PCA for dimensionality reduction while preserving significant information.
Conduct a comparative analysis pre- and post-transformation to evaluate the impact of these processes on the data.
Hint: For guidance on data integration and transformation, check out this article on Data Transformation.


"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

try:
    happiness_df = pd.read_csv('world_happiness_report.csv')
    health_df = pd.read_csv('global_health_statistics.csv')
except FileNotFoundError:
    print("Error: One or both CSV files not found. Please provide the correct file paths.")
    exit()


# Data Integration (Merge datasets)
merged_df = pd.merge(happiness_df, health_df, on='Country', how='inner')


# Data Transformation (Normalization)
numerical_cols_to_normalize = ['GDP per Capita', 'Life Expectancy', 'Healthy Life Expectancy'] # Add other relevant columns

scaler = MinMaxScaler()
merged_df[numerical_cols_to_normalize] = scaler.fit_transform(merged_df[numerical_cols_to_normalize])


# Dimensionality Reduction (PCA)
pca = PCA(n_components=0.95)  # Preserve 95% of variance
pca_result = pca.fit_transform(merged_df[numerical_cols_to_normalize])
pca_df = pd.DataFrame(data=pca_result, columns=[f'PC{i+1}' for i in range(pca_result.shape[1])])

# Concatenate PCA results with original DataFrame
merged_df = pd.concat([merged_df, pca_df], axis=1)


# Comparative Analysis (Pre and Post Transformation)
print("Original Data (head):")
print(merged_df.head())
print("-" * 50)

# Example of comparison: Statistics of GDP per capita before and after normalization
print("Statistics of 'GDP per Capita':")
print("Before Normalization:")
print(merged_df['GDP per Capita'].describe())
print("After Normalization:")
print(merged_df['GDP per Capita'].describe())

# More comparative analysis can be performed
# ... your code for more comparative analysis ...

print(merged_df.head())

"""Exercise 3 : Exploring Dimensionality Reduction Techniques
Instructions
Read this article : A Complete Guide On Dimensionality Reduction
Import this dataset : Shop Customer Data
Implement Principal Component Analysis (PCA) and observe how much variance is retained with different numbers of components.
Apply at least one more dimensionality reduction technique (like t-SNE or LDA) and compare its results with PCA.
Visualize the results of these techniques using plots.
Write a brief analysis of how dimensionality reduction impacted the dataset and the insights you gained from the visualizations.

"""

import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('Shop_Customer_Data.csv')
except FileNotFoundError:
    print("Error: 'Shop_Customer_Data.csv' not found. Please provide the correct file path.")
    exit()

# Separate features and target variable (assuming 'CustomerID' is not a feature)
X = df.drop('CustomerID', axis=1)

# Apply PCA
pca = PCA()
pca.fit(X)

# Explained variance ratio for each component
explained_variance_ratio = pca.explained_variance_ratio_

# Cumulative explained variance
cumulative_variance = np.cumsum(explained_variance_ratio)

# Plot explained variance ratio
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance by PCA Components')
plt.grid(True)
plt.show()

# Apply PCA with 2 components for visualization
pca_2 = PCA(n_components=2)
X_pca = pca_2.fit_transform(X)

# Apply t-SNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# Visualize PCA results
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Dimensionality Reduction')
plt.show()

# Visualize t-SNE results
plt.figure(figsize=(8, 6))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE Dimensionality Reduction')
plt.show()

# Analysis
print("Analysis of Dimensionality Reduction:")
# Discuss the explained variance plot (elbow point suggests optimal # of components for PCA).
# Compare the visualizations of PCA and t-SNE, noting the different clustering/separation patterns.
# Discuss how dimensionality reduction impacted the data (loss of information vs. improved visualization).
# Discuss any insights gained about customer segmentation based on the visualization.