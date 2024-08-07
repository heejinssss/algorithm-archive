-- MySQL
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;

-- Oracle
SELECT *
FROM (SELECT NAME
      FROM ANIMAL_INS
      ORDER BY DATETIME)
WHERE ROWNUM = 1;