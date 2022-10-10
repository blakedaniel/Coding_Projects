square = '[ ]'
x_square = '[X]'
o_square = '[O]'
player_square = ''
board_values = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1),
                (2, 2)]
board_lst = []


def create_board_lst():
    for value in board_values:
        board_lst.append((value, square))


create_board_lst()


def board():
    # print('Board List', board_lst)
    n3 = (3, 6, 9)
    m = 2
    print('   0', '  1', '  2')
    for n in n3:
        print(m, board_lst[n-3][1], board_lst[n-2][1], board_lst[n-1][1])
        m -= 1


board()

player_input = (0, 0)
player_square = o_square
replace = board_lst.index((player_input, square))
board_lst[replace] = (player_input, player_square)
print('after o placement', board_lst)
board()

player_input = (2, 2)
player_square = x_square
replace = board_lst.index((player_input, square))
board_lst[replace] = (player_input, player_square)
print('after x placement', board_lst)
board()
