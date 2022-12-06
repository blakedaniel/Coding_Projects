# day2_part1.py
# A|X = rock -> 1, B|Y = paper -> 2, C|Z = scissors -> 3
# lose = 0, draw = 3, win = 6
# [1, 1] --> 3, 3 --> 1 - 1 = 0
# [1, 3] --> 6, 0 --> 1 - 3 = -2
# [3, 1] --> 0, 6 --> 3 - 1 = 2
# [1, 2] --> 0, 6 --> 1 - 2 = -1

file = 'GitHub/Coding_Projects/advent_of_code/day_2/input_part1.txt'
game_rounds = open(file)
# game_rounds = (['A', 'Z'], ['B', 'Z'])  # output should be 6, 6


class player():
    def __init__(self):
        self.win_points = 0
        self.shape_points = 0
        self.cur_move = 0


player_1 = player()
player_2 = player()
player_2_possible_wins = ([1, 2], [2, 3], [3, 1])

for game_round in game_rounds:
    game_round = game_round.split()
    players = (0, 1)  # 0 is for the elf, 1 is for blake
    for player in players:
        if game_round[player] == 'A' or game_round[player] == 'X':
            game_round[player] = 1
        if game_round[player] == 'B' or game_round[player] == 'Y':
            game_round[player] = 2
        if game_round[player] == 'C' or game_round[player] == 'Z':
            game_round[player] = 3

    player_1.shape_points += game_round[0]
    player_2.shape_points += game_round[1]

    if game_round in player_2_possible_wins:
        player_1.win_points += 0
        player_2.win_points += 6
    elif game_round[0] == game_round[1]:
        player_1.win_points += 3
        player_2.win_points += 3
    else:
        player_1.win_points += 6
        player_2.win_points += 0

print(player_1.shape_points + player_1.win_points)
print(player_2.shape_points + player_2.win_points)
