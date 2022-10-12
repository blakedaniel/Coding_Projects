# feedback from Ethan
# [] Delete commented code and keep in mind that printing variables is prefered
# [] create class for global values to be passed around and used in functions
# [] create loop to create board coordinates
# [] learn about sets vs. lists
# [] how would I approach the winning functions outside of try-except
# [] combine winning functions into one main function


# initialize
import re

n = tuple(range(0, 3))
board_values = set([(x, y) for x in n for y in n])

player_x_moves = []
player_o_moves = []
player_moves = []

# strings for making the board
square = '[ ]'
x_square = '[X]'
o_square = '[O]'
player_square = ''

# list of possible board values, paired with apropriate board string
board_lst = []

# the move a play chooses, one for each player
player_x_input = 'x input'
player_o_input = 'o input'

# the move of the player in current turn
player_input = 'player input'


# coordinates for moves
x = -1
y = -1

# player turn counter, when odd it's X when even it's O
player_turn = 1
game_count = 1

# used to determin if someone won to end game
win = False

# functions
# create list of board values with coordinate pairings


def create_board_lst():
    for value in board_values:
        board_lst.append((value, square))
    return board_lst

# print visual board for playing


def display_board():
    n3 = (3, 6, 9)
    m = 0
    print('   0', '  1', '  2')
    for n in n3:
        print(m, board_lst[n-3][1], board_lst[n-2][1], board_lst[n-1][1])
        m += 1

# it is player x's turn when 0, player O's turn when 1


def player_def():
    global player_moves
    global player_input
    global player_turn
    global player
    global player_square
    global x_square
    global o_square
    if player_turn == 0:
        player_moves = player_o_moves
        player_input is player_o_input
        player = 'O'
        player_turn += 1
        player_square = o_square
    else:
        player_moves = player_x_moves
        player_input is player_x_input
        player = 'X'
        player_turn -= 1
        player_square = x_square
    # ER: so the way return works in Python is that it will
    # immediately exit the function and return the named value.
    # so I think this will return `player_moves` alone and then
    # the following three lines will never execute.
    return player_moves
    return player_input
    return player_turn
    return player

# player input


def player_move():
    global win
    while True:
        try:
            player_input = input('Player ' + player + ', where would you like to go? format: x, y ')
            if player_input == 'quit':
                win = True
                player_input == board_values[0]
            else:
                player_input = re.findall('[0-4]', player_input)
                player_input = (int(player_input[0]), int(player_input[1]))
                board_values.index(player_input)
            break
        except Exception:
            print(player_input, 'is not a valid choice, please try again')
            continue
    # ER: since we actually return the player_input here, it probably doesn't need to be global
    # at all.
    return player_input

# remove player input from possible board values and add to player list


def player_placement(player_input):
    placement = player_input
    # ER: minor point, but: if board_values were a set rather than a list, this remove call would
    # be more performant. Not a big deal in tic tac toe, but for arbitrarily sized boards it could
    # matter :)
    board_values.remove(placement)
    player_moves.append(placement)
    replace = board_lst.index((player_input, square))
    board_lst[replace] = (player_input, player_square)
    return player_moves


# check if player won from left to right


def win_lr(player_moves):
    global win
    for move in player_moves:
        x = move[0]
        y = move[1]
        # ER: this definitely works but I think it's code that we expect to hit the error case
        # a majority of times? might be worth thinking about how we can only check valid cases.
        try:
            player_moves.index((x, y + 1))
            player_moves.index((x, y + 2))
            win = True
            print('Player', player, 'wins left to right!!')
        except Exception:
            None


# check if player won from up to down

# ER: this code is really similar to the `win_lr` function above. Could we find a way to pull
# out the duplicate code and reuse it?
def win_ud(player_moves):
    global win
    for move in player_moves:
        x = move[0]
        y = move[1]
        try:
            player_moves.index((x + 1, y))
            player_moves.index((x + 2, y))
            win = True
            print('Player', player, 'wins up and down!!')
        except Exception:
            None

# player wins from diagnal bottom left to top right

# ER: Same as above, there's some duplication here between the diag victory
# checks. Would be cool to limit it to a single function
def win_diag1(player_moves):
    global win
    win_diag = [(0, 0), (1, 1), (2, 2)]
    try:
        player_moves.index(win_diag[0])
        player_moves.index(win_diag[1])
        player_moves.index(win_diag[2])
        win = True
        print('Player', player, 'wins by diagnal!!')
    except Exception:
        None

# player wins from diagnal top left to bottom right


def win_diag2(player_moves):
    global win
    win_diag = [(2, 0), (1, 1), (0, 2)]
    try:
        player_moves.index(win_diag[0])
        player_moves.index(win_diag[1])
        player_moves.index(win_diag[2])
        win = True
        print('Player', player, 'wins by diagnal!!')
    except Exception:
        None


# the game is a draw


def draw():
    global win
    if len(board_values) < 1:
        win = True
        print('Draw! Everyone wins!')


# executing

create_board_lst()

while win == False:
    display_board()
    player_def()
    player_move()
    player_placement(player_input)
    win_lr(player_moves)
    win_ud(player_moves)
    win_diag1(player_moves)
    win_diag2(player_moves)
    draw()

display_board()
