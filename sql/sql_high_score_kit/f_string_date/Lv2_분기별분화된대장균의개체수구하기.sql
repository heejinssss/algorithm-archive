WITH MONTH AS (
    SELECT CASE
           WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 10 AND 12 THEN '4'
           WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 7 AND 9 THEN '3'
           WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 4 AND 6 THEN '2'
           ELSE '1' END AS QUARTER
      FROM ECOLI_DATA
)

  SELECT CONCAT(QUARTER, 'Q') AS QUARTER, COUNT(QUARTER) AS ECOLI_COUNT
    FROM MONTH
GROUP BY QUARTER
ORDER BY CONCAT(QUARTER, 'Q');