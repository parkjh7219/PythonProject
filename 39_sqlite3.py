# sqlite3
# 경량급 관계형 데이터베이스
# 서버 없이 단일 파일(.db)로 동작 - 설치 간단, 설정도 없음
# 보통 장치에 내장되어 동작하는 데이터베이스
# 표준 sql 쿼리 대부분 지원 - 일부는 지원하지 않음

# 파이썬에는 sqlite3를 위한 모듈이 기본적으로 지원

import os
import sqlite3

# 1. 데이터베이스 연결
# 파일이 없을 경우 디비 파일 바로 생성 - 이것을 방지하려면 exists 함수 사용
# sqlite3.connect(디비파일명)
# conn = sqlite3.connect('PythonProject.db')
# cursor = conn.cursor()

# 데이터베이스 연결 종료
# conn.cursor()

dbfile = 'C:/Users/rotlqkf/PycharmProjects/PythonProject.db' # 존재하지 않는 파일 ############ 파이썬.pr

#디비 파일 존재 여부 검사
if os.path.exists(dbfile):
    conn = sqlite3.connect(dbfile)
    print('DB연결 완료')

    # 2. 데이터베이스 처리 객체인 커서를 하나 생성
    cursor = conn.cursor()

    # 3. 학생 데이터 추가
    # 쿼리 실행 : 커서객체.excute(쿼리)
    # sql = '''INSERT INTO 학생2 (학번, 이름, 주소, 생년월일, 학과명, 교수)
    #          VALUES (2025112614, '아서스', '경기도 고양시',1985-03-22,  '디아블로4', 999)'''

    hakbun = int(input('학번은?'))
    name = input('이름은?')
    addr = input('주소는?')
    birth = input('생년월일은?')
    dept = input('학과명은?')
    prof = int(input('교수번호는?'))

    # sql 인젝션 공격 빌미 제공
    # sql = f''' insert into 학생2 (학번, 이름, 주소, 생년월일, 학과명, 교수)
    #         values ({hakbun},'{name}','{addr}','{birth}','{dept}','{prof}')'''
    # 
    # cursor.execute(sql)

    # 쿼리에 삽입될 값을 placeholder 로 지정
    sql = f'''insert into 학생2 (학번, 이름, 주소, 생년월일, 학과명, 교수)
        values (?,?,?,?,?,?)'''
    cursor.execute(sql,(hakbun,name, addr, birth, dept, prof))
    
    print('학생 데이터 추가 완료')

    # 변경 사항 저장
    # insert, update, delete 명령 시 commit 필요 !
    conn.commit()

    # 데이터베이스 연결 종료
    conn.close()    
    
else:
    print('DB 연결 실패 - 파일이 존재하지 않음')


if os.path.exists(dbfile):
    # 데이터베이스 연결
    conn = sqlite3.connect(dbfile)
    print('DB 연결 성공')
    
    # 커서 생성
    cursor = conn.cursor()

    # 쿼리 작성 후 실행
    sql = 'select * from 학생2 where 이름 = ?'
    name = input('조회할 학생 이름은?')
    cursor.execute(sql, (name)) # 튜플로 작성
    
    # 실행한 쿼리의 결과집합을 받아옴 - 한개만 존재할 경우
    row = cursor.fetchallone()

    # 결과집합을 적절한 형태로 출력
    if row:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}')
    else:
        print('데이터가 존재하지 않아요')
    
    # 데이터베이스 연결 종료
    conn.close()

else:
    print('DB 연결 실패 - 파일이 존재하지 않음')