# mariadb
# mysql 에서 파생된 오픈 소스 관계형 데이터베이스
# oracle이 mysql을 인수하면서 상업화 될 위기에 처함에 따라
# mysql 창시자가 mysql 소스를 기반으로
# maria db라는 독립적인 오픈소스 데잍터베이스를 만듬
# 따라서 , mysql와 100% 호환, 심지어 mysql보다 성능이 좋음

# 파이썬에서 mariadb를 사용하려면 해당 드라이버 설치 필요
# pip install mariadb

import sys
import mariadb

# 데이터베이스 연결
try:
    conn = mariadb.connect(user='helloworld',password='parkjh7269',host='43.203.150.161',
                            port=3306, database ='helloworld')
    print('연결성공')
    conn.close()
except mariadb.Error as ex:
    print(f'연결실패{ex}')
    sys.exit(-1)

# insert 테스트
sql = 'insert into 배송업체 values (?,?,?,?)'

try:
    conn = mariadb.connect(user='helloworld',password='parkjh7269',host='43.203.150.161',
                           port=3306, database ='helloworld')
    curses = conn.cursor()
    curses.execute(sql,(111,'2222','3333','44444',))
    conn.commit()
    print('배송업체 데이터 추가')
    conn.close()
except mariadb.Error as ex:
    print(f'연결실패{ex}')
    sys.exit(-1)