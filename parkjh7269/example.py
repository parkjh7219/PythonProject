# 21
def compute_tax(salary,isMarried):
    tax = 0
    rate = 0

    if isMarried == 'n':
        if salary < 3000:
            rate = 10
        else:
            rate = 25
    elif isMarried == 'y':
        if salary < 6000:
            rate = 10
        else:
            rate = 25
    else:
        print('성별 오류!!')

    tax = salary * (rate / 100)

    result = f'''
    적용세율 : {rate}%
    납부해야 할 세금은 {tax}만원입니다
    '''

    return result

# 23 a
def lotto999(mykey,lotto):

    match = 0
    prize = 0
    message = '일치하는 숫자가 없습니다'

    for i in range(3):
        for j in range(3):
            if lotto[i] == mykey[j]:
                match += 1
    match match:
        case 3:
            prize = 1000000
            message = '1등상입니다'
        case 2:
            prize = 10000
            message = '2등상입니다'
        case 1:
            prize = 1000
            message = '3등상입니다'
    print(message)

    result = f'''
당첨번호 : {lotto}
당신의 복권번호 : {mykey}
일치한 숫자 갯수 : {match}
당첨 금액 : {prize}원
       '''
    print(result)

    return match

# 23 b
def lotto999_repeat(mykey,lotto):
    match = 0

    for i in range(3):
        for j in range(3):
            if lotto[i] == mykey[j]:
                match += 1
    return match

def lotto999_case(match):

    prize = 0
    message = '일치하는 숫자가 없습니다'

    match match:
        case 3:
            prize = 1000000
            message = '1등상입니다'
        case 2:
            prize = 10000
            message = '2등상입니다'
        case 1:
            prize = 1000
            message = '3등상입니다'
    print(message)
    return prize

def lotto999_output(lotto,mykey,match,prize):

    result = f'''
    당첨번호 : {lotto}
    당신의 복권번호 : {mykey}
    일치한 숫자 갯수 : {match}
    당첨 금액 : {prize}원
    '''
    return result

# 24

def gugudan(dan):
    if 1 <= dan <= 9:
        result = f'=== {dan}단 ===\n'
        for i in range(1, 9 + 1):
            result += f'{dan} x {i} = {dan * i}\n'
    else:
        result = '잘못 입력하셨습니다!!'
    return result

# 32
