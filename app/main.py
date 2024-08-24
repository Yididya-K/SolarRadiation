import streamlit as st
from utils import load_data, calculate_average, plot_distribution

# Load the cleaned data
dbe = load_data('./cleaned_benin_malanville.csv')
dsi = load_data('./cleaned_sierra_leone_bumbuna.csv')
dto = load_data('./cleaned_togo_dapaong_qc.csv')

# Title of the dashboard
st.title('Renewable Energy Data Dashboard')

# Navigation sidebar
page = st.sidebar.selectbox("Select a page", ['Benin-Malanville', 'Sierra Leone-Bumbuna', 'Togo-Dapaong_qc'])

# Display data based on user selection
if page == 'Benin-Malanville':
    st.subheader('Benin-Malanville Data')
    st.write(dbe)  # Display the Benin-Malanville data
    
    # Calculate and display average energy consumption
    average_energy_benin = calculate_average(dbe, 'Energy_Consumption')
    st.write(f"Average energy consumption in Benin-Malanville: {average_energy_benin}")
    
    # Plot distribution of energy consumption
    st.subheader('Distribution of Energy Consumption')
    plot_distribution(dbe, 'Energy_Consumption')

    # Additional visualizations
    st.subheader('Energy Production vs. Consumption')
    st.line_chart(dbe[['Energy_Production', 'Energy_Consumption']])

elif page == 'Sierra Leone-Bumbuna':
    st.subheader('Sierra Leone-Bumbuna Data')
    st.write(dsi)  # Display the Sierra Leone-Bumbuna data
    
    # Calculate and display average energy consumption
    average_energy_sierra = calculate_average(dsi, 'Energy_Consumption')
    st.write(f"Average energy consumption in Sierra Leone-Bumbuna: {average_energy_sierra}")
    
    # Plot distribution of energy consumption
    st.subheader('Distribution of Energy Consumption')
    plot_distribution(dsi, 'Energy_Consumption')

    # Additional visualizations
    st.subheader('Energy Production Trend')
    st.area_chart(dsi['Energy_Production'])

else:
    st.subheader('Togo-Dapaong_qc Data')
    st.write(dto)  # Display the Togo-Dapaong_qc data
    
    # Calculate and display average energy consumption
    average_energy_togo = calculate_average(dto, 'Energy_Consumption')
    st.write(f"Average energy consumption in Togo-Dapaong_qc: {average_energy_togo}")
    
    # Plot distribution of energy consumption
    st.subheader('Distribution of Energy Consumption')
    plot_distribution(dto, 'Energy_Consumption')

    # Additional visualizations
    st.subheader('Energy Source Comparison')
    st.bar_chart(dto.groupby('Energy_Source')['Energy_Consumption'].sum())

    st.subheader('Renewable Energy Production by Source')
    st.area_chart(dto.pivot_table(index='Month', columns='Energy_Source', values='Energy_Production', aggfunc='sum'))