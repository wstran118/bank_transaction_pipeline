SELECT * 
FROM  transformed_transactions
WHERE ABS(amount) > 10000;