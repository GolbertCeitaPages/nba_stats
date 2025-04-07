from nba_config import ANALYTICS_DB_CONFIG
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as sk

conn = mysql.connector.connect(**ANALYTICS_DB_CONFIG)
cursor = conn.cursor()


cursor.execute("SELECT * FROM nba_stats_analytics.salary_analysis")

data = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]

df = pd.DataFrame(data, columns=columns)

cursor.close()
conn.close()

# Check NA values
print(df.isna().sum())

columns_to_replace = columns[8:]

df[columns_to_replace] = df[columns_to_replace].replace(np.nan,0)

print()

# Check NA values after
print(df.isna().sum())

# Drop non-numeric columns
columns_to_drop = ['season','player','pos','age','experience','tm']
df = df.drop(columns_to_drop,axis=1)

corr_matrix = df.corr()

plt.figure(figsize=(12, 8))
sb.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)

plt.title('Heatmap')
plt.show()