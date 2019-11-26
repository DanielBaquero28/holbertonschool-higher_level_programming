-- Displays the average temperature by city
-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT
	test.city,
	AVG(test.value)
AS
	avg_temp
FROM
	temperatures test
GROUP BY
      test.city
ORDER BY
      test.avg_temp DESC;
