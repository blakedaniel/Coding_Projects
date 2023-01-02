import random


class Player():
    options = ('Rock', 'Paper', 'Scissors')

    def __init__(self, p_type):
        self.cur_move = ''
        self.wins = 0
        self.p_type = p_type

    def choose(self):
        if self.p_type == 'person':
            while True:
                self.cur_move = input('{0[0]}, {0[1]}, or {0[2]}: '.format(Player.options))
                if self.cur_move not in self.options:
                    print('Please choose from {0[0]}, {0[1]}, or {0[2]}!'.format(Player.options))
                else:
                    return
        if self.p_type == 'computer':
            i = random.randrange(start=0, stop=3)
            self.cur_move = self.options[i]
            return


class GameRound():
    def __init__(self, p, c):
        p.choose()
        c.choose()

    def checkRoundWinPoints(self, p, c):
        print('Player: {} vs. Computer: {}'.format(p.cur_move, c.cur_move))
        p_win_cases = (('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock'))
        if p.cur_move == c.cur_move:
            print('Round is a draw')
        elif (p.cur_move, c.cur_move) in p_win_cases:
            print('Player wins the round')
            p.wins += 1
        else:
            print('Computer wins the round.')
            c.wins += 1


class Game():
    def __init__(self):
        self.person = Player('person')
        self.comp = Player('computer')
        self.end_game = False

    def startRound(self):
        game_round = GameRound(self.person, self.comp)
        game_round.checkRoundWinPoints(self.person, self.comp)

    def checkWinnerEnd(self):
        if self.person.wins == 2:
            self.end_game = True
            print('Player wins the game!')
        elif self.comp.wins == 2:
            print('Computer wins the game!')
            self.end_game = True


game = Game()
while game.end_game == False:
    game.startRound()
    game.checkWinnerEnd()
