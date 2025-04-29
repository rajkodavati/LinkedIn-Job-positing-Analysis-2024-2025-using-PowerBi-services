import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'LdIn_data_f.csv')
print(df.columns)
#heatmap for the data
numeric_data = df.select_dtypes(include=['float64', 'int64'])  # filter only numeric columns
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

#pie chart for the comapnies

company_counts = df['company_name'].value_counts()
top_companies = company_counts.head(10)
plt.figure(figsize=(8, 8))
plt.pie(top_companies, labels=top_companies.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Companies by Number of Job Postings')
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()


industries = df['industry'].value_counts()
top_industries = industries.head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_industries.index, top_industries.values, color='skyblue')
plt.title("Top 10 Industries by Job Postings")
plt.xlabel("Industry")
plt.ylabel("Number of Job Postings")
plt.xticks(rotation=45, ha='right')  # rotate x labels for readability
plt.tight_layout()
plt.show()





