# A Used Car Price Prediction Project

A Machine Learning Model that gives users  accurate used car price predictions  based on the vehicle features
<p>

![Red and Black Modern Car Service Poster 4](https://github.com/user-attachments/assets/121ebc40-8d71-4fa5-bf20-2ae010cf6e09)

## Project Overview
The Kenyan used car market, once dominated by new vehicles, experienced a significant shift in the 1990s due to economic liberalization, leading to an influx of used cars, primarily from Japan. Today, used cars account for about 80% of vehicle sales in Kenya, driven by their affordability. 

Accurately estimating used car prices in Kenya is challenging due to variables like age, mileage, and vehicle condition. This project aims to develop a machine learning model to predict used car prices, offering a reliable, data-driven tool for buyers, sellers, and businesses in the Kenyan market.

## Problem Statement
The lack of a dependable, data-driven method for predicting used car prices in the Kenya market leads to inefficiencies, uncertainties, mispricing, financial losses and reduced trust in the market.

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

We are maintaining a low Mean Absolute Error (MAE), which  reflects a minimal average prediction error.

## Constraints
- Limited availability of Kenyan-specific data for effective model training.
---
## Project data

The dataset has 6,019 entries sourced from local car bazaars and showrooms, containing vehicles manufactured up to 2017, with details on vehicle name, year, mileage, fuel type, transmission, engine, power, seats, and price. This dataset forms the basis for our predictive model and offers insights into the Kenyan used car market.

---
## Modelling and Evaluation

Models used and their metrics score

|MODEL	           |R SQUARED	    |MAE              |	
|------------------|----------------|-----------------|
|Catboost regression |	0.87        |  298328.91      |
|XGBoost regression  |	0.86        |  302261.48	  |
|Random regression  |    0.85       |  315234.6	  |	     
|Knn regression	   |    0.84       |  337761.66	  |	    	     
|Lasso regression  |    0.63        |  5492235.34      |         
|Ridge regression   |    0.62       |  550384.84      |         
|ElasticNet         |     0.29      |   678576.8              |
|Linear regression   |    -2.37     |    3632345302271830.06             |

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

Welcome to our user-friendly app

**App setup Instructions**

* Install the required packages using pip:

    ```
    pip install -r requirements.txt
    ```

* Install Streamlit:

    ```
    pip install streamlit
    ```

* To run the app locally run the following on the terminal:
    ```
    streamlit run app.py
---
## Team Members

* [Kevin Mwaura](https://github.com/TyrionCodister)
* [Jackson Munene](https://github.com/jakkkc)
* [Gerald Mwangi](https://github.com/Geraldkigotho)
* [Marion Achieng](https://github.com/marionrion)
* [Benedict Kuloba](https://github.com/myles-G)


