import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('healthcare.db')  

# Getting public health dataset from CDC online source
df = pd.read_csv('https://data.cdc.gov/resource/bi63-dtpu.csv')

# Load dataset into SQLite database
df.to_sql('leading_causes_of_death_us', conn, if_exists='replace', index=False)

# Query 1: Select all records for New York
query1 = """
    SELECT * 
    FROM leading_causes_of_death_us
    WHERE state = 'New York';
"""
result_df1 = pd.read_sql_query(query1, conn)
print("Query 1: All records for New York:")
print(result_df1)

# Query 2: Count number of records where deaths exceed 600
query2 = """
    SELECT COUNT(*) AS total_records
    FROM leading_causes_of_death_us
    WHERE deaths > 600;
"""
result_df2 = pd.read_sql_query(query2, conn)
print("Query 2: Total Records where deaths exceed 500:")
print(result_df2)

# Query 3: Groups data by state and calculates total deaths for each state
query3 = """
    SELECT state, SUM(deaths) AS total_deaths
    FROM leading_causes_of_death_us
    GROUP BY state;
"""
result_df3 = pd.read_sql_query(query3, conn)
print("Query 3: Total deaths grouped by state:")
print(result_df3)

# Query 4: Select first 5 records in dataset
query4 = """
    SELECT * 
    FROM leading_causes_of_death_us
    LIMIT 5;
"""
result_df4 = pd.read_sql_query(query4, conn)
print("Query 4: First 5 records")
print(result_df4)

conn.close()