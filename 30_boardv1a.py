from parkjh7269.boardv1_lib import input_boards, get_views, get_contents
from parkjh7269.boardv1_lib import get_list
from parkjh7269.boardv1_lib import readone_boards  #, readall_boards
# from parkjh7269.boardv1_lib import modify_boards, remove_boards

from parkjh7269.boardv1_lib import menu
print(menu)

broad = []
views = 0

while True:
    choice = int(input('메뉴 선택 : '))
    match choice:
        case 1:
            title, userid, regdate = input_boards()
            views = get_views(views)
            contents = get_contents()
            broad += get_list (title, userid, regdate, views, contents)
        case 2:
            result = readone_boards(broad)
            print(result)
        # case 3:
        #     readall_boards(choice)
        # case 4:
        #     modify_boards(choice)
        # case 5:
        #     remove_boards(choice)
        case 0:
            break