  SELECT YEAR(B.SALES_DATE) AS YEAR,
         MONTH(B.SALES_DATE) AS MONTH,
         A.GENDER AS GENDER,
         COUNT(DISTINCT A.USER_ID) AS USERS
    FROM USER_INFO A, ONLINE_SALE B 
   WHERE A.USER_ID = B.USER_ID
     AND A.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;