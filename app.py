import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('Best_performing_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict Price", "About", "Meet the Team", "Feedback"])

# Display the logo below the sidebar
st.sidebar.image(r'C:\Phase 5 final project\car_price\company logo.png', width=200)

# Set the title of the app
st.title("Car Price Prediction App")

# Display the main content based on selected page
if page == "Home":
    st.header("Welcome to the Car Price Prediction App")
    st.markdown("""
    The Car Price Prediction App is designed to provide accurate, data-driven predictions for used car prices in Kenya. Here's how to use it:
    
    1. **Enter the Car Details**
    2. **Predict the Price**
    3. **Get the Estimated Price**
    """)

elif page == "About":
    st.header("About Neural Gearbox")
    st.markdown("""
    **Mission Statement**: We’re here to help Kenyans buy and sell used cars with confidence. By providing clear, data-driven insights, we make it easier for you to make smart decisions in the used car market.
    
    **Vision**: Our goal is to be Kenya’s go-to platform for car price predictions, where every transaction is fair, transparent, and based on trust.
    
    **Motto**: "Drive the future, predict the value."
    
    ### Contact Information
    For support or inquiries, please reach out to [kelvin.mwaura.edu@gmail.com](mailto:kelvin.mwaura.edu@gmail.com).
    """)

elif page == "Meet the Team":
    st.header("Meet the Team")
    
    st.subheader("Gerald Mwangi")
    st.image(r'C:\Phase 5 final project\car_price\Gerald.jpeg', width=150)
    st.markdown("""
    - **LinkedIn**: [Gerald Mwangi](https://www.linkedin.com/in/gerald-mwangi-662870230/)
    - **GitHub**: [Geraldkigotho](https://github.com/Geraldkigotho)
    - **Email**: [mwangigerald436@gmail.com](mailto:mwangigerald436@gmail.com)
    """)

elif page == "Predict Price":
    st.header("Predict the Price of a Car")

    # Input fields for user input
    Name = st.text_input("Car Name", "Toyota Corolla")
    Year = st.slider("Year of Manufacture", 1990, 2024, 2015)
    Kilometers_Driven = st.slider("Mileage", 0, 300000, 50000)
    Fuel_Type = st.selectbox("Fuel Type", ("Petrol", "Diesel", "CNG"))
    Transmission = st.selectbox("Transmission", ("Manual", "Automatic"))
    Use = st.selectbox("Use", ("Foreign", "Local"))
    Engine = st.slider("Engine Capacity (cc)", 800, 5000, 1500)
    Power = st.slider("Horse Power (bhp)", 50, 400, 100)
    Seats = st.slider("Seats", 2, 7, 5)

    # Predict button
    if st.button("Predict Price"):
        # Map categorical features to numerical values
        fuel_type_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
        transmission_map = {"Manual": 0, "Automatic": 1}
        use_map = {"Foreign": 0, "Local": 1}

        # Prepare the input features
        features = np.array([
            Year,
            Kilometers_Driven,
            fuel_type_map[Fuel_Type],
            transmission_map[Transmission],
            use_map[Use],
            Engine,
            Power,
            Seats
        ]).reshape(1, -1)
        
        # Predict the car price
        price = model.predict(features)[0]
        st.success(f"Estimated Price for {Name}: ${price:,.2f}")

elif page == "Feedback":
    st.header("We Value Your Feedback")
    st.markdown("Please share your thoughts and suggestions about our app:")
    
    feedback = st.text_area("Your Feedback")
    if st.button("Submit"):
        st.success("Thank you for your feedback!")

























