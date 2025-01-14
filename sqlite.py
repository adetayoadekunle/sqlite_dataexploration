import pandas as pd
import sqlite3

conn = sqlite3.connect('healthcare.db')      

df = pd.read_csv('https://data.cdc.gov/resource/bi63-dtpu.csv')
df
df['deaths'].value_counts()

df.to_sql('leading_causes_of_death_us', conn, if_exists='replace', index=False)

query  = 'SELECT * FROM leading_causes_of_death_us WHERE cause_name = 'Heart disease';

result_df = pd.read_sql_query(query, conn)

print(result_df)