import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('workforce_data.csv')

# Data Cleaning
# Check for missing values
print("Missing Values:")
print(df.isnull().sum())
# Ensure numeric columns are correct type
df['PerformanceScore'] = df['PerformanceScore'].astype(float)
df['TasksCompleted'] = df['TasksCompleted'].astype(float)
df['HoursWorked'] = df['HoursWorked'].astype(float)

# Calculate Productivity (Tasks per Hour)
df['Productivity'] = df['TasksCompleted'] / df['HoursWorked']

# Display Dataset Preview
print("\nDataset Preview:")
print(df.head())

# Pivot Table 1: Average PerformanceScore by Department and Year
pivot_performance = df.pivot_table(
    values='PerformanceScore',
    index='Year',
    columns='Department',
    aggfunc='mean'
)
print("\nPivot Table: Average PerformanceScore by Year and Department")
print(pivot_performance)

# Pivot Table 2: Total TasksCompleted by Role and Quarter
pivot_tasks = df.pivot_table(
    values='TasksCompleted',
    index='Quarter',
    columns='Role',
    aggfunc='sum'
)
print("\nPivot Table: Total TasksCompleted by Quarter and Role")
print(pivot_tasks)

# Visualization 1: PerformanceScore by Department (Bar Plot)
plt.figure(figsize=(10, 6))
pivot_performance.plot(kind='bar')
plt.title('Average Performance Score by Year and Department')
plt.ylabel('Performance Score')
plt.xlabel('Year')
plt.legend(title='Department')
plt.tight_layout()
plt.savefig('performance_by_department.png')
plt.show()

# Visualization 2: Productivity Trends Over Time (Line Plot)
plt.figure(figsize=(10, 6))
productivity_trends = df.groupby(['Year', 'Quarter'])['Productivity'].mean().reset_index()
productivity_trends['Time'] = productivity_trends['Year'].astype(str) + '-' + productivity_trends['Quarter']
sns.lineplot(data=productivity_trends, x='Time', y='Productivity', marker='o')
plt.title('Productivity Trends Over Time')
plt.ylabel('Tasks per Hour')
plt.xlabel('Time (Year-Quarter)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('productivity_trends.png')
plt.show()

# Visualization 3: Heatmap of PerformanceScore by Department and Role
plt.figure(figsize=(10, 6))
pivot_heatmap = df.pivot_table(
    values='PerformanceScore',
    index='Department',
    columns='Role',
    aggfunc='mean'
)
sns.heatmap(pivot_heatmap, annot=True, cmap='YlGnBu', fmt='.1f')
plt.title('Average Performance Score by Department and Role')
plt.tight_layout()
plt.savefig('performance_heatmap.png')
plt.show()