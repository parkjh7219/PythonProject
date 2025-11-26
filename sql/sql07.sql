-- 공유 5번 p43

-- DDL
-- 데이터 정의어 : 테이블, 스키마, 인덱스 등의
--              데이터 구조를 정의하고 수정하는 SQL 명령
-- CREATE : 데이터베이스 객체(테이블, 뷰, 인덱스, 스키마) 생성 명령
-- ALTER : 기존 객체의 구조 변경
-- DROP : 기존 객체 제거 명령

-- 스키마 SCHEMA
-- 데이터베이스 내 객체의 구조와 구성을 의미
-- 데이터가 어떻게 저장될 지 정하는 ㅌ틀, 설계도를 의미
-- 구조, 관계, 제약 조건 등이 포함

-- 테이블 생성
-- 학번, 이름, 주소, 생년원일, 학과명, 교수로 구성된 학생 테이블 생성

CREATE TABLE 학생(
    학번      INT,
    이름      VARCHAR(10) NOT NULL,
    주소      VARCHAR(100) NOT NULL,
    생년월일   DATETIME NOT NULL,
    성별      CHAR(2) NOT NULL CHECK(성별 IN('남','여')),
    학과명     VARCHAR(50),
    교수      INT DEFAULT 0,
--    마일리지   INT DEFAULT 0,
    PRIMARY KEY (학번)
);

-- INSERT , P 7

-- INSERT
-- 테이블에 새로운 데이터를 추가하는 명령
-- INSERT INTO 테이블 명 (컬럼1, 컬럼2 . . .)
-- VALUES (값1, 값2 . . . )
-- 데이터 추가 시 컬럼과 값 순서를 맞춰야 함
--
INSERT INTO 학생(학번, 이름, 주소, 생년월일, 성별, 학과명, 교수)
VALUES (201350050, '김태희', '경기도 고양시',
        1985-03-22, '여', '컴퓨터', 504);

-- 데이터 추가 시 마일리지 컬럼 제외 - DEFAULT 제약조건이 설정되어 있기 때문
INSERT INTO 학생(학번, 이름, 주소, 생년월일, 성별, 학과명, 교수)
VALUES (201250006, '송혜교', '서울 영등포구',
        '1988-09-17', '여', '컴퓨터', 301);

SELECT * FROM 학생;

INSERT INTO 학생 (학번, 이름, 주소, 생년월일, 성별, 학과명, 교수)
VALUES (201252110,'전지현','경기도 의정부시','1986-4-30', '여','의상디자인',445);

INSERT INTO 학생 (학번, 이름, 주소, 생년월일, 성별, 학과명, 교수)
VALUES (201351010,'수지','서울 성북구','1988-7-13', '여','식품영양',556);

INSERT INTO 학생(학번, 이름, 주소, 생년월일, 성별, 학과명, 교수)
VALUES (201353011,'아이유','경기도 천안시','1987-2-25', '여','철학',504);

SELECT * FROM 학생;

-- 학과명, 전화번호, 사무실위치, 학과장으로 구성된 학과 테이블 생성

create table 학과(
    학과명 varchar(10) ,
    전화번호  varchar(13) unique not null ,
    `사무실 위치` varchar(8) not null ,
    학과장 int not null,

    primary key (학과명)
);

-- 테이블에 모든 컬럼에 값을 입력하는 경우
-- 컬럼 목록은 생략 가능
insert into 학과(학과명, 전화번호, `사무실 위치`, 학과장) -- () 안 생략 가능
values ('컴퓨터공학','123-4567-8901', 'E동 2층',504);

-- 과목번호, 과목명, 과목개요, 담당교수로 구성된 과목 테이블 생성

CREATE TABLE 과목1(
    과목번호 CHAR(4),
    과목명 VARCHAR(15) NOT NULL,
    과목개요 VARCHAR(25) NOT NULL ,
    담당교수 INT NOT NULL ,

    PRIMARY KEY (과목번호)
);

INSERT INTO 과목1 VALUES ('0205','프로그래밍','자바 프로그래밍',301);
INSERT INTO 과목1 VALUES ('0211','드레스 코드','옷 입기의 기초',445);

SELECT * FROM 과목1;

-- 교수 번호, 이름, 전공분야로 구성된 교수 테이블 생성

CREATE TABLE 교수(
    교수번호 INT,
    이름 VARCHAR(10) NOT NULL ,
    전공분야 VARCHAR(25) NOT NULL ,
    PRIMARY KEY (교수번호)
);

INSERT INTO 교수 (교수번호, 이름, 전공분야)
VALUES (301,'이순신','프로그래밍');
INSERT INTO 교수 (교수번호, 이름, 전공분야)
VALUES (445,'정약용','의상디자인');

-- 제약 조건 확인 : DDL

SELECT * FROM sqlite_master;

-- 참조 무결성
-- 부모 테이블에 존재하지 않는 데이터는
-- 자식 테이블이 참조하면 안된다는 규칙
--      자식 테이블이 가르키는 부모 테이블의 값은 항상 실제로 존재하도록 보장하는 장치
-- 두 테이블의 외래키 관계가 올바르게 유지되도록 강제하는 규칙
-- 예) 주문 테이블의 고객 번호는 고객 테이블에 존재하는 고객 번호이다

-- 외래 키 제약 조건 추가
-- FOREIGN KEY (컬럼명)
-- REFERENCES 부모테이블 (컬럼명)
CREATE TABLE 학생2 (
    학번      INT,
    이름      VARCHAR(10) NOT NULL,
    주소      VARCHAR(100) NOT NULL,
    생년월일   DATETIME NOT NULL,
    학과명     VARCHAR(50),
    교수      INT,

    PRIMARY KEY (학번),
    FOREIGN KEY (교수) REFERENCES 교수(교수번호)
);

-- 참조 무결성 테스트

-- INSERT INTO 학생2(학번, 이름, 주소, 생년월일, 학과명, 교수)
-- VALUES (2025112610, '아서스', '경기도 고양시',
--         1985-03-22,  '디아블로4', 999); -- 원 컴파일에서 실행 , 캡쳐 확인

-- 외래키 제약조건 추가 2
-- ALTER TABLE 테이블 명
-- ADD CONSTRAINT 제약 조건 명  외래키 제약 조건
-- ALTER TABLE 학생
-- ADD CONSTRAINT FK_학생
-- FOREIGN KEY (교수) REFERENCES 교수(교수번호); -- 원 컴파일에서 실행 , 캡쳐 확인

-- MARIADB에서 제약조건 조회
-- SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS;
--
-- SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
-- WHERE TABLE_NAME = '학생';

-- 일련번호 컬럼 추가
CREATE TABLE 교수2(
    번호  INTEGER PRIMARY KEY AUTOINCREMENT,
    교수번호 INT,
    이름 VARCHAR(10) NOT NULL ,
    전공분야 VARCHAR(25) NOT NULL
);

INSERT INTO 교수2 (교수번호, 이름, 전공분야)
VALUES (301,'이순신','프로그래밍');
INSERT INTO 교수2 (교수번호, 이름, 전공분야)
VALUES (445,'정약용','의상디자인');

SELECT * FROM 교수2;

CREATE TABLE 학생3 (
    번호      INTEGER PRIMARY KEY AUTOINCREMENT,
    학번      INT,
    이름      VARCHAR(10) NOT NULL,
    주소      VARCHAR(100) NOT NULL,
    생년월일   DATETIME NOT NULL,
    학과명     VARCHAR(50),
    교수      INT,

    FOREIGN KEY (교수) REFERENCES 교수(교수번호)
);

DROP TABLE 학생3;

INSERT INTO 학생3 (학번, 이름, 주소, 생년월일, 학과명, 교수)
VALUES (201350050, '김태희', '경기도 고양시',
        1985-03-22, '컴퓨터', 1);

INSERT INTO 학생3 (학번, 이름, 주소, 생년월일, 학과명, 교수)
VALUES (201250006, '송혜교', '서울 영등포구',
        '1988-09-17', '컴퓨터', 2);

SELECT * FROM 학생3;
SELECT * FROM 교수2;


-- UPDATE
-- 테이블에 존재하는 데이터를 수정할 때 사용하는 명령
-- UPDATE 테이블명
-- SET 수정할 컬럼 = 새로운 값
-- WHERE 조건
--      자동 커밋을 푸세요

-- 송혜교 학생의 생년월일 변경

SELECT * FROM 학생;

UPDATE 학생
SET 생년원일 = '1111-11-11'; -- 캡쳐 확인

ROLLBACK ;

SELECT * FROM 학생;

UPDATE 학생
SET 생년원일 = '1111-11-11'
WHERE 이름 = '송혜교';

SELECT * FROM 학생;

COMMIT;

-- 김태희 학생의 주소, 학과명, 마일리지에 500원 추가한 값으로 변경
UPDATE 학생
SET 주소 = 'XXX', 학과명 = 'YYY' -- , 마일리지 = 마일리지 + 500 (마일리지 안만듬)
WHERE 이름 = '김태희';

SELECT * FROM 학생;

ROLLBACK ;


UPDATE 학생 SET 주소 ='TTT' WHERE 이름 = '송혜교';

SELECT * FROM 학생;

ROLLBACK ;

SELECT * FROM 학생;

-- DELETE
-- 테이블에 존재하는 데이터를 삭제 할 때 사용하는 명령
-- DELETE FROM 테이블명 WHERE 조건
-- 수정 작업 시 트랜잭션 제어를 수동으로 설정할 것을 권장 !

-- 김태희 학생의 정보를 제거
DELETE FROM 학생 WHERE 이름 = '송혜교';

SELECT * FROM 학생;

ROLLBACK;

SELECT * FROM 학생;

DELETE FROM 학생 WHERE 이름 = '김태희';

SELECT * FROM 학생;

ROLLBACK;

SELECT * FROM 학생;

-- 예제 7-5 사원번호가 E10인 사원의 이름을 김레몬으로 변경
-- 직접 만든 예제
SELECT 이름 FROM 사원 WHERE 사원번호 = 'E10' ;

UPDATE 사원
SET 이름 = '김레몬'
WHERE 사원번호 = 'E10';

SELECT * FROM 사원;

-- 제품 번호가 78인 제품의 포장단위를 ' 200 ML BOTTLES' 로 변경
SELECT 포장단위 FROM 제품 WHERE 제품번호 = 78;

UPDATE 제품
SET 포장단위 = '200 ML BOTTLES'
WHERE 제품번호 = 78;

SELECT * FROM 제품;

-- 제품 번호가 78인 제품의 단가를 10 % 인상하고 재고를 -10으로 변경
UPDATE 제품
SET 단가 = ROUND(단가 * 1.1), 재고 = 재고 - 10
WHERE 제품번호 = 78;

-- 제품 번호가 78인 제품을 제거
DELETE FROM 제품
WHERE 제품번호 = 78;

-- 사원들 중 입사일이 가장 늦은 사원의 정보 제거
SELECT 이름 , 입사일 FROM 사원
ORDER BY 입사일 DESC LIMIT 3;

DELETE FROM 사원
ORDER BY 입사일 DESC
LIMIT 3;

DELETE FROM 사원
WHERE 사원번호 IN (SELECT 사원번호 FROM 사원
ORDER BY 입사일 DESC LIMIT 3) ;


select * from 학생2;