import streamlit as st
from utils import load_data, calculate_average, plot_distribution
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
dbe = load_data('./cleaned_benin_malanville.csv')
dsi = load_data('./cleaned_sierra_leone_bumbuna.csv')
dto = load_data('./cleaned_togo_dapaong_qc.csv')

# Title of the dashboard
st.title('Renewable Energy Data Dashboard')

# Navigation sidebar
page = st.sidebar.selectbox("Select a page", ['Benin-Malanville', 'Sierra Leone-Bumbuna', 'Togo-Dapaong_qc'])

# Helper function to create scatter plots
def scatter_plot(data, x_col, y_col, title):
    fig, ax = plt.subplots()
    ax.scatter(data[x_col], data[y_col], alpha=0.5)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)
    st.pyplot(fig)

# Helper function to create correlation heatmap
def correlation_heatmap(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Interactive function to select columns for scatter plot
def interactive_scatter_plot(data):
    st.subheader('Interactive Scatter Plot')
    available_columns = data.columns.tolist()
    
    # Select X and Y columns
    x_col = st.selectbox('Select X-axis column', available_columns)
    y_col = st.selectbox('Select Y-axis column', available_columns)
    
    scatter_plot(data, x_col, y_col, f'{x_col} vs {y_col}')

# Interactive function to select columns for correlation heatmap
def interactive_correlation_heatmap(data):
    st.subheader('Interactive Correlation Heatmap')
    available_columns = data.columns.tolist()
    
    # Multi-select for columns to include in the heatmap
    selected_columns = st.multiselect('Select columns for correlation heatmap', available_columns, default=available_columns)
    
    if selected_columns:
        correlation_heatmap(data[selected_columns])

# Display data based on user selection
if page == 'Benin-Malanville':
    st.subheader('Benin-Malanville Data')
    st.write(dbe)  # Display the Benin-Malanville data
    
    # Example: Calculate and display average of GHI
    average_ghi_benin = calculate_average(dbe, 'GHI')
    st.write(f"Average GHI in Benin-Malanville: {average_ghi_benin}")
    
    # Plot distribution of GHI
    st.subheader('Distribution of GHI')
    plot_distribution(dbe, 'GHI')

    # Interactive visualizations
    interactive_scatter_plot(dbe)
    interactive_correlation_heatmap(dbe)

elif page == 'Sierra Leone-Bumbuna':
    st.subheader('Sierra Leone-Bumbuna Data')
    st.write(dsi)  # Display the Sierra Leone-Bumbuna data
    
    # Example: Calculate and display average of GHI
    average_ghi_sierra = calculate_average(dsi, 'GHI')
    st.write(f"Average GHI in Sierra Leone-Bumbuna: {average_ghi_sierra}")
    
    # Plot distribution of GHI
    st.subheader('Distribution of GHI')
    plot_distribution(dsi, 'GHI')

    # Interactive visualizations
    interactive_scatter_plot(dsi)
    interactive_correlation_heatmap(dsi)

else:
    st.subheader('Togo-Dapaong_qc Data')
    st.write(dto)  # Display the Togo-Dapaong_qc data
    
    # Example: Calculate and display average of GHI
    average_ghi_togo = calculate_average(dto, 'GHI')
    st.write(f"Average GHI in Togo-Dapaong_qc: {average_ghi_togo}")
    
    # Plot distribution of GHI
    st.subheader('Distribution of GHI')
    plot_distribution(dto, 'GHI')

    # Interactive visualizations
    interactive_scatter_plot(dto)
    interactive_correlation_heatmap(dto)
