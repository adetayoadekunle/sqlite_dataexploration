import pandas as pd
import sqlite3

conn = sqlite3.connect('healthcare.db')      

df = pd.read_csv('https://data.cdc.gov/resource/bi63-dtpu.csv')

df.to_sql('leading_causes_of_death_us', conn, if_exists='replace', index=False)

query1 = """
    SELECT * 
    FROM leading_causes_of_death_us
    WHERE state = 'New York';
"""
result_df1 = pd.read_sql_query(query1, conn)
print("Query 1: All records for New York:")
print(result_df1)

result_df1 = pd.read_sql_query(query1, conn)
print("Query 1: Heart disease records:")
print(result_df1)

query2 = """
    SELECT COUNT(*) AS total_records
    FROM leading_causes_of_death_us
    WHERE cause_name = 'Cancer';
"""
result_df2 = pd.read_sql_query(query2, conn)
print("Query  2: Total records for Cancer")
print(result_df2)

query3 = """
    SELECT SUM(deaths) AS total_deaths
    FROM leading_causes_of_death_us;
"""
result_df3 = pd.read_sql_query(query3, conn)
print("Query 3: Total deaths in the dataset")
print(result_df3)

query4 = """
    SELECT * 
    FROM leading_causes_of_death_us
    LIMIT 5;
"""
result_df4 = pd.read_sql_query(query4, conn)
print("Query 4: First 5 records")
print(result_df4)

conn.close()