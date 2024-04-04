SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS,
       ROUND(AVG(b.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO a, REST_REVIEW b
WHERE (LEFT(a.ADDRESS, 3) = '서울시' OR LEFT(a.ADDRESS, 5) = '서울특별시')
  AND a.REST_ID = b.REST_ID
GROUP BY REST_ID
ORDER BY ROUND(AVG(b.REVIEW_SCORE), 2) DESC, a.FAVORITES DESC;