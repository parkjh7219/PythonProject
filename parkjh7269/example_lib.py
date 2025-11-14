# 21
def compute_tax(salary,isMarried):
    """
    결혼 여부와 연봉을 입력하면 세율과 세금을 계산해줍니다 # 함수의 설명은 큰 따움표 3개

        prameters :
            isMarried : 결혼 여부
            salart : 연봉

        return:    # 타입을 알려준다
            list : (rate, tax)
                - int : 세율
                - float : 세금
    """

    tax,rate = 0

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

# 만일 두개의 값을 보낼 시 return rate, tax라고 적는다
# 본 코드에서는 rate, tax = compute_tax(salary,isMarried)

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
    # 함수 명은 동사 혹은 동사 + 명사로 작성  / 정보를 가져올 때 get(간단), read(자세한)
    # 변수는 명사로 작성

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

def generate_gugudan(dan): # 만들 때 generate 사용
    """
    단을 입력받아 구구단을 출력하는 함수

    :param dan:
    :return:
    """
    if 1 <= dan <= 9:
        result = f'=== {dan}단 ===\n'
        for i in range(1, 9 + 1):
            result += f'{dan} x {i} = {dan * i}\n'
    else:
        result = '잘못 입력하셨습니다!!'
    return result

# 32

def check_jumun(jumin):
    """
    입력한 주민번호가 올바른 것인지 확인하는 함수

    :param jumin:
    :return:
    """
    sum - 0
    code = [int(j) for j in jumin if j.isdigit()]  # 코드 한줄로 줄여보기

    wght = [(i % 8) + 2 for i in range(12)]

    for i in range(12):
        sum += code[i] * wght[i]

    checker = 11 - (sum % 11)
    isvalid = str(checker)[-1] == jumin

    return code, wght, sum, isvalid