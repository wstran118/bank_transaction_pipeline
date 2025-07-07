import pandas as pd
import sqlite3

def run_sql_verification(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        with open('sql/verify_duplicate_transactions.sql') as f:
            duplicate_check = f.read()
        cursor.execute(duplicate_check)
        duplicates = cursor.fetchall()

        with open('sql/verify_high_value_transactions.sql') as f:
            high_value_check = f.read()
        cursor.execute(high_value_check)
        high_values = cursor.fetchall()

        return {"duplicates": duplicates, "high value": high_values}