# 성적 처리프로그램 V4
# 3명의 학생의 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 성적 처리의 CRUD를 메뉴식으로 구현

# CRUD : 데이터의 추가 조회 수정 삭제

menus = f'''
-----------------
성적 처리 프로그램 V4
-----------------

1. 성적 데이터 입력
2. 성적 데이터 조회
3. 성적 데이터 상세 조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료

작업을 선택하세요 : '''

header = '''
이름  국어  영어  수학  총점  평균  학점
==================================
'''

while True:
    job = input(menus)

    match job:
        case '1':
            name = input(f'{1}) 이름을 입력하세요 : ')
            kor = int(input(f'{1}) 국어 점수를 입력하세요 : '))
            eng = int(input(f'{1}) 영어 점수를 입력하세요 : '))
            mat = int(input(f'{1}) 수학 점수를 입력하세요 : '))

            tot = kor + eng + mat
            avg = tot / 3
            grd = ('A' if (avg >= 90) else
                   'B' if (avg >= 80) else
                   'C' if (avg >= 70) else
                   'D' if (avg >= 60) else 'F')
            print('입력한 데이터 대해 성적처리가 완료되었습니다')

        case '2':
            result = f'{name:3s}{kor:3d} {eng:3d} '\
                       f'{mat:3d} {tot:3d} {avg:.2f} {grd:3s}\n'
            print(f'{header}{result}')

        case '3': print ('성적 데이터 상세 조회를 진행합니다.')
        case '4': print ('성적 데이터 수정을 진행합니다.')
        case '5': print ('성적 데이터 삭제를 진행합니다.')
        case '0':
                print ('성적 처리 프로그램을 종료합니다.')
                break
        case _: print('번호를 잘못 입력하셨습니다.') # _는 위 번호 외 나머지