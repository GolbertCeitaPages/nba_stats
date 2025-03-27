# load file
import mysql.connector
from nba_config import RAW_DB_CONFIG
import pandas as pd

# Function to insert data into a given table
def insert_data(df, table_name):

    conn = mysql.connector.connect(**RAW_DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute(f"TRUNCATE TABLE {table_name}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    # Get the column names from the DataFrame
    columns = df.columns.tolist()

    # Create a comma-separated string of column names
    column_str = ', '.join(columns)

    # Create the placeholders (%s) for the values
    value_placeholders = ', '.join(['%s'] * len(columns))

    # Construct the SQL INSERT query dynamically
    insert_query = f"""
        INSERT INTO {table_name} ({column_str}) 
        VALUES ({value_placeholders})
    """
    
    # Loop through the DataFrame and insert data
    for row in df.itertuples(index=False):
        try:
            # Replace NaN values with None
            values = [None if pd.isna(x) else x for x in row]
            
            # Execute the query with the row values
            cursor.execute(insert_query, values)
        except Exception as e:
            print(f"Error inserting row {row}: {e}")

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()