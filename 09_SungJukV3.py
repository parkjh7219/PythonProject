# 성적 처리프로그램 V3
# 3명의 학생에 대해
# 이름, 국어, 영어, 수학 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력

# 입력
name1 = input('1) 이름을 입력하세요 : ')
kor1 = int(input('1) 국어 점수를 입력하세요 : '))
eng1 = int(input('1) 영어 점수를 입력하세요 : '))
mat1 = int(input('1) 수학 점수를 입력하세요 : '))
tot1 = 0
avg1 = 0.0
grd1 = '가'

name2 = input('2) 이름을 입력하세요 : ')
kor2 = int(input('2) 국어 점수를 입력하세요 : '))
eng2 = int(input('2) 영어 점수를 입력하세요 : '))
mat2 = int(input('2) 수학 점수를 입력하세요 : '))
tot2 = 0
avg2 = 0.0
grd2 = '가'

name3 = input('3) 이름을 입력하세요 : ')
kor3 = int(input('3) 국어 점수를 입력하세요 : '))
eng3 = int(input('3) 영어 점수를 입력하세요 : '))
mat3 = int(input('3) 수학 점수를 입력하세요 : '))
tot3 = 0
avg3 = 0.0
grd3 = '가'

# 성적처리
tot1 = kor1 + eng1 + mat1
avg1 = tot1 / 3
grd1 = ('A' if (avg1 >= 90) else
      'B' if (avg1 >= 80) else
      'C' if (avg1 >= 70) else
      'D' if (avg1 >= 60) else 'F')

tot2 = kor2 + eng2 + mat2
avg2 = tot2 / 3
grd2 = ('A' if (avg2 >= 90) else
      'B' if (avg2 >= 80) else
      'C' if (avg2 >= 70) else
      'D' if (avg2 >= 60) else 'F')

tot3 = kor3 + eng3 + mat3
avg3 = tot3 / 3
grd3 = ('A' if (avg3 >= 90) else
      'B' if (avg3 >= 80) else
      'C' if (avg3 >= 70) else
      'D' if (avg3 >= 60) else 'F')

# 결과출력
pfmt = f'''
이름  국어  영어  수학  총점  평균  학점
==================================
{name1}  {kor1}  {eng1}  {mat1}  {tot1} {avg1:.2f}   {grd1}
{name2}  {kor2}  {eng2}  {mat2}  {tot2} {avg2:.2f}   {grd2}
{name3}  {kor3}  {eng3}  {mat3}  {tot3} {avg3:.2f}   {grd3}
'''

print(pfmt)