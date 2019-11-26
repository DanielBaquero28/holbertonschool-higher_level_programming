-- Lists all records of the table
-- Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT test.score, test.name FROM second_table test
WHERE score >= 10
ORDER BY test.score DESC;
