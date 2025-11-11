# 성적 처리프로그램 V2
# 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 단, 학점은 삼항연산자를 이용해서 계산한다.
# 조건 : 국어-99, 영어-99, 수학-98

# 입력
name = input('이름을 입력하세요 : ')
kor = int(input('국어 점수를 입력하세요 : '))
eng = int(input('영어 점수를 입력하세요 : '))
mat = int(input('수학 점수를 입력하세요 : '))
tot = 0
avg = 0.0
grd = '가'

# 성적처리
tot = kor + eng + mat
avg = tot / 3
grd = ('A' if (avg >= 90) else
      'B' if (avg >= 80) else
      'C' if (avg >= 70) else
      'D' if (avg >= 60) else 'F')

# 결과출력
pfmt = f'''
===== 성적 결과 =====
이름 : {name}
국어 : {kor}
영어 : {eng}
수학 : {mat}
총점 : {tot}
평균 : {avg:.2f}
학점 : {grd}
'''

print(pfmt)
