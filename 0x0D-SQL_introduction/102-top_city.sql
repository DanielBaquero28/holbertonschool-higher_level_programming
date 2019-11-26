-- Displays the top 3 of cities temperature
-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT
	test.city,
	AVG(test.value)
AS
	avg_temp
FROM
	temperatures test
WHERE
	month = 7 or month = 8
GROUP BY
      test.city
ORDER BY
      avg_temp DESC
LIMIT
	3;
