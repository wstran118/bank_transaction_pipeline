import pandas as pd
import sqlite3

def load_final_data(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql("SELECT * FROM transformed_transactions", conn)
        df.to_sql("final_transactions", conn, if_exists="replace", index=False)
        