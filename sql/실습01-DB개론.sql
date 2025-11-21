select all 제조업체 from 제품2;

select distinct 제조업체 from 제품2;

select 제품명, 단가 '가격' from 제품2;

select 제품명, 단가, 단가 + 500 '조정 단가' from 제품2;

select  * from 고객2 where 나이 is null;

select  * from 고객2 where 나이 is not null;

select  * from 주문2 where 수량 >= 10
order by 주문제품, 수량;

