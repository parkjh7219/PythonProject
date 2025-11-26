# 성적 처리프로그램 V6용 모듈

import logging as log
import os
import sqlite3

menus = f'''
-------------------
 성적처리 프로그램 V9
-------------------
1. 성적데이터 입력
2. 성적데이터 조회
3. 성적데이터 상세조회
4. 성적데이터 수정
5. 성적데이터 삭제
0. 프로그램 종료
-------------------
작업을 선택하세요 : '''

header1 = '''
이름    국어    영어    수학
========================
'''

header2 = '''
이름   국어   영어   수학   총점   평균   학점
========================================
'''

dbfile = 'sungjuk.db'

def sungjuk_logging():
    """ 로깅 설정을 초기화하는 함수"""
    log.basicConfig(
        filename = 'sungjukv9.log',
        level= log.INFO , encoding= 'utf-8',
        format = '%(asctime)s %(levelname)s --- %(message)s'
    )

def input_sungjuk():
    """
    성적 데이터를 입력받는 함수

    :return:
    """
    log.info('input_sungjuk 호출됨')
    try:
        name = input(f'이름을 입력하세요 : ')
        kor = int(input(f'국어 점수를 입력하세요 : '))
        eng = int(input(f'영어 점수를 입력하세요 : '))
        mat = int(input(f'수학 점수를 입력하세요 : '))
    except ValueError:
        # print('점수는 숫자만 입력 가능합니다')
        log.error('점수는 숫자만 입력가능합니다')
        name, kor, eng, mat = '0',0,0,0

    return name, kor, eng, mat


def compute_sungjuk(name, kor, eng, mat):
    """
    성적 데이터에 대한 총점,평균,학점 처리

    :return:
    """
    tot = kor + eng + mat
    avg = tot / 3
    grd = ('A' if (avg >= 90) else
           'B' if (avg >= 80) else
           'C' if (avg >= 70) else
           'D' if (avg >= 60) else 'F')

    log.info('compute_sungjuk 호출됨')

    return [name, kor, eng, mat, tot, avg, grd]


def add_sungjuk(sj):
    """
    처리한 성적데이터를 리스트에 추가
    """
    sql = '''insert into sungjuk (name,kor,eng,mat,tot,avg,grd)
          values (?,?,?,?,?,?,?)'''

    if os.path.exists(dbfile):
        conn = sqlite3.connect(dbfile)
        print('add_sungjuk - DB 연결 성공!!')
    
        cursor = conn.cursor()
        cursor.execute(sql, (sj[0],sj[1],sj[2],sj[3],sj[4],sj[5],sj[6]))
        conn.commit()
        print('add_sungjuk - 성적 데이터 추가 완료')
    
        conn.close()
    else:
        print('add_sungjuk - DB 연결 실패 , 파일이 존재하지 않음')
    
    log.info('add_sungjuk 호출됨 ')


def readall_sungjuk():
    """
    저장된 성적데이터 중 이름/국어/영어/수학만 출력
    """
    result = ''
    sungjuks =[]
    for sjno, name, kor, eng, mat, tot, avg, grd in sungjuks:
        result += f'{sjno:3d} {name:5s} {kor:4d} {eng:4d} {mat:4d}\n'

    print(f'{header1}{result}')
    log.info('readall_sungjuk 호출됨')


def readone_sungjuk():
    """
    이름으로 성적데이터를 조회해서 모두 출력
    """
    result = ''
    sungjuks =[]
    try:
        namekey = input('조회할 학생 이름은?: ')

        for sjno, name, kor, eng, mat, tot, avg, grd in sungjuks:
            if namekey == name:
                result += f'{sjno:3d} {name:5s} {kor:4d} {eng:4d} {mat:4d} ' \
                          f'{tot:4d} {avg:4.2f} {grd:4s}\n'

        print(f'{header2}{result}')
        log.info('readone_sungjuk 호출됨')
    except ValueError as ex:
        print('숫자만 입력하세요')
        log.error(f'readone_sungjuk 오류발생 {type(ex)}')


def modify_sungjuk():
    """
    기존 성적데이터를 새로운 성적데이터로 수정하는 함수
    """

    sungjuks =[]
    result = '해당 학생번호가 존재하지 않아요!!'
    sjno = int(input('수정할 학생 번호는? '))

    for i in range(len(sungjuks)):
        if sjno == sungjuks[i][0]:
            kor = int(input(f'새로운 국어점수는? ({sungjuks[i][2]}): '))
            eng = int(input(f'새로운 영어점수는? ({sungjuks[i][3]}): '))
            mat = int(input(f'새로운 수학점수는? ({sungjuks[i][4]}): '))

            sjone = compute_sungjuk(sungjuks[i][1], kor, eng, mat)
            sjone.insert(0, sjno)
            sungjuks[i] = sjone

            result = '성적 수정이 완료되었습니다!!'
            break

    print(result)
    log.info('modify_sungjuk 호출됨')


def remove_sungjuk():
    """
    특정 학생의 성적데이터를 삭제하는 함수
    """

    sungjuks =[]
    result = '해당 학생번호가 존재하지 않아요!!'
    sjno =  int(input('삭제할 학생 번호는? '))

    for i in range(len(sungjuks)):
        if sjno == sungjuks[i][0]:
            sungjuks.pop(i)
            result = '성적 데이터가 삭제되었습니다!!'
            break

    print(result)
    log.info('remove_sungjuk 호출됨')

