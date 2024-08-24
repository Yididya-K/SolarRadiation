import streamlit as st
from utils import load_data, calculate_average, plot_distribution

# Load the cleaned data
dbe = load_data('cleaned_benin_malanville.csv')
dsi = load_data('cleaned_sierra_leone_bumbuna.csv')
dto = load_data('cleaned_togo_dapaong_qc.csv')

# Title of the dashboard
st.title('Renewable Energy Data Dashboard')

# Navigation sidebar
page = st.sidebar.selectbox("Select a page", ['Benin-Malanville', 'Sierra Leone-Bumbuna', 'Togo-Dapaong_qc'])

# Display data based on user selection
if page == 'Benin-Malanville':
    st.subheader('Benin-Malanville Data')
    st.write(dbe)  # Display the Benin-Malanville data
    average_energy_benin = calculate_average(dbe, 'Energy_Consumption')
    st.write(f"Average energy consumption in Benin-Malanville: {average_energy_benin}")
    plot_distribution(dbe, 'Energy_Consumption')

elif page == 'Sierra Leone-Bumbuna':
    st.subheader('Sierra Leone-Bumbuna Data')
    st.write(dsi)  # Display the Sierra Leone-Bumbuna data

else:
    st.subheader('Togo-Dapaong_qc Data')
    st.write(dto)  # Display the Togo-Dapaong_qc data