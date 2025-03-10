# Diabetes Prediction and Recommendation System

## Overview
This project focuses on predicting diabetes using machine learning techniques and providing health recommendations based on the predictions. The system utilizes an **Random Forest model** for accurate diabetes classification and integrates a **streamlit-based web application** for user interaction.

## Dataset
- **Source:** CDC's Behavioral Risk Factor Surveillance System (BRFSS) 2015 dataset
- **Total Records:** 253,680 survey responses
- **Features:** 21 health-related variables
- **Target Variable:** `Diabetes_012`
  - `0`: No Diabetes
  - `1`: Diabetes
## Features and Workflow
1. **Exploratory Data Analysis (EDA)**
   - Data cleaning, visualization, and feature engineering
2. **Data Preprocessing**
   - Handling missing values, encoding categorical variables, feature scaling
3. **Feature Selection**
   - Identifying key variables impacting diabetes prediction
4. **Model Training & Evaluation**
   - Models used: **Random Forest, KNN, CatBoost, XGBoost**
   - Metrics: Accuracy, Precision, Recall, F1-score
5. **Web Application (Streamlit)**
   - User inputs health parameters
   - Model predicts diabetes risk
   - Recommends dietary and lifestyle changes

## Technologies Used
- **Programming Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn,Streamlit
- **Big Data Technologies:** PySpark (for data processing)
- **Deployment:** Streamlit UI

## Usage
- Enter health-related parameters in the web application.
- The model will predict the likelihood of diabetes.
- If at risk, personalized recommendations will be displayed.

## Results

![image alt](https://github.com/adityaawati45/Diabetes-Health-Prediction-System/blob/18778dc5363bc79967baf14cd86902bf49084307/WhatsApp%20Image%202025-02-11%20at%203.45.34%20AM.jpeg)

![image alt](https://github.com/adityaawati45/Diabetes-Health-Prediction-System/blob/95bea9811564bc30e5e2f95b9d9f8c6d3d3e4e0f/WhatsApp%20Image%202025-02-11%20at%2012.09.51%20PM.jpeg)


