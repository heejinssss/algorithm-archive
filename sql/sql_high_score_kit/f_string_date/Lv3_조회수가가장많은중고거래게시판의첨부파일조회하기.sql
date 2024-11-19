  SELECT CONCAT('/home/grep/src/', B.BOARD_ID, '/', B.FILE_ID, B.FILE_NAME, B.FILE_EXT) AS FILE_PATH
    FROM USED_GOODS_BOARD A, USED_GOODS_FILE B
   WHERE A.BOARD_ID = B.BOARD_ID
     AND A.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_ID DESC;