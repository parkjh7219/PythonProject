# 성적 2번
# 이름 국어 영어 수학 점수를 키보드로 입력받아
# 총점 평균 학점을 처리한뒤 결과 출력
# 단 학점은 삼항연산자를 이용해서 계산한다


# 문자열 비교 - 문자열 풀 pool
# 동일한 문자열 값을 한번만 저장하고 재사용하는 메커니즘

say1 = 'Hello World'
say2 = 'Hello World'
print(say1==say2)
print(id(say1), id(say2)) # 메모리 위치 비교

say3 = str('Hello World')
print(say1==say3)
print(id(say1), id(say3))

say4 = say[:] # 슬라이싱을 이용한 문자열 복사

print (say1 == say4)
print(id(say1), id(say4))

jumin = '12345-1234567'
