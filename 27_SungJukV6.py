# 성적 처리프로그램 V4
# 3명의 학생의 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 성적 처리의 CRUD를 메뉴식으로 구현
# 성적 데이터를 시퀀스 자료형에 저장
# 성적 처리 CRUD 기능을 함수로 구조화 : 모듈명 sungjukv6_lib

# sungjuks = [
#     ['혜교', 99, 98, 99, 297, 99.99, 'A'],
#     ['지현', 33, 44, 55, 197, 77.99, 'C'],
#     ['수지', 77, 88, 99, 235, 85.99, 'B'],
# ]

from parkjh7269.sungjukv6_lib import menus
from parkjh7269.sungjukv6_lib import header1
from parkjh7269.sungjukv6_lib import header2

from parkjh7269.sungjukv6_lib import input_sungjuk, compute_sungjuk, add__sungjuk
from parkjh7269.sungjukv6_lib import readall_sungjuk
from parkjh7269.sungjukv6_lib import readone_sungjuk
from parkjh7269.sungjukv6_lib import modify_sungjuk
from parkjh7269.sungjukv6_lib import remove_sungjuk

sungjuks = []  # 성적 데이터 저장용 변수

while True:
    job = input(menus)

    match job:
        case '1':
            name, kor, eng, mat = input_sungjuk()
            sj = compute_sungjuk(name, kor, eng, mat)
            add__sungjuk(sj,sungjuks)

        case '2':
            readall_sungjuk(sungjuks)

        case '3':
            readone_sungjuk(sungjuks)

        case '4':
            modify_sungjuk(sungjuks)

        case '5':
            remove_sungjuk(sungjuks)

        case '0':
            print('성적 처리 프로그램을 종료합니다.')
            break
        case _:
            print('번호를 잘못 입력하셨습니다.')