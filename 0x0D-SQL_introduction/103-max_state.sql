-- Displays the top 3 of cities temperature
-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT
	test.state,
	MAX(test.value)
AS
	max_temp
FROM
	temperatures test
GROUP BY
      test.state
ORDER BY
      test.state ASC;
