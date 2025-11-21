-- 고객 : 거주 도시가 '광역시'인 고객 조회
-- like : 특정 문자열이 부분적으로 일치할 때 검색되게 하는 연산자
select * from 고객
where 도시 like '%광역시'
order by 도시;

-- 고객 : 고객 번호 두 번째나 세 번째 글자가 'c'인 고객 조회
select * from 고객
where 고객번호 like '_C%' or 고객번호 like '__C%'
order by 고객번호;

-- 고객 : 거주 도시가 '광역시'이면서
-- 고객번호 두 번째나 세 번째 글자가 'c'인 고객
select * from 고객
where 도시 like '%광역시'and
      (고객번호 like '_C%' or 고객번호 like '__C%');

-- 고객 : 고객회사명에 '푸드'가 포함된 고객 조회
select * from 고객
where 고객회사명 regexp '%푸드%'
order by 고객회사명;

-- 고객 : 전화번호 뒷자리가 '45'인 고객 조회
select * from 고객
where 전화번호 like '%45';

-- 고객 : 전화번호 중 뒤에서 세 번째 자리가 '45'인 고객 조회
select * from 고객
where 전화번호 like '%45_';

-- 고객 : 전화번호에 '45'가 포함된 고객 조회
select * from 고객
where 전화번호 like '%45%';