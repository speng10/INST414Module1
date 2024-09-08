import pandas as pd

# Load dataset
data = pd.read_csv('urban_air_quality.csv')

# Inspect the first few rows
print(data.head())

python
Copy code
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation matrix
corr_matrix = data[['Temp_Avg', 'Humidity', 'Precip_Prob', 'Wind_Speed', 'Health_Risk_Score']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

