from pipeline import ingest, validate, transform, verify_sql, load

DB_PATH = 'db/bank.db'
CSV_FILE = 'data/transactions_2025_07_01.csv'

# 1. Ingest
ingest.ingest_csv_to_db(CSV_FILE, DB_PATH)

# 2. Validate
errors = validate.run_validation_checks(DB_PATH)
if errors:
    print("Validation errors:", errors)
    exit()

# 3. Transform
transform.transform_data(DB_PATH)

# 4. SQL Verification
sql_issues = verify_sql.run_sql_verification(DB_PATH)
if sql_issues['duplicates']:
    print("Duplicate transaction IDs found:", sql_issues['duplicates'])
    exit()
if sql_issues['high_values']:
    print("High-value transactions flagged for review:", sql_issues['high_values'])

# 5. Load
load.load_final_data(DB_PATH)
print("Pipeline completed successfully.")
