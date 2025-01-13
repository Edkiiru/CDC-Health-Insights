# Chronic Disease Risk Stratification Project

## Overview
This project focuses on classifying high-risk individuals for chronic diseases and complications using predictive modeling. By leveraging machine learning techniques, the project aims to provide actionable insights for public health officials and healthcare providers to develop targeted intervention plans.

## Datasets
### Original Dataset
- **File Name:** `U.S._Chronic_Disease_Indicators__CDI_.csv`
- **Size:** 300 MB

### Combined Prediction Dataset
- **File Name:** `combined_predictions_with_categories.csv`
- **Size:** 1.82 MB
- **Description:** NexusMax predictions combined with the original dataset, forming the basis of the risk classification model.

## Problem Statement
- **Objective:** Classify high-risk individuals for chronic diseases and complications.
- **Solution:** Risk stratification using machine learning.
- **Model Type:** ExtraTreesClassifier.
- **Algorithm:** ExtraTreesClassifier.
- **Independent Variables:** `AgeGroup`, `Race/Ethnicity`, `DataValue`, `LocationDesc`.
- **Dependent Variable:** `Risk Classification` (High, Medium, Low).
- **Target Audience:** Public health officials and healthcare providers.

## Key Features and Capabilities
- **Future Capabilities:** Develop targeted intervention plans for high-risk groups.

## Key Performance Indicators (KPIs)
The following KPIs from the Chronic Disease Indicators (CDI) dataset are essential to predict future hospitalization rates for chronic diseases:

1. **Percentage of High-Risk Individuals by Age Group**
   - **Importance:** Identifies which age groups have the highest concentration of high-risk individuals.
   - **Calculation:**  
     ```
     (Number of high-risk individuals in an age group / Total number of individuals in that age group) * 100
     ```

2. **Risk Classification Distribution (High, Medium, Low)**
   - **Importance:** Provides an overall view of population stratification.
   - **Visualization:** Stacked bar chart or pie chart showing high, medium, and low-risk percentage distribution.

3. **Top Locations with High-Risk Individuals**
   - **Importance:** Identifies geographic areas with the highest prevalence of high-risk individuals.
   - **Visualization:** Map or bar chart highlighting regions with the highest concentration of high-risk individuals.

4. **Risk Classification by Race/Ethnicity**
   - **Importance:** Identifies disparities in chronic disease risk among racial/ethnic groups.
   - **Calculation:** Breakdown of risk classification (High, Medium, Low) by race/ethnicity groups.

5. **Intervention Effectiveness Potential (Projected Impact)**
   - **Importance:** Measures the potential impact of targeted interventions on high-risk groups.
   - **Visualization:** Scenario analysis showing how different interventions could shift the risk profile.

## Process and Challenges
- **Model Development:**
  - Initially created using a partial dataset of 5,000 records.
  - Successfully scaled to a full dataset of approximately 1 million records.
  
- **Challenges:**
  - The resulting prediction dataset was split into 7 files due to size constraints.
  - Merging the prediction results with the original dataset has been challenging due to file size.

- **Current Work:**
  - Merging predictive results into a single dataset.
  - Merging the combined dataset with the original dataset for comprehensive reporting and insights.

## Reporting
- Insights will include:
  - Trends in chronic disease risks.
  - Identification of high-risk demographics and regions.
  - Projections on the effectiveness of targeted interventions.

---

## Future Work
- Optimize the model for better scalability.
- Improve reporting to provide more granular insights.
- Develop intervention simulations to guide public health strategies.

---

## Visuals
Example visualizations and screenshots are included for reference:
- **Zoom Image:** `Zoom Screenshot 2024-09-05 053221.png`
- **Sample Prediction Report:** Derived from partial prediction datasets.

---

## Contact
For questions or contributions, please reach out.
- **Email:** [Kiirued@gmail.com](mailto:Kiirued@gmail.com)
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com)
