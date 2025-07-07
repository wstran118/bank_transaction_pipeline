SELECT transaction_id, COUNT(*)
FROM transformed_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;