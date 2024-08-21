import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the trained model, OHE, and scaler
with open('Catboost.pkl', 'rb') as file:
    model = pickle.load(file)

with open('ohe.pkl', 'rb') as file:
    ohe = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Load the cleaned data for model's unique values
@st.cache_data
def load_data():
    return pd.read_pickle('cleaned_df.pkl')

cleaned_df = load_data()
brand_list = sorted(cleaned_df.Brand.unique())

# Set up the sidebar for navigation
st.sidebar.image("company logo.png", width=200)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict Price", "About", "Meet the Team", "Feedback"])

# Set the title of the app
st.title("Car Price Prediction App")

# Display the main content based on selected page
if page == "Predict Price":
    st.header("Predict the Price of a Car")

    # Input fields for user input
    Brand = st.selectbox("Car Brand", brand_list)
    Year = st.slider("Year of Manufacture", 1990, 2024, 2015)
    Mileage = st.slider("Mileage", 0, 300000, 50000)
    Fuel_Type = st.selectbox("Fuel Type", ("Petrol", "Diesel", "CNG"))
    Transmission = st.selectbox("Transmission", ("Manual", "Automatic"))
    Use = st.selectbox("Use", ("Foreign", "Local"))
    Engine = st.slider("Engine Capacity (cc)", 800, 5000, 1500)
    Seats = st.slider("Seats", 2, 7, 5)

    # Predict button
    if st.button("Predict Price"):
        # Prepare the input features
        features = {
            "Brand": Brand,
            "Fuel_Type": Fuel_Type,
            "Transmission": Transmission,
            "Use": Use,
            "Year": Year,
            "Mileage": Mileage,
            "Engine": Engine,
            "Seats": Seats
        }

        # Create a DataFrame from features
        features_df = pd.DataFrame([features])
        st.write(features_df)

        # Separate the categorical and numerical columns
        categorical_features = ['Fuel_Type', 'Transmission', 'Use', 'Brand']
        numerical_features = ["Year", "Mileage", "Engine", "Seats"]

        # Extract categorical and numerical data
        categorical_data = features_df[categorical_features]
        numerical_data = features_df[numerical_features]

        # Apply the OneHotEncoder
        encoded_categorical_data = ohe.transform(categorical_data)
        X_test_ohe_dense = encoded_categorical_data.toarray()
        X_test_cat_df = pd.DataFrame(X_test_ohe_dense, columns=ohe.get_feature_names_out(categorical_features))

        # Apply the StandardScaler to numerical features
        scaled_numerical_data = scaler.transform(numerical_data)
        X_test_num_df = pd.DataFrame(scaled_numerical_data, columns=numerical_features)

        # Combine encoded categorical features with scaled numerical features
        processed_features = pd.concat([X_test_cat_df, X_test_num_df], axis=1)

        # Predict the car price
        price = model.predict(processed_features)
        st.success(f"Estimated Price for {Brand}: Ksh{price}")


elif page == "Home":
    st.header("Welcome to the Car Price Prediction App")
    st.markdown("""
    **How to Use the App**:
    
    - **Step 1**: Navigate to the 'Predict Price' page using the sidebar.
    
    - **Step 2**: On the 'Predict Price' page, you'll find sliders and dropdowns for different car features.
    
    - **Step 3**: Use the dropdowns to select the car's **Brand**, **Fuel Type**, **Transmission**, and **Use** (whether the car is Foreign or Local).
    
    - **Step 4**: Adjust the sliders to set the **Year of Manufacture**, **Mileage** (Kilometers Driven), **Engine Capacity** (cc), **Horse Power** (bhp), and the number of **Seats**.
    
    - **Step 5**: Once you've set all the features according to your car's specifications, click the "Predict Price" button.
    
    - **Step 6**: The app will instantly generate an estimated price for your car based on the input features.

    """)
   

elif page == "About":
    st.header("About Neural Gearbox")
    st.markdown("""
    **Mission Statement**: Guiding Kenyans to confidently navigate the used car market with ease.
    
    **Vision**: To be the trusted name in Kenya for car price predictions, ensuring fair and transparent deals.
    ### Contact Information
    For support or inquiries, please reach out to [kelvin.mwaura.edu@gmail.com](mailto:kelvin.mwaura.edu@gmail.com).

    ### Future Work
    We plan to:
    - Incorporate additional features to refine predictions.
    
    - Expand the model to cover other East African markets.
    """)

elif page == "Meet the Team":
    st.header("Meet the Team")

    # Add the animated icon (GIF) at the top
    st.image('customer.gif', width=150)
    
    st.subheader("Marion Achieng - Data Narrative Architect")
    st.markdown("""
   Marion excels at distilling complex business needs into clear, strategic overviews. Her expertise lies in crafting concise, data narratives that align  business goals with actionable insights, ensuring every stakeholder is on the same page.
    - **LinkedIn**: [Marion Achieng](https://www.linkedin.com/in/marion-achieng-0747712a3/)
    - **GitHub**: [marionrion](https://github.com/marionrion)
    - **Email**: [marionachieng@gmail.com](mailto:marionachieng@gmail.com)
    """)
    
    st.subheader("Benedict Kuloba - Data Visualisation Maestro")
    st.image('Benedict.jpeg', width=150)
    st.markdown("""
    Benedict is our data visualization virtuoso translating complex datasets into visually compelling dashboards and reports, making complex insights intuitive and easy to act on.
    - **LinkedIn**: [Benedict Kuloba](https://www.linkedin.com/in/benedict-kuloba-76954512a/)
    - **GitHub**: [myles-G](https://github.com/myles-G)
    - **Email**: [benedictkuloba@yahoo.com](mailto:benedictkuloba@yahoo.com)
    """)

    st.subheader("Gerald Mwangi - Modelling Aficionado")
    st.image('Gerald.jpeg', width=150)
    st.markdown("""
    Gerald is our modeling maestro, crafting predictive pipelines that crunch numbers and turn raw data into actionable insights you can trust.
    - **LinkedIn**: [Gerald Mwangi](https://www.linkedin.com/in/gerald-mwangi-662870230/)
    - **GitHub**: [Geraldkigotho](https://github.com/Geraldkigotho)
    - **Email**: [mwangigerald436@gmail.com](mailto:mwangigerald436@gmail.com)
    """)

    st.subheader("Jackson Mwaniki - Scrum Master")
    st.image('Jackson.jpeg', width=150)
    st.markdown("""
    Jackson ensures smooth and efficient project delivery by keeping the team focused and on track.
    - **LinkedIn**: [Jackson Mwaniki](https://www.linkedin.com/in/jackson-mwaniki/)
    - **GitHub**: [jakkkc](https://github.com/jakkkc)
    - **Email**: [jacmwaniki@gmail.com](mailto:jacmwaniki@gmail.com)
    """)

    st.subheader("Mwaura Njung'e - App Deployment Wizard")
    st.image('Mwaura.jpeg', width=150)
    st.markdown("""
    When it comes to deploying apps in the cloud, Mwaura is the expert who ensures everything functions perfectly and delivers a flawless UX.
    - **LinkedIn**: [Kelvin Mwaura](https://www.linkedin.com/in/kelvin-mwaura-a642351a2/)
    - **GitHub**: [TyrionCodister](https://github.com/TyrionCodister)
    - **Email**: [kelvinmwaura.edu@gmail.com](mailto:kelvinmwaura.edu@gmail.com)
    """)

elif page == "Feedback":
    st.header("We Value Your Feedback")
    st.markdown("Please share your thoughts and suggestions about our app:")
    
    feedback = st.text_area("Your Feedback")
    if st.button("Submit"):
        st.success("Thank you for your feedback!")



































