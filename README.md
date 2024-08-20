<<<<<<< HEAD
# A Kenyan used Car Price Prediction Model

A Machine Learning Model that gives users  accurate price predictions on used motor vehicles in Kenya  which helps users either budget to  purchase  one or evaluate user's vehicles giving them  accurate prices according to their vehicle features 
<p>
<img src="https://github.com/user-attachments/assets/4503cb71-f2af-45f2-90d7-e83cd954ea4d"/>
=======
# A Used Car Price Prediction Project

A Machine Learning Model that gives users  accurate used car price predictions  based of the vehicle features
<p>

![Red and Black Modern Car Service Poster](https://github.com/user-attachments/assets/382e85c2-6bf7-4a2a-b2f0-a3fc34895693)


## Project Overview
The Kenyan used car market, once dominated by new vehicles, experienced a significant shift in the 1990s due to economic liberalization, leading to an influx of used cars, primarily from Japan. Today, used cars account for about 80% of vehicle sales in Kenya, driven by their affordability. 

Accurately estimating used car prices in Kenya is challenging due to variables like age, mileage, and vehicle condition. This project aims to develop a machine learning model to predict used car prices, offering a reliable, data-driven tool for buyers, sellers, and businesses in the Kenyan market.

## Problem Statement
The lack of a dependable, data-driven methodS for predicting used car prices in the Kenya market leading to inefficiencies , uncertainties, mispricing, financial losses and reduced trust in the market.

## Objectives
-
**Main Objective:**

To develop a machine learning model to accurately predict used car prices in Kenya based on various vehicle features.

**Specific Objectives:**

To Identify key vehicle features impacting price.

To determine the most popular car brands in the Kenyan market.

To analyze the most common features in the dataset.

## **Success Criteria**
Achieving an R-squared value of 0.8, indicating the model explains 80% of the variance in the target variable.

Maintaining a low Mean Absolute Error (MAE),which  reflecting a minimal average prediction error.

## Constraints
- Limited availability of Kenyan-specific data for effective model training.
---
## Project data

The dataset has 6,019 entries sourced from local car bazars and showrooms,containig vehiclles manufactured up to 2017, with details on vehicle name, year, mileage, fuel type, transmission, engine, power,seats and price. This dataset forms the basis for our predictive model and offers insights into the Kenyan used car market.

---
## Modelling and Evaluation

Models used and their metrics score

| Model                  | R-Squared | MAE score   |
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
---
## Modules used

![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![matplotib](https://img.shields.io/badge/matplotib-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=blue)
![seaborn](https://img.shields.io/badge/seaborn-D00000?style=for-the-badge&logo=keras&logoColor=white)
![GridsearchCV](https://img.shields.io/badge/gridsearchcv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=black)
![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=pink)
![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
---

## App

Welcome to our user friendly [app](https://carprice-prediction-dxogxazajkxpll3hllugmn.streamlit.app/)

**App setup Instructions**

* Install the required packages using pip:

    ```
    pip install -r requirements.txt
    ```

* Install Streamlit:

    ```
    pip install streamlit
    ```

* To run the app locally run the following on terminal:
    ```
    streamlit run deployment/app.py
---
## Team Members

* [Kevin Mwaura](https://github.com/TyrionCodister)
* [Jackson Munene](https://github.com/jakkkc)
* [Gerald Mwangi](https://github.com/Geraldkigotho)
* [Marion Achieng](https://github.com/marionrion)
* [Benedict Kuloba](https://github.com/myles-G)

>>>>>>> f192cf8146f75157f7b673c2d8eeba4127b6444f
