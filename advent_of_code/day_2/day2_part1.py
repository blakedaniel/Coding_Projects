
file = 'GitHub/Coding_Projects/advent_of_code/day_2/input_part1.txt'
game_rounds = open(file)


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
    players = (0, 1)
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

print(player_1.shape_points + player_1.win_points, player_2.shape_points + player_2.win_points)
