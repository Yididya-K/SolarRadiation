import streamlit as st
from utils import load_data, calculate_average, plot_distribution
import matplotlib.pyplot as plt
import seaborn as sns

file_id_benin = '1DY0AgTabaKKMkyAxnZrrDnx_TTNYlqvT'
file_id_sierra = '1WzQE79qQtj4McrkgJqNduCPfL8pj4rNn'
file_id_togo = '1pZkFkGf8JvL2ZYbQm6Z2hTg_j7quDdIQ'

file_url_benin = f'https://drive.google.com/uc?id={file_id_benin}'
file_url_sierra = f'https://drive.google.com/uc?id={file_id_sierra}'
file_url_togo = f'https://drive.google.com/uc?id={file_id_togo}'

dbe = load_data(file_url_benin)
dsi = load_data(file_url_sierra)
dto = load_data(file_url_togo)


# Check if data loaded correctly
if dbe is not None:
    st.write("Benin-Malanville Data Loaded Successfully")
    st.write(dbe.head())  # Display the first few rows for verification
else:
    st.write("Failed to load Benin-Malanville Data")

if dsi is not None:
    st.write("Sierra Leone-Bumbuna Data Loaded Successfully")
    st.write(dsi.head())  # Display the first few rows for verification
else:
    st.write("Failed to load Sierra Leone-Bumbuna Data")

if dto is not None:
    st.write("Togo-Dapaong_qc Data Loaded Successfully")
    st.write(dto.head())  # Display the first few rows for verification
else:
    st.write("Failed to load Togo-Dapaong_qc Data")

# Title of the dashboard
st.title('Renewable Energy Data Dashboard')

# Navigation sidebar
page = st.sidebar.radio("Select a section", ['Data Overview', 'Interactive Visualizations'])

# Sidebar dropdown for dataset selection (available in both sections)
selected_dataset = st.sidebar.selectbox("Select Dataset", ['Benin-Malanville', 'Sierra Leone-Bumbuna', 'Togo-Dapaong_qc'])

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

# Select the dataset based on user choice
if selected_dataset == 'Benin-Malanville':
    data = dbe
    location_name = 'Benin-Malanville'
elif selected_dataset == 'Sierra Leone-Bumbuna':
    data = dsi
    location_name = 'Sierra Leone-Bumbuna'
else:
    data = dto
    location_name = 'Togo-Dapaong_qc'

# Section 1: Data Overview
if page == 'Data Overview':
    st.subheader(f'{location_name} Data')
    st.write(data)  # Display the selected dataset
    
    # Example: Calculate and display average of GHI
    average_ghi = calculate_average(data, 'GHI')
    st.write(f"Average GHI in {location_name}: {average_ghi}")
    
    # Plot distribution of GHI
    st.subheader('Distribution of GHI')
    plot_distribution(data, 'GHI')

# Section 2: Interactive Visualizations
elif page == 'Interactive Visualizations':
    st.subheader(f'Interactive Visualizations for {location_name}')
    
    # Choose which interactive visualization to show
    visualization_type = st.radio("Choose Visualization Type", ['Scatter Plot', 'Correlation Heatmap'])

    if visualization_type == 'Scatter Plot':
        interactive_scatter_plot(data)
    elif visualization_type == 'Correlation Heatmap':
        interactive_correlation_heatmap(data)
