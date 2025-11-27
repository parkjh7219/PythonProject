# 성적 처리프로그램 V9
# 학생의 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력 - 학생번호도 추가
# 성적처리의 CRUD를 메뉴식으로 구현
# 성적 데이터를 sungjuk.csv파일에 저장
# 성적처리 CRUD 기능 함수로 구조화 : 모듈명 sungjukv9_lib
#


from parkjh7269.sungjukv9_lib import menus, sungjuk_logging
from parkjh7269.sungjukv9_lib import input_sungjuk, compute_sungjuk, add_sungjuk
from parkjh7269.sungjukv9_lib import readall_sungjuk
from parkjh7269.sungjukv9_lib import readone_sungjuk
from parkjh7269.sungjukv9_lib import modify_sungjuk
from parkjh7269.sungjukv9_lib import remove_sungjuk

# sungjik 테이블

# create table sungjuk(
#   sjno integer primary key aytoincrement,
#   name varchar(10) not null,
#   kor int,
#   eng int,
#   mat int,
#   tot int,
#   avg float,
#   grd char(1),
#   regdate datetime default current_timestamp
#)

sungjuk_logging()

while True:
    job = input(menus)

    match job:
        case '1':
            name,kor,eng,mat = input_sungjuk()
            if name != '0':
                sj = compute_sungjuk(name, kor, eng, mat)
                add_sungjuk(sj) # sungjuk 테이블에 성적 추가
        case '2':
            readall_sungjuk()

        case '3':
            readone_sungjuk()

        case '4':
            modify_sungjuk()

        case '5':
            remove_sungjuk()

        case '0':
            print('성적프로그램을 종료합니다...')
            break

        case _: print('번호를 잘못입력하셨습니다!')