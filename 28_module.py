# 모듈
# 파이썬 코드가 포함된 파일
# 즉, 변수, 함수, 클래스 등을 하나의 파일에 담은 것
# 따라서, 이미 만든 기능을 다른 파일에서 다시 사용 가능
# 코드를 기능별로 파일 단위로 나누면 관리가 수월함

# 파이썬 표준 모듈
# 파이썬에서 기본적으로 제공하는 모듈들
# math, random, datetime, os, sys 등등
# 파이썬 셸에서 dir(모듈명) 실행 시 함수 / 상수 조회가능

# 외부 모듈 - 3rd party
# pip install 로 설치해야 사용 가능 - 픽픽 확인 , 가상 환경에서만 실행할 것

# 모듈 생성
# 임의의 패키지 디렉토리 아래에 기능을 의미하는 이름으로 py 파일 작성

# 모듈 가져오기 1
# import 모듈파일명

import parkjh7269.sayhello

# 모듈 기능 호출 1
# 모듈파일명.함수명,
# 모듈파일명.변수명
print(parkjh7269.sayhello.msg)
parkjh7269.sayhello.greeting()

# 모듈 가져오기 2
# import 모듈 파일명 as 별칭
import parkjh7269.sayhello as sh

# 모듈 기능 호출 2
# 별칭.함수명, 별칭.변수명

print(sh.msg)
sh.greeting()

# 모듈 가져오기 2b
# import 모듈 파일명 as 별칭
import parkjh7269.sayhello as sayhello

# 모듈 기능 호출 2
# 별칭.함수명, 별칭.변수명

print(sayhello.msg)
sh.greeting()


# 모듈 가져오기 3 (추천!)
# from 패키지.모듈 파일명 import 함수명/변수명 # 2번은 parkjh7269의 모든 함수 변수를 가져옴
from parkjh7269.sayhello import greeting # greeting만 가져오겠다
from parkjh7269.sayhello import msg # msg만 가져오겠다
# from parkjh7269.sayhello import greeting, msg # 붙여 쓸 수도 있지만 가독성이 떨어져 많이 쓰이지 않음

# 모듈 기능 호출 3
# 함수명, 변수명

print(msg)
greeting()