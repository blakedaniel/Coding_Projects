
# initialize
# import tkinter
import re

# ER: Global values like the following can sometimes be hard to track well, or
# really understand how they work. Would it be possible to create a class that
# stores all these values, and pass that around to functions as necessary?
# ER: could we create this with a loop, rather than hardcoding all the values?
board_values = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1),
                (2, 2)]
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

# ER: just a heads up, commented code like this is a little iffy 
# because it can easily be unclear what purpose it originally served,
# if it's still necessary, and if it's still correct. Not a big deal
# for a print statement, but worth keeping in mind especially as things get
# more complex :)

# print(dir(board_values))

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

# ER: need slight cleanup of this comment :) 
# used to determin if somoen one to end game
# ER: probably better to use a bool rather than an int for
# this value
win = 0

# functions
# create list of board values with coordinate pairings


def create_board_lst():
    for value in board_values:
        board_lst.append((value, square))
    return board_lst

# create visual board for playing

# ER: does this create a board, or print it out? `display_board() might
# be a better name for the latter.
def board():
    # print('Board List', board_lst)
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
    global player_input
    # print('Remaining board options:', board_values)
    while True:
        try:
            player_input = input('Player ' + player + ', where would you like to go? format: x, y ')
            # player_input = '(0, 1)'
            if player_input == 'quit':
                global win
                win = 1
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
    # print('Board Values: ', board_values)
    player_moves.append(placement)
    # print('Player Moves: ', player_moves)
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
            win = 1
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
            win = 1
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
        win = 1
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
        win = 1
        print('Player', player, 'wins by diagnal!!')
    except Exception:
        None


# the game is a draw


def draw(game_count):
    global win
    if len(board_values) < 1:
        win = 1
        print('Draw! No one wins')

# end game


'''
player_x_less_than_3 = [(0, 0), (0, 1)]
player_x_win_lr = [(1, 0), (1, 1), (1, 2)]
player_x_win_ud = [(2, 1), (1, 1), (0, 1)]
player_x_win_diag1 = [(0, 0), (1, 1), (2, 2)]
player_X_win_diag2 = [(2, 0), (1, 1), (0, 2)]
'''

# executing

test_moves = ['(0, 0)', '(1, 1)', '(0, 1)', '(1, 2)', '(0, 2)']
create_board_lst()

# ER: I like this structure! it's nice and clean. Might be good to
# put this all in a main function. 
while win == 0:
    board()
    # player_input = move
    player_def()
    player_move()
    player_placement(player_input)
    win_lr(player_moves)
    # print('win_lr: ', win)
    win_ud(player_moves)
    # print('win_ud: ', win)
    win_diag1(player_moves)
    # print('win_diag1: ', win)
    win_diag2(player_moves)
    # print('win_diag2: ', win)
    # print('player x moves:', player_x_moves)
    # print('player 0 moves:', player_o_moves)

board()
