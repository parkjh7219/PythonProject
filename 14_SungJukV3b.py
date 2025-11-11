result = ''
tot = 0
avg = 0.0
grd = '가'

for i in range(1,3+1):

    name = input(f'{1}) 이름을 입력하세요 : ')
    kor = int(input(f'{1}) 국어 점수를 입력하세요 : '))
    eng = int(input(f'{1}) 영어 점수를 입력하세요 : '))
    mat = int(input(f'{1}) 수학 점수를 입력하세요 : '))

    tot= kor + eng + mat
    avg = tot / 3
    grd = ('A' if (avg >= 90) else
          'B' if (avg >= 80) else
          'C' if (avg >= 70) else
          'D' if (avg >= 60) else 'F')

    result += f'{name:5s}  {kor:4d}  {eng:4d}  {mat:4d}  {tot:4d} {avg:.2f}   {grd:3s}\n'


print(f'''
이름  국어  영어  수학  총점  평균  학점
==================================
{result}
''')
