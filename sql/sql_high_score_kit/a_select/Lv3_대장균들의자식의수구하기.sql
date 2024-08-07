   SELECT B.ID, IFNULL(A.CNT, 0) AS CHILD_COUNT
     FROM ECOLI_DATA B
LEFT JOIN (SELECT PARENT_ID, COUNT(ID) AS CNT
             FROM ECOLI_DATA
            WHERE PARENT_ID IS NOT NULL
         GROUP BY PARENT_ID) A ON B.ID = A.PARENT_ID;