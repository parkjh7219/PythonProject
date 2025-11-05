# 성적 처리 프로그램 V1
# 이름, 국어, 영어, 수학, 점수를 변수로 설정하고
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 단, 학점은 삼항연산자를 이용하여 계산한다
# 변수 = 참일 때 값 if 조건식 else 거짓일 때 값

#  내 풀이

name = '김민수'
korean = 99
english = 99
math = 98

총점 = korean + english + math
평균 = 총점 / 3

if 90 <= 평균 <= 100:
    result = 'A'
else:  # 90점 미만인 경우
    if 80 <= 평균 < 90:
        result = 'B'
    else:  # 80점 미만인 경우
        if 70 <= 평균 < 80:
            result = 'C'
        else:  # 70점 미만인 경우
            if 60 <= 평균 < 70:
                result = 'D'
            else:  # 60점 미만인 경우
                result = 'F'


# 선생님 풀이

# kor = 95
# eng = 88
# mat = 90
# tot = 0
# avg 0.0
# grd = '가'

# tot = kor + eng + mat
# avg = tot / 3

# grd = 'A' if (avg >= 90) else 'B'
# grd = 'B' if (avg >= 90) else 'C'
# grd = 'C' if (avg >= 90) else 'D'
# grd = 'D' if (avg >= 90) else 'F'
# grd = 'F' if (avg >= 59) else '' , 안됨 

# grd = ('A' if (avg >= 90) else
#       'B' if (avg >= 80) else
#       'C' if (avg >= 70) else
#       'D' if (avg >= 60) else 'F') , 됨

print('국어 : ', korean)
print('영어 : ', english)
print('수학 : ', math)
print('총점 : ', 총점)
print('평균 : ', 평균)
print('학점 : ', result)

print(f'평균 : {평균:.2f}') # 04에서 배운 소수점 2자리까지만 출력
