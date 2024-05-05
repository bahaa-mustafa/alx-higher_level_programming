-- lists the number of records with the same score
SELECT score, name FROM second_table GROUP BY score HAVING COUNT(*) > 1 ORDER BY score DESC;
