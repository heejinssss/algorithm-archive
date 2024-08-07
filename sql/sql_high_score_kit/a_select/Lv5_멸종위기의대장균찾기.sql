-- RECURSIVE CTE
WITH RECURSIVE CTE AS (
    SELECT ID, 1 AS GENERATION
      FROM ECOLI_DATA
     WHERE PARENT_ID IS NULL

 UNION ALL
    
    SELECT A.ID, GENERATION + 1 AS GENERATION
      FROM ECOLI_DATA AS A INNER JOIN CTE
        ON CTE.ID = A.PARENT_ID
)

   SELECT COUNT(*) AS COUNT, A.GENERATION
     FROM CTE A LEFT JOIN ECOLI_DATA B
       ON A.ID = B.PARENT_ID
    WHERE B.ID IS NULL
 GROUP BY GENERATION
 ORDER BY GENERATION;