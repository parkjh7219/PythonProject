# 성적 처리프로그램 V1
# 이름, 국어, 영어, 수학 점수를 변수로 설정하고
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 단, 학점은 삼항연산자를 이용해서 계산한다.
# 변수 = 참일때값 if 조건식 else 거짓일때값
# 조건 : 국어-99, 영어-99, 수학-98


# 입력
# 이름, 국어, 영어, 수학 점수를 변수로 설정
name = '김민수'
kor = 99
eng = 99
mat = 98
tot = 0
avg = 0.0
grd = '가'


# 성적처리
# 총점, 평균, 학점 처리
tot = kor + eng + mat
avg = tot / 3
# grd = 'A' if (avg >= 90) else 'B'
# grd = 'C' if (avg >= 70 and avg < 80) else 'D'
# grd = 'F' if (avg <= 59) else ''
grd = ('A' if (avg >= 90) else
      'B' if (avg >= 80) else
      'C' if (avg >= 70) else
      'D' if (avg >= 60) else 'F')

# 결과출력
# 이름, 국어, 영어, 수학, 총점, 평균, 학점 출력
print('===== 성적 결과 ===== ')
print('이름 : ', name)
print('국어 : ', kor)
print('영어 : ', eng)
print('수학 : ', mat)
print('총점 : ', tot)
print(f'평균 : {avg:.2f}')
print('학점 : ', grd)
