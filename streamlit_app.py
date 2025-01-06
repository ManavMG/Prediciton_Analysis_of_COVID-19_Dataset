import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the COVID-19 dataset (Assuming it's in CSV format or already processed data)
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/ManavMG/Prediction_Analysis_of_COVID-19_Dataset/main/data/covid_data.csv"
    data = pd.read_csv(url)
    return data

# Load data
data = load_data()

# Set up the app title and description
st.title("COVID-19 Prediction Analysis")
st.markdown("""
    This app performs prediction analysis on the COVID-19 dataset.
    The goal is to analyze COVID-19 data trends, predict future cases, and visualize the findings.
""")

# Display data as a table
if st.checkbox('Show raw data'):
    st.write(data)

# Select the feature to analyze
feature = st.selectbox('Select a feature to analyze:', data.columns)

# Display a line chart for the selected feature
st.line_chart(data[feature])

# Add a plot for feature trends (e.g., daily new cases)
if st.button('Show Trend Analysis'):
    plt.figure(figsize=(10, 6))
    data['Date'] = pd.to_datetime(data['Date'])
    plt.plot(data['Date'], data['New Cases'], label="New Cases")
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.title('COVID-19 New Cases Trend')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot()

# Display a prediction or analysis button (if you have a prediction model)
if st.button('Make Prediction'):
    # Sample prediction logic (You should replace it with actual model logic)
    prediction = np.random.randint(1000, 10000)  # Simulated prediction
    st.write(f"The predicted number of COVID-19 cases for the next day is: {prediction}")

# Show the app's footer
st.markdown("### Made with ❤️ by [Your Name]")

