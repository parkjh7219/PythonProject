-- 조인
-- 두 개 이상의 테이블을 연결해서 관련 데이터를 함께 조회할 때 사용하는 기능
-- 함께 조회할 때 사용하는 기능
-- 조인 할 테이블들은 보통 키를 기준으로 서로 관련되어 있음
-- 주문과 고객 : 고객번호로 서로 관련됨

-- 조인 종류 : 보통 키를 조건으로 테이블을 조인함
-- 크로스(cross) 조인(join) : 조건 없이 모든 행의 조합 생성. 각 테이블을 ,로 조합
-- 이너(inner) 조인 : 양쪽 테이블에서 조건이 맞는 데이터만 조회(교집합), inner join 키워드 사용
-- 아우터(outer) 조인 : 조인 조건에 맞지 않는 데이터도 결과에 포함시키는 조인
--                   즉, 한쪽 테이블에만 존재하는 데이터도 NULL을 채워서 보여줌
--                   누락없이 기존 테이블의 모든 행을 보고싶을 때 사용
-- 크로스(self) 조인
-- NETVI 주문고객의 이름 고객회사, 주소, 전화번호 조회 (크로스 조인)
select 고객회사명, 주소, 전화번호
from 주문, 고객
where 주문.고객번호 = 'NETVI'
order by 주문번호;

select 고객회사명, 주소, 전화번호
from 주문 join 고객
where 주문.고객번호 = 'NETVI'
order by 주문번호;

-- NETVI 주문고객의 고객회사 이름, 주소, 전화번호 조회 (이너조인 조인)
select 고객회사명, 주소, 전화번호
from 주문 inner join 고객
where 주문.고객번호 = 고객.고객번호 and 고객. 고객번호 = 'NETVI';

select 고객회사명, 주소, 전화번호
from 주문 join 고객
where 주문.고객번호 = 고객.고객번호 and 고객.고객번호 = 'NETVI';

select 고객회사명, 주소, 전화번호
from 주문 inner join 고객
on 주문.고객번호 = 고객.고객번호
where 고객.고객번호 = 'NETVI';

select 고객회사명, 주소, 전화번호
from 주문 join 고객
using(고객번호)
where 고객.고객번호 = 'NETVI';

-- 예제 5-2
select 사원번호, 직위, 사원.부서번호, 부서명
from 사원 inner join 부서
using(부서번호)
where 이름 = '이소미';

-- 예제 5-3
-- 고객회사별로 주문한 주문건수 조회
-- 단, 주문건수를 내림차순 정렬해서 보여줌
select 고객회사명, count(주문번호) 주문건수
from 고객 join 주문
using (고객번호)
group by 고객회사명
order by 주문건수 desc;

-- 고객회사별로 주문한 주문금액의 총합 조회
-- 단, 주문금액의 총합을 내림차순 정렬해서 보여줌
-- A join B using (AB컬럼) join C using (BC/AC컬럼)

select
    고객회사명,   sum(단가 * 주문수량) 주문금액총합
from 주문
    join 고객
    using (고객번호)
    join 주문세부
    using (주문번호)
group by 고객회사명
order by 주문금액총합 desc;

-- 사원의 이름, 성별, 입사일, 부서명 조회
-- 단, 부서명이 없는 사원도 같이 조회

SELECT 이름, 성별, 입사일, 부서명
FROM 사원 LEFT OUTER JOIN 부서
USING(부서번호);

-- 사원의 이름, 성별, 입사일, 부서명 조회
-- 단, 부서명이 없는 사원을 조회

select
    이름, 성별, 입사일, 부서명
from 사원 left outer join 부서
on 사원.부서번호 = 부서.부서번호
where 부서.부서명 is null;

-- 주문을 한번도 하지 않은 고객의 회사명, 담당자명, 전화번호

SELECT 고객회사명, 담당자명, 전화번호
FROM 고객 LEFT OUTER JOIN 주문
ON 고객.고객번호 = 주문.고객번호
WHERE 주문.고객번호 IS NULL;

SELECT * FROM 고객;
SELECT * FROM 주문;
SELECT * FROM 고객;




select 고객회사명, 담당자명, 전화번호, 주문번호
from 고객 left outer join 주문
using (고객번호)
where 주문번호 is null;

