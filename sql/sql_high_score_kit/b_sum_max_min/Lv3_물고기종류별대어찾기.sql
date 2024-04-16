SELECT D.ID, C.FISH_NAME, D.MAXL AS LENGTH
FROM FISH_NAME_INFO C, (SELECT A.ID AS ID, B.FISH_TYPE AS FISH_TYPE, B.MAXL AS MAXL
                          FROM FISH_INFO A JOIN (SELECT FISH_TYPE, MAX(LENGTH) AS MAXL
                                                 FROM FISH_INFO
                                                 GROUP BY FISH_TYPE) B
                                                 ON (A.FISH_TYPE = B.FISH_TYPE
                                                 AND A.LENGTH = B.MAXL)) D
WHERE C.FISH_TYPE = D.FISH_TYPE
ORDER BY D.ID;