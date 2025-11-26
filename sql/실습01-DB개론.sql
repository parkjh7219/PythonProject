CREATE TABLE 학과 (
    학과명 VARCHAR(6),
    전화번호 VARCHAR(15),
    '사무실 위치' VARCHAR(7),
    학과장 INT,

    PRIMARY KEY (학과명)
);

INSERT INTO 학과 (학과명, 전화번호, "사무실 위치", 학과장)
VALUES ('컴퓨터공학','123-4567-8901','E동 2층',504);

SELECT * FROM 학과;

CREATE TABLE 과목(
    과목번호 INT,
    과목명 VARCHAR(7),
    과목개요 VARCHAR(20),
    담당교수 INT,
    PRIMARY KEY (과목번호)
);

INSERT INTO 과목(과목번호, 과목명, 과목개요, 담당교수)
VALUES (0205,'프로그래밍','자바 프로그래밍',301);

SELECT * FROM 과목;

CREATE TABLE 교수(
    교수번호 INT,
    이름 VARCHAR(5),
    전공분야 VARCHAR(7),
    PRIMARY KEY (교수번호)
);

INSERT INTO 교수(교수번호, 이름, 전공분야)
VALUES (301,'이순신','프로그래밍');

SELECT * FROM 교수;