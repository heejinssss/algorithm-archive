-- MySQL
SELECT B.BOOK_ID, A.AUTHOR_NAME,
       DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B, AUTHOR A
WHERE B.CATEGORY = "경제" AND B.AUTHOR_ID = A.AUTHOR_ID
ORDER BY PUBLISHED_DATE;

-- Oracle
SELECT B.BOOK_ID, A.AUTHOR_NAME,
       TO_CHAR(B.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM BOOK B, AUTHOR A
WHERE B.CATEGORY = '경제' AND B.AUTHOR_ID = A.AUTHOR_ID
ORDER BY PUBLISHED_DATE;