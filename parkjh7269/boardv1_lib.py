# boardv1a

menu = f"""
==== 게시판 프로그램 ====
1. 새 글쓰기
2. 글 목록
3. 본문 보기
4. 글 수정
5. 글 삭제
0. 종료 """
print(menu)


def input_boards() :
    title = input('글 제목 : ')
    userid = input('작성자 : ')
    regdate = input('본문 : ')

    return title, userid, regdate

def get_views(views) :

    views += 1
    return views

def get_contents() :

    from datetime import date

    contents = date.today()

    return contents

def get_list (title, userid, regdate, views, contents) :
    broad = [title, userid, regdate, views, contents]

    return broad

def readone_boards(broad) :

    result = ''
    for br in broad:
        result += f'{br[0]} | {br[1]} | {br[2]} | {br[3]} | {br[4]} \n'

    return result


# def readall_boards(choice) :


# def modify_boards(choice) :
#     pass
#
# def remove_boards(choice) :
#     pass

# boardv1b

counts = 1

menus = f'''
--------------------------
    게시판 프로그램 V1
--------------------------
    1. 새 글 쓰기
    2. 게시글 목록
    3. 게시글 본문 보기
    4. 게시글 수정
    5. 게시글 삭제
    0. 프로그램 종료 
--------------------------
작업을 선택하세요 : '''


def input_board():
    global counts # 전역변수 함수 내 수정 허옹
    
    title = input('글 제목 : ')
    userid = input('작성자 : ')
    contents = input('본문 : ')

    board = [counts, title, userid, contents, 0, '2025-11-14']
    counts += 1

    return board

def write_board(boards) :

    board = input_board()
    boards.append(board)

    print('🥱🥱🥱글이 등록되었습니다.🥱🥱🥱')

header1 = '''
        ===== 게시글 목록 =====
번호 |   제목   | 작성자 |  작성일  | 조회
-----------------------------------
'''

def list_board(boards):
    result = ''
    for bd in boards:
        result += f'{bd[0]} {bd[1]} {bd[2]} {bd[5][:10]} {bd[4]}\n'

    print(f'{header1}{result}')