-- lists the number of records with the same score
SELECT score, name FROM second_table HAVING COUNT(score) > 1 ORDER BY score DESC;
