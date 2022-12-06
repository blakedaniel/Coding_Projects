# ticTacToe.py

class player():
    def __init__(self, name):
        self.name = name
        self.player_name = 'player_' + name
        self.player_square = '[' + name + ']'
        self.placement = 0
        self.placements = set()
    
    # player chooses, can add AI/computer coding here
    def choose(self):
        print('\n'+'To quit game, enter QUIT')
        while True:
            self.placement = input(self.name + ', pick your placement! ')
            if self.placement == 'QUIT':
                break
            try:
                self.placement = int(self.placement)
                return self.placement
            except:
                print('Placement must be an integer. Please try again.')
                continue

class game():
    def __init__(self):
        # defining instances of two players
        self.player_x = player('x')
        self.player_o = player('o')
        self.current_player = self.player_x

        # all main placement sets/dictionaries 
        self.starting_placements = set(range(1, 10))
        self.played_placements = self.player_x.placements.union(self.player_o.placements)
        self.available_placements = self.starting_placements.difference(self.played_placements)
        self.current_placements = {}

        #for start of game, fill current_placements dictionary with starting placement options
        for placement in self.starting_placements:
            self.current_placements[placement] = placement

        # digits defining the bottom of the tic tac toe board, will be used to define up-down, left-right wins
        self.columns = {1, 2, 3}

        # defined winning cases, up_down and left_right will be defined by later below
        self.wins = {'up_down':[],
                'left_right':[],
                'tleft_bright':[{3, 5, 7}],
                'bleft_tright':[{1, 5, 9}]}
        
        # create up-down and left-to right win cases
        for column in self.columns:
            ud = {column, column + 3, column + 6}
            if column == 1:
                for row in ud:
                    lr = {row, row + 1, row + 2}
                    self.wins['left_right'].append(lr)
            self.wins['up_down'].append(ud)

        self.end_game = False
    
    # switch from one player to another player
    def playerSwitch(self):
        match self.current_player:
            case self.player_x:
                self.current_player = self.player_o
            case self.player_o:
                self.current_player = self.player_x

    # display board based on currently played placements
    def displayBoard(self):
        v3 = (7, 4, 1)
        for v in v3:
            print('[' + str(self.current_placements[v]) + ']' + '[' + str(self.current_placements[v+1]) + ']' + '[' + str(self.current_placements[v+2])+ ']')

    # update played and available placements based on most recent player placements
    def updateSets(self):
        self.played_placements = self.player_x.placements.union(self.player_o.placements)
        self.available_placements = self.starting_placements.difference(self.played_placements)

    # request player placement, check that placement is valid, if so add to player placements
    def chooseValidateAdd(self):
        self.updateSets()
        while True:
            self.current_player.choose()
            if self.current_player.placement == 'QUIT':
                break
            elif self.current_player.placement not in self.current_placements.values():
                print('Placement unavailable. Please try again.')
            else:
                self.current_player.placements.add(self.current_player.placement)
                self.current_placements[self.current_player.placement] = self.current_player.name
                self.updateSets()
                return self.current_player.placements

    def checkEndGame(self):
        # check if player wants to quit, then end game if so
        if self.current_player.placement == 'QUIT':
            print('\n' + 'Goodbye and thanks for playing!')
            self.end_game = True

        # checking player's placements against win cases
        for sets in self.wins.values():
            for set in sets:
                if set.issubset(self.current_player.placements):
                    self.end_game = True
                    break
        # if winner exists, display winner and winning board
        if (self.end_game == True) and (self.current_player.placement != 'QUIT'):
            self.displayBoard()                
            print(self.current_player.name + ' wins!')

        # display tie, if tie
        elif len(self.available_placements) < 1:
            self.displayBoard()
            self.end_game = True
            print('Tied game. You both win!')


game = game()
while game.end_game == False:
    game.displayBoard()
    game.chooseValidateAdd()
    game.checkEndGame()
    game.playerSwitch()