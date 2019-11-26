-- Lists number of records with the same score
-- Lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT
	test.score,
	COUNT(test.score)
AS
	number
FROM
	second_table test
GROUP BY test.score
HAVING COUNT(test.score) >= 1
ORDER BY number DESC;
