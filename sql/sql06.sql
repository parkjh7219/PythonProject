-- 서브 쿼리
-- 하나의 SQL 문장에 괄호를 이용해서 또 다른 쿼리를 포함시킨 것 - 쿼리 속에 쿼리
-- 서브 쿼리는 메인 쿼리에 필요한 값을 제공하거나 조건을 계산하는데 사용
-- 즉, 메인 쿼리 안에 포함되어 실행되는 보조 쿼리

-- 단일행 서브 쿼리 : 서브 쿼리의 결과가 한 행만 나오는 형태, 비교연산자와 함께 사용

-- 다중행 서브 커리 (복수행 서브 쿼리) 서브 쿼리의 결과가 여러 행이 나오는 형태, IN ANY ALL 연산자와 함께 사용

-- 가장 많은 마이리리지를 보유한 고객 조회 (이전 방식)
SELECT MAX(마일리지) 가장높은마일리지 FROM 고객;
SELECT * FROM 고객 WHERE 마일리지 = 128790;
-- (서브 쿼리를 이용해 하나의 SELECT문으로 만들기)
SELECT * FROM 고객
WHERE 마일리지 = (SELECT MAX(마일리지) 가장높은마일리지 FROM 고객);

-- 주문번호 'H0250' 의 고객회사명과 담당자명을 조회
-- 조인을 사용
SELECT 고객회사명, 담당자명
FROM 고객 JOIN 주문
USING(고객번호)
WHERE 주문번호 = 'H0250';
-- 서브 쿼리를 사용
SELECT 고객회사명, 담당자명 FROM 고객
WHERE 고객번호 = (SELECT 고객번호 FROM 주문
WHERE 주문번호 = 'H0250');

-- 청운 유통의 주문번호를 조회
-- 1 조인을 사용
SELECT 주문번호
FROM 주문 JOIN 고객
USING (고객번호)
WHERE 고객회사명 = '청운유통';
-- 2 서브쿼리를 사용
SELECT 주문번호 FROM 주문
WHERE 고객번호 = (SELECT 고객번호 FROM 고객
WHERE 고객회사명 = '청운유통');

-- 6-3
SELECT 담당자명, 고객회사명, 마일리지 FROM 고객
WHERE 마일리지 >= (SELECT MIN(마일리지) FROM 고객
WHERE 도시 = '부산광역시');

-- 부산광역시 거주 고객이 주문한 주문 건수 조회
SELECT count(주문번호) 주문건수 FROM 주문
WHERE 고객번호 IN (SELECT 고객번호 FROM 고객
WHERE 도시 = '부산광역시');

SELECT * FROM 고객
WHERE 도시 = '부산광역시';

SELECT COUNT(주문번호) 주문건수 FROM 주문;

-- 부산광역시 거주 고객의 전체 마일리지보다
-- 더 많은 마일리지를 가진 고객 조회
-- ANY : 서브 쿼리 결과 중 하나라도 결과를 만족하면 참
-- 즉, 최소 ~ 값보다 클 경우를 조회
-- ALL : 서브 쿼리 결과 중 모든 결과를 만족하면 참
-- 즉. 최대 어떤 값 보다 클 경우를 조회
-- SELECT 고객회사명, 마일리지 FROM 고객
-- WHERE 마일리지 > ANY (SELECT 마일리지 FROM 고객
-- WHERE 도시 = '부산광역시') ;
-- ONE COMPILER , POSTGRE SQL로 실행
-- 바탕화면 고객 TXT 노트패드로 실행 후 붙어넣기 하고 위 코드 붙여넣기 실행
-- SELECT 고객회사명, 마일리지 FROM 고객
-- WHERE 마일리지 > ALL (SELECT 마일리지 FROM 고객
-- WHERE 도시 = '부산광역시') ;

-- 한번이라도 주문한 적이 있는 고객을 조회
-- JOIN 사용 두 테이블을 결합하고 추려야 하기 때문에 메모리 소모가 큼
SELECT DISTINCT 고객번호, 고객회사명 FROM 고객 JOIN 주문
USING (고객번호);
-- 서브 쿼리 실행 결과가 너무 많은 경우 조회 성능이 나쁨
SELECT 고객번호, 고객회사명 FROM 고객
WHERE 고객번호 IN (SELECT DISTINCT 고객번호 FROM 주문);
-- SQL의 일반적인 실행 순서
-- FROM - IN - JOIN - WHERE - GROUP BY - HAVING - SELECT - ORDER BY
-- EXISTS가 포함된 SQL의 실행 순서
-- SELECT - SUBQUERY - WHERE
-- 조인이나 IN 연산자보다 성능은 좋음
SELECT 고객번호, 고객회사명 FROM 고객 C
WHERE EXISTS (SELECT 고객번호 FROM 주문 O
WHERE O.고객번호 = C.고객번호);
    -- 81 > 82 > 83번 줄 순으로 실행

-- 점검문제
-- 1
SELECT 부서명 FROM 부서
WHERE 부서번호 = (SELECT 부서번호 FROM 사원
       WHERE 이름 = '배재용');

-- 2 주문, 주문세부, 제품
-- 한번이라도 주문한 적이 있는 제품 조회
SELECT DISTINCT 제품명
FROM 주문 JOIN 주문세부
USING(주문번호)
    JOIN 제품
USING (제품번호);

SELECT 제품명 FROM 제품
WHERE 제품번호 IN (
SELECT DISTINCT 제품번호 FROM 주문세부
WHERE 주문번호 IN (
SELECT 주문번호 FROM 주문));

SELECT 제품명 FROM 제품 P
WHERE EXISTS(SELECT 제품번호 FROM 주문세부 OD
WHERE P.제품번호 = OD.제품번호 AND EXISTS(
    SELECT 주문번호 FROM 주문 O
        WHERE O.주문번호 = OD.주문번호));

-- 한번이라도 주문한 적이 없는 제품 조회
SELECT DISTINCT 제품명
FROM 주문 RIGHT JOIN 주문세부
USING(주문번호)
RIGHT JOIN 제품
USING (제품번호)
WHERE 주문번호 IS NULL;

SELECT 제품명 FROM 제품
WHERE 제품번호 NOT IN (
SELECT DISTINCT 제품번호 FROM 주문세부
WHERE 주문번호 IN (
SELECT 주문번호 FROM 주문));

SELECT 제품명 FROM 제품 P
WHERE NOT EXISTS(SELECT 제품번호 FROM 주문세부 OD
WHERE P.제품번호 = OD.제품번호 AND EXISTS(
    SELECT 주문번호 FROM 주문 O
    WHERE O.주문번호 = OD.주문번호));