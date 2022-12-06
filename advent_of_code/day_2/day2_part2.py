# day2_part2.py

# A = rock -> 1, B = paper -> 2, C = scissors -> 3
# X -> lose, Y -> tie, Z -> win
# lose = 0, draw = 3, win = 6


file = 'GitHub/Coding_Projects/advent_of_code/day_2/input_part1.txt'
game_rounds = open(file)  # output: win_points = 12; shape_points = 12; total_points = 24


player_2_win_cases = (['A', 'B'], ['B', 'C'], ['C', 'A'])
player_2_moves = []

x_count = 0
y_count = 0
z_count = 0
shape_points = 0

for game_round in game_rounds:
    game_round = game_round.rstrip().split()
    if game_round[1] == 'X':
        x_count += 1
        for win_case in player_2_win_cases:
            win_case.reverse()
            if game_round[0] == win_case[0]:
                player_2_moves.append(win_case[1])
            win_case.reverse()
    elif game_round[1] == 'Y':
        y_count += 1
        player_2_moves.append(game_round[0])
    else:
        z_count += 1
        for win_case in player_2_win_cases:
            if game_round[0] == win_case[0]:
                player_2_moves.append(win_case[1])        

for move in player_2_moves:
    if move == 'A':
        shape_points += 1
    elif move == 'B':
        shape_points += 2
    elif move == 'C':
        shape_points += 3

total_points = (x_count * 0) + (y_count * 3) + (z_count * 6) + shape_points
print(total_points)
