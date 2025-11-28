# oracle
# 기업용 관계형 데이터베이스
# 파이썬에서 oracle 사용하려면 해당 드라이버 설치 필요
# pip install oracledb

# oracle 11g를 파이썬에서 사용하려면 Thick mode 설정 필요,
# 따라서, oracle instant client 설치하고 path 환경변수 설정함
# https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html#id2

import sys
import oracledb

# instant client 초기화 -  user_guide 2.5.2.1.1
# vs 2019 재배포 패키지 필요 user_guide 2.5.2.1
oracledb.init_oracle_client(lib_dir=r"C:\Java\instantclient_21_3")

try:
    conn = oracledb.connect(user='helloworld',password='beautifulworld',
                            port=1521, dsn ='54.180.130.250:1521/XE')
    print('연결성공')
    conn.close()
except oracledb.Error as ex:
    print(f'연결실패{ex}')
    sys.exit(-1)

# insert 테스트
# 위치 기반 바인딩 - :1, :2, :3 , :4
# 이름 기반 바인딩 - :id , :company, :addr, :tel
sql1 = 'insert into 배송업체 values (:1,:2,:3,:4)'
# sql2 = 'insert into 배송업체 values (:id , :company, :addr, :tel)'

try:
    conn = oracledb.connect(user='helloworld',password='beautifulworld',
                            port=1521, dsn ='54.180.130.250:1521/XE')
    curses = conn.cursor()
    curses.execute(sql1,(111,'2222','3333','44444',))
    conn.commit()
    print('배송업체 데이터 추가')
    conn.close()
except oracledb.Error as ex:
    print(f'연결실패{ex}')
    sys.exit(-1)