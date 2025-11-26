-- 집계함수 난생처음 3번 p55

-- 집계함수
-- 여러 행으로 이루어진 데이터를 하나의 요약된 값으로 계산해 주는 함수
-- 통계, 데이터 분석에 자주 사용되는 함수
-- count, sun, avg, max, min
-- 주로 그룹별 분석(group by절)과 함께 사용

select 마일리지 from 고객;

select count(마일리지) 고객수 from 고객; -- 첫 번째 방식 권장
select count(*) 고객수2 from 고객;

-- count 함수 적용 시 null은 제외
-- 또한, 중복까지 포함해서 갯수 파악


-- 예제 4-1, 4-2
select
    count(고객번호),
    count(도시),
    count(distinct 도시) 조정된도시수,
    count(지역)
from 고객;

select
    sum(마일리지),
    round(avg(마일리지),1),
    min(마일리지),
    max(마일리지)
from 고객;

-- 서울특별시 고객에 한해 마일리지 합/평균/최대/최소 조회

select
    sum(마일리지),
    round(avg(마일리지),1),
    min(마일리지),
    max(마일리지)
from 고객
where 도시 = '서울특별시';

-- group by 절
-- 테이블의 데이터를 특정 컬럼을 기준으로 그룹화하고,
-- 각 그룹마다 집계함수를 적용하는 구문
-- 즉, 같은 값끼리 묶어서 요약할 때 사용
-- select 컬럼1, 집계함수(컬럼2) -- 컬럼1만 올 수 있음, 컬럼2를 쓰고 싶다면 집계삼수를 써야 함
-- from 테이블
-- group by 컬럼1

-- 도시별 고객수 조회
-- 그룹별 조회 시 컬럼명 대신 select 절에 나열된 컬럼 순번을 지정
select 도시, count(고객번호) 고객수
from 고객
group by 1;

select 도시, count(고객번호) 고객수
from 고객
group by 도시
order by 고객수 desc;

-- 도시별 고객수, 평균 마일리지 조회
select
    도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
group by 도시
order by 고객수 desc;

-- 담장자 직위별 도시별 고객수, 평균 마일리지 조회
select
    담당자직위, 도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
group by 담당자직위, 도시
order by 담당자직위, 고객수 desc;

-- 4-6
-- 도시별 고객수, 평균 마일리지 조회 단, 고객수가 10명 이상일 경우만 조회

select
    도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
group by 도시
having 고객수 >= 10
order by 담당자직위, 고객수 desc;

-- 도시별 고객수, 평균 마일리지 조회
-- 단, 고객수가 5명 이상이고 평균 마일리지가 3500 이상일 경우만 조회
select
    도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
group by 도시
having 고객수 >= 5 and 평균마일리지 >= 3500
order by 담당자직위, 고객수 desc;

-- 도시별 고객수 , 평균 마일리지 조회
-- 단, 서울특별시에 거주하는 고객만 대상으로 조회
select
    도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
group by 도시
having 도시 = '서울특별시'
order by 고객수 desc; -- 다소 비효율적

select
    도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
where 도시 = '서울특별시'
group by 도시
order by 고객수 desc; -- 효율적

-- 실행 계획
-- explain query plan
-- 쿼리가 어떻게 실행될 지 SQLite가 예측해서 보여주는 명령
-- 실제 성능을 높이거나 , 불필요한 전체 데이터 스캔을 줄이는데 유용
explain query plan
select
    도시, count(고객번호) 고객수,
    round(avg(마일리지),2) 평균마일리지
from 고객
group by 도시
having 도시 = '서울특별시'
order by 고객수 desc;

-- 예제 4-7
select 도시, sum(마일리지) 마일리지총합
from 고객
-- where leftstr(고객번호,1) = 'T'
where 고객번호 like 'T%'
group by 도시
having 마일리지총합 >= 1000
order by 마일리지총합 desc;

-- 점검문제 1
select count(도시),
       count(distinct 도시)
from 고객;

-- 점검문제 2
select
    leftstr(주문일, 4) 주문년도,
    count(주문번호) 주문건수
from 주문
group by leftstr(주문일, 4);

-- 점검문제 4
select
    -- 요청일, 발송일,
    substr(주문일, 6, 2) 주문월,
    count(주문번호) 주문건수
from 주문
where 요청일 < 발송일
group by 주문월
order by 주문월;

-- 점검문제 5
select
    제품명, sum(재고) 재고합
from 제품
where 제품명 like '%아이스크림'
group by 제품명;