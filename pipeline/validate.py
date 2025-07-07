import pandas as pd
import sqlite3

def run_validation_checks(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_csv("SELECT * FROM staging_transactions", conn)

        errors = []

        if df['transaction_id'].isnull().any():
            errors.append("Null transaction_id found.")
        if (df['amount'] < 0).any():
            errors.append("Negative transaction amounts found.")
        if not pd.to_datetime(df['transaction_date'], errors='coerce').notnull().all():
            errors.append("Invalid transaction_date format.")

        return errors