# 성적 처리프로그램 V4
# 3명의 학생의 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력 - 학생 번호도 추가
# 성적 처리의 CRUD를 메뉴식으로 구현
# 성적 데이터를 sungjuk.csv 파일에 저장
#   1. 혜교 99,98,99,297,99.98,A
#   2. 지현 33,44,55,197,77.82,C
#   3. 수지 77,88,99,235,85.99,B
# 성적처리 CRU 기능 함수로 구조화 : 모듈명 sungjukv7_lib

from parkjh7269.sungjukv7_lib import menus
from parkjh7269.sungjukv7_lib import header1
from parkjh7269.sungjukv7_lib import header2

from parkjh7269.sungjukv7_lib import input_sungjuk, compute_sungjuk, add__sungjuk
from parkjh7269.sungjukv7_lib import readall_sungjuk
from parkjh7269.sungjukv7_lib import readone_sungjuk
from parkjh7269.sungjukv7_lib import modify_sungjuk
from parkjh7269.sungjukv7_lib import remove_sungjuk

from parkjh7269.sungjukv7_lib import write_sungjuk
from parkjh7269.sungjukv7_lib import load_sungjuk

# 성적데이터가 저장된 sungjuk.csv로부터 저장된 성적 데이터를 모두 읽어
# sungjuk 변수에 저장
sungjuks = load_sungjuk()  # 성적 데이터 저장용 변수

while True:
    job = input(menus)

    match job:
        case '1':
            name, kor, eng, mat = input_sungjuk()
            sj = compute_sungjuk(name, kor, eng, mat)
            add__sungjuk(sj,sungjuks)

            # sungjuks 변수에 저장된 모든 성적데이터들을 sungjuk.csv에 저장
            write_sungjuk(sungjuks)

        case '2':
            readall_sungjuk(sungjuks)

        case '3':
            readone_sungjuk(sungjuks)

        case '4':
            modify_sungjuk(sungjuks)
            write_sungjuk(sungjuks)

        case '5':
            remove_sungjuk(sungjuks)
            write_sungjuk(sungjuks)

        case '0':
            print('성적 처리 프로그램을 종료합니다.')
            break
        case _:
            print('번호를 잘못 입력하셨습니다.')