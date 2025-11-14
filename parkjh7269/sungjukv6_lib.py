# 성적 처리 프로그램 v6 용 모듈


menus = f'''
-----------------
성적 처리 프로그램 V6
-----------------

1. 성적 데이터 입력
2. 성적 데이터 조회
3. 성적 데이터 상세 조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료

작업을 선택하세요 : '''

header1 = '''
이름  국어  영어  수학  
====================
'''
header2 = '''
이름  국어  영어  수학  총점  평균  학점
==================================
'''

def input_sungjuk():
    """
    성적 데이터를 입력받는 함수
    :return:
    """
    name = input(f'{1}) 이름을 입력하세요 : ')
    kor = int(input(f'{1}) 국어 점수를 입력하세요 : '))
    eng = int(input(f'{1}) 영어 점수를 입력하세요 : '))
    mat = int(input(f'{1}) 수학 점수를 입력하세요 : '))

    return name, kor, eng, mat

def compute_sungjuk(name, kor, eng, mat):
    """
    성적 데이터에 대한 총점 , 평균 , 학점 처리
    :return: 
    """
    tot = kor + eng + mat
    avg = tot / 3
    grd = ('A' if (avg >= 90) else
           'B' if (avg >= 80) else
           'C' if (avg >= 70) else
           'D' if (avg >= 60) else 'F')
    return [name, kor, eng, mat, tot, avg, grd]

def add__sungjuk(sj,sungjuks):
    """
    처리한 성적 데이터를 리스트에 추가
    :return: 
    """
    # sj = [name, kor, eng, mat, tot, avg, grd]
    # 리스트를 만들지 않으면 20번 줄이 def add__sungjuk(name, kor, eng, mat, tot, avg, grd, sj, sungjuks)
    sungjuks.append(sj)

def readall_sungjuk(sungjuks):
    """
    저장된 성적 데이터 중 이름/국어/영어/수학만 출력
    :param sungjuks: 
    :return: 
    """

    result = ''
    for sj in sungjuks:
        result += f'{sj[0]:3s} {sj[1]:3d} {sj[2]:3d} {sj[3]:3d} \n'

    print(f'{header1}{result}')

def readone_sungjuk(sungjuks):
    """
    이름으로 성적 데이터를 조회해서 모두 출력

    :param sungjuks:
    :return:
    """

    namekey = input('조회할 학생 이름은? : ')

    result = ''

    for name, kor, eng, mat, tot, avg, grd in sungjuks:
        if name == namekey :
            result += f'{name:3s}{kor:3d} {eng:3d} ' \
                      f'{mat:3d} {tot:3d} {avg:.2f} {grd:3s}\n'
    print(f'{header2}{result}')

def modify_sungjuk(sungjuks):
    """
    기존 성적 데이터를 새로운 성적 데이터로 수정하는 함수
    :return:     """
    result = '해당 학생이 존재하지 않아요'
    namekey = input('수정할 학생 이름은? : ')

    # 수정할 학생이 존재하는지 확인
    # sungjuk[i]는 개별 성적 데이터를 가르키는 포인터pointer
    # sungjuk[i] = sjone 라는 코드를 이용해서
    # compute_sungjuk 함수에 의해 새롭게 생성된 sj 객체로 완전히 교체함
    # 즉, sungjuk[i]는 특정 학생의 성적 데이터를 가르키는 인덱스
    # sungjuk[i][j]는 특정 학생 성적 데이터의 특정요소를 가르키는 인덱스
    for i in range(len(sungjuks)):
        if namekey == sungjuks[i][0] :
            kor = int(input(f'새로운 국어 성적을 입력하세요'))
            eng = int(input(f'새로운 영어 성적을 입력하세요'))
            mat = int(input(f'새로운 수학 성적을 입력하세요'))

            sjone = compute_sungjuk(sungjuks[i][0], kor, eng, mat)
            sungjuks[i] = sjone

            result = '성적 수정이 완료되었습니다'
            break

    print(result)

def remove_sungjuk(sungjuks):
    """
    특정 학생의 성적 데이터를 삭제하는 함수
    :return:
    """

    result = '해당 학생이 존재하지 않아요'
    namekey = input('삭제할 학생 이름은? : ')

    for i in range(len(sungjuks)):
        if namekey == sungjuks[i][0] :
            sungjuks.pop(i)

            result = '성적 수정이 완료되었습니다'
            break

    print(result)