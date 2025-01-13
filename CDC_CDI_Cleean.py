import pandas as pd

# Load the dataset
file_path = 'C:/Users/edkii/OneDrive/Data Science/PowerBI/Chronic_Disease/U.S._Chronic_Disease_Indicators__CDI_.csv'  # Update the path if necessary
data = pd.read_csv(file_path, low_memory=False)

# Display dataset information and initial structure
print("Dataset Info:")
print(data.info())
print("\nPreview of the dataset:")
print(data.head())

# Handle missing values - decide how to treat them (drop or fill)
print("\nChecking missing values:")
print(data.isnull().sum())

# Dropping columns with too many missing values (example: >50% missing)
threshold = len(data) * 0.5
data = data.dropna(axis=1, thresh=threshold)

# Fill missing values in numeric columns with median, and categorical columns with mode
for column in data.columns:
    if data[column].dtype in ['float64', 'int64']:
        data[column].fillna(data[column].median(), inplace=True)
    elif data[column].dtype == 'object':
        data[column].fillna(data[column].mode()[0], inplace=True)

# Ensure consistent data types for columns with mixed types
for column in data.columns:
    if data[column].dtype == 'object':  # Check for numeric-like columns stored as objects
        try:
            data[column] = pd.to_numeric(data[column], errors='coerce')
        except:
            continue

# Remove duplicates if present
data = data.drop_duplicates()

# Save the cleaned dataset to a new file
cleaned_file_path = 'Cleaned_Chronic_Disease_Indicators.csv'
data.to_csv(cleaned_file_path, index=False)

# Display preview of cleaned data
print("\nCleaned Dataset Info:")
print(data.info())
print("\nPreview of the cleaned dataset:")
print(data.head())

print(f"\nCleaned dataset saved as: {cleaned_file_path}")
