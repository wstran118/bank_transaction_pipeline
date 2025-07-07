import pandas as pd
import sqlite3

def transform_data(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql("SELECT * FROM staging_ transactions", conn)
        df['transaction_type'] = df['amount'].apply(lambda x: 'debit' if x < 0 else 'credit')
        df['day_of_week'] = pd.to_datetime(df['transaction_date']).dt.day_name()
        df.to_sql("transformed transactions", conn, if_exists="replace", index=False)
        