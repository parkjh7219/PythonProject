-- 문자 길이 함수 - length, char_length
select length('hello'), length('안녕');

select char_length('hello'), char_length('안녕');

-- 고객 : 도시, 주소 전화번호를 조회
-- 단, 출력 형식은 다음과 같이 지정 : 서울 특별시 송파구 잠실동 220-123-4567-9812

select concat (도시, '', 주소, '', 전화번호) '고객 주소' from 고객;

select concat_ws('', 도시, 주소, 전화번호) '고객 주소' from 고객;

-- 고객 : 거주 도시가 '광역시'인 고객 조회
select * from 고객
where rightstr(도시, 3) = '광역시';

-- 고객 : 고객번호 두 번째나 세 번째 글자가 'c'인 고객 조회
select * from 고객 where substr(고객번호, 2, 1) = 'C'
    or substr(고객번호, 3, 1) = 'C';
--where leftstr(고객번호, 2) = 'C';??

-- 123.56을 round, ceil, floor 함수 적용
select  round(123.56), ceil(123.46), floor(123.56);

-- 난수 생성 : rand
select random(), random(), random(), random(), random();
select abs(random() % 45 ) + 1 '로또 6/45';

-- 현재 날짜, 시간
select current_timestamp, current_date, current_time; -- 로컬 , 지역시간
select date(), time(), datetime(); -- UTC, 표준시

-- 날짜 계산
select julianday('2025-12-25') - julianday('2025-11-22');

-- 날짜 계산
select first_name 사원이름, HIRE_DATE 입사일,
       date(HIRE_DATe + '30 days' ) 첫월급날
from EMPLOYEES;

-- select date (current_date, 'start of month', '+1 month', '-1 day');

-- 0: 일, 1: 월, . . . 6: 토
select strftime('%w', current_date);

-- 예제
-- 1)
select julianday('2025-11-21') - julianday('1997-09-06');

-- 2)
select date('1997-09-06', '+10000 day');

-- 3)
select strftime('%w', '1997-09-06');

-- NULL 다루기 : INFULL
update EMPLOYEES set COMMISSION_PCT = null
where COMMISSION_PCT is '';

select COMMISSION_PCT from EMPLOYEES;

select COMMISSION_PCT, ifnull (COMMISSION_PCT, 0)
from EMPLOYEES;

-- 주문세부 테이블에서 주문금액, 할인금액, 실제 주문금액 조회
-- 단, 모든 금액은 1원 단위로 버림하고 10원 단위까지만 출력 floor(123.56)

select 주문번호, 제품번호, 단가, 주문수량, 할인율, round(할인율, 2) 할인율,
       주문수량 * 단가 주문금액,
       round((주문수량 * 단가 * 할인율) / 10) * 10 할인금액,
       round(((주문수량 * 단가)- (주문수량 * 단가 * 할인율)) / 10) * 10 실주문금액
from 주문세부;

-- 사원 테이블에서 이름, 생일, 만나이, 입사일, 입사일수, 입사한지 500일 후 조회
select  이름, 생일, leftstr('current_time')- leftstr(생일, 4) 나이,
        입사일 , date(입사일 , '+500 day') "500일후"
from 사원;

-- 4번 5번