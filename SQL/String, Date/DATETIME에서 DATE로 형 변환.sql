#DATE_FORMAT 함수 이용 ==> 대소문자에 따라 표현방식도 바뀐다는사실..! 

SELECT ANIMAL_ID, NAME, 
-- DATE_FORMAT(DATETIME, '%Y-%M-%D') AS 날짜
-- 2016-June-7th
DATE_FORMAT(DATETIME,'%Y-%m-%d') AS 날짜 
-- 	2015-01-29
FROM ANIMAL_INS ;

