# **Car Price Prediction Project**

## **/Overview/**
The Kenyan used car market, once dominated by new vehicles, experienced a significant shift in the 1990s due to economic liberalization, leading to an influx of used cars, primarily from Japan. Today, used cars account for about 80% of vehicle sales in Kenya, driven by their affordability. 

Accurately estimating used car prices in Kenya is challenging due to variables like age, mileage, and vehicle condition. This project aims to develop a machine learning model to predict used car prices, offering a reliable, data-driven tool for buyers, sellers, and businesses in the Kenyan market.

## **/Problem/ Statement/**
The lack of a dependable, data-driven method for predicting used car prices in Kenya leads to inefficiencies and uncertainties. Mispricing can result in financial losses and reduced trust in the market.

## **/Objectives/**
- **/Main Objective/:** Develop a machine learning model to accurately predict used car prices in Kenya based on various vehicle features.
- **/Specific Objectives/:**
  - Identify key vehicle features impacting price.
  - Determine the most popular car brands in the Kenyan market.
  - Analyze the most common features in the dataset.

## **/Success/ Criteria/**
- Achieve an R-squared value of 0.8, indicating the model explains 80% of the variance in the target variable.
- Maintain a low Mean Absolute Error (MAE), reflecting minimal average prediction error.

## **/Constraints/**
- Limited availability of Kenyan-specific data for effective model training.

## **/Data/ Understanding/**
The dataset includes 6,019 entries from Nairobi car bazaars and showrooms up to 2021, with details on vehicle name, year, mileage, fuel type, transmission, and price. This dataset forms the basis for our predictive model and offers insights into the Kenyan used car market.

---
Certainly! Here’s a more concise version:

---

## **/Exploratory/ Data/ Analysis/ (EDA)**

Next, we perform Exploratory Data Analysis (EDA) to gain insights from the dataset through univariate and bivariate analysis.

### **/Univariate/ Analysis/**
![image](https://github.com/user-attachments/assets/434e4d1c-f817-461d-8259-44b988d0340f)

![image](https://github.com/user-attachments/assets/d0b021e0-9590-4b26-9723-441c1d9707de)

![image](https://github.com/user-attachments/assets/ebaf9176-f552-4c23-8605-d74d3f9f1221)

![image](https://github.com/user-attachments/assets/a0c8bb1b-3427-4ce2-8cf9-eb0a780e8c33)

![image](https://github.com/user-attachments/assets/f18ab235-6081-423a-83be-bf6d616ee1e3)

![image](https://github.com/user-attachments/assets/00c90895-9b87-47ba-a9d0-fbe895e65ee1)

![image](https://github.com/user-attachments/assets/7f9d5523-641c-4801-a801-be4c15f64174)

![image](https://github.com/user-attachments/assets/67268104-decf-42eb-8083-81fd2251d26f)

![image](https://github.com/user-attachments/assets/0f83a326-9d7e-4cb5-8c5c-724e629f0e22)
## **/Observations/**

- **Engine Capacity:** Most vehicles are between **1000 to 2000 cc**.
- **Power:** Most vehicles have **< 100 brake horsepower**.
- **Car Price:** Price distribution is **non-normal**.
- **Transmission:** Majority are **manual**.
- **Fuel Type:** **Diesel** cars are most common.
- **Usage:** Most are **foreign used**.
- **Age:** Most cars are **5 to 15 years old**.

---
### **/Bivariate/ Analysis/**
![image](https://github.com/user-attachments/assets/4ba0c00e-53b8-4296-b0fc-2077fdc2cad2)

![image](https://github.com/user-attachments/assets/bbddd3d7-bdf9-451b-a48f-1103bd5a99e6)

![image](https://github.com/user-attachments/assets/5a2c4745-268e-49a0-977c-9a8c451b5207)

![image](https://github.com/user-attachments/assets/b7ed8da6-d11f-4022-b0e0-b3a202733048)

![image](https://github.com/user-attachments/assets/91808429-ae9e-40fc-9db3-7e85992c489d)

## **/Observations/**

- **Correlation Overview:** Engine size, power, and car price are all positively correlated, forming a cluster of related variables.
- **Strongest Relationship:** Engine size and power have a strong positive correlation of **0.86**, reflecting their mechanical connection.
- **Price Influence:** Car prices are influenced by both power and engine size, with power having a slightly stronger correlation.
- **Multicollinearity:** The high correlation of **0.86** between engine size and power indicates significant multicollinearity. Advanced regression techniques such as ridge regression and polynomial regression will be employed to address this issue.
---
## **/Model/ Evaluation/ and/ Selection/**

**Top Performers:** XGBoost, CatBoost Regressor, RandomForest Regressor, and KNN Regressor. **RandomForest Regressor** stands out with the best performance, showing the lowest MAE. We will focus on fine-tuning it with GridSearch.

**SVR** was the least effective and will not be further optimized.

### **/Evaluation/ Metrics/**
- **R-Squared (R²):** Measures overall trend capture.
- **Mean Absolute Error (MAE):** Indicates average prediction error, less affected by outliers.

### **/Model/ Performance/**

| Model                  | R-Squared | MAE         |
|------------------------|-----------|-------------|
| Linear Regression     | 0.58      | 653,141.09  |
| Ridge Regression       | 0.73      | 435,767.83  |
| Lasso Regression       | 0.78      | 408,372.36  |
| Elastic Net            | 0.41      | 626,174.62  |
| Random Forest          | 0.86      | 287,296.62  |
| KNN Regressor          | 0.81      | 345,368.21  |
| XGBoost                | 0.88      | 296,930.22  |
| CatBoost               | 0.88      | 311,516.22  |
| SVR                    | -0.11     | 1,001,403.48|
| Tuned RandomForest     | 0.86      | 307,417.55  |

### **/Best/ Model/**

**RandomForest Regressor** is chosen for deployment due to:
- **Highest R² Score:** 0.88
- **Lowest MAE:** 287,296.62
- **Consistent Performance:** R² values from 0.81 to 0.91

---


# A Kenyan used Car Price Prediction Model

A Machine Learning Model that gives users  accurate price predictions on used motor vehicles in Kenya  which helps users either budget to  purchase  one or evaluate user's vehicles giving them  accurate prices according to their vehicle features 
<p>
<img src="https://github.com/user-attachments/assets/4503cb71-f2af-45f2-90d7-e83cd954ea4d"/>
