import pandas as pd
import sqlite3

def ingest_csv_to_db(file_path, db_path):
    df = pd.read_csv(file_path)
    with sqlite3.connect(db_path) as conn:
        df.to_sql("staging_transactions", conn, if_exists="replace", index=False)
        