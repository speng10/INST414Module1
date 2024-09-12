import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('Urban Air Quality and Health Impact Dataset.csv')

# Inspect the first few rows
#print(data.head())

data.isnull().sum().sort_values(ascending=False)

# Function for Temperature Distribution
def plot_temperature_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='City', y='temp', data=data, color='lightblue')
    # Set plot title and labels
    plt.title('Average Temperature Distribution Across Cities')
    plt.ylabel('Average Temperature (°F)')
    # Display the plot
    plt.show()

# Function for average Health Risk Score Comparison
def plot_health_risk_score(data):
    plt.figure(figsize=(10, 6))
    # Group by city and calculate the mean Health Risk Score
    avg_health_risk = data.groupby('City')['Health_Risk_Score'].mean().reset_index()
    # Create a bar plot with average health risk score for each city
    sns.barplot(x='City', y='Health_Risk_Score', data=avg_health_risk, color='green')
    # Set plot title and labels
    plt.title('Average Health Risk Score by City')
    plt.ylabel('Average Health Risk Score (Lower is Better)')
    # Display the plot
    plt.show()

# Function for Precipitation Probability
def plot_precipitation_prob(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='City', y='precipprob', data=data, color='blue')
    # Set the plot title and labels
    plt.title('Precipitation Probability by City')
    plt.ylabel('Precipitation Probability (%)')
    # Display the plot
    plt.show()

def plot_severity_score(data):
    plt.figure(figsize=(12, 6))
    # 'DateTime' is in datetime format
    data['DateTime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d')
    # Create a line plot with 'Date' on the x-axis and 'Severity_Score' on the y-axis
    sns.lineplot(x='datetime', y='Severity_Score', hue='City', data=data, marker='o')
    # Set the y-axis limit
    plt.ylim(0, 10)
    # Set plot title and labels
    plt.title('Weather Severity Score Over Time by City')
    plt.ylabel('Severity Score (Lower is Better)')
    plt.xlabel('Date')
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    # Display the plot
    plt.tight_layout()
    plt.show()

def plot_health_risk_by_time(data):
    plt.figure(figsize=(12, 6))
    # 'DateTime' is in datetime format
    data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d')
    # Create a line plot with 'Time' on the x-axis and Health_Risk_Score on the y-axis
    sns.lineplot(x='datetime', y='Health_Risk_Score', hue='City', data=data, marker='o')
    # Set the plot title and labels
    plt.title('Health Risk Score by Time of Day for Each City')
    plt.ylabel('Health Risk Score')
    plt.xlabel('Date')
    # Display the plot
    plt.tight_layout()
    plt.show()
    
# Call the functions
plot_temperature_distribution(data)
plot_health_risk_score(data)
plot_precipitation_prob(data)
plot_severity_score(data)
plot_health_risk_by_time(data)