# ticTacToe.py

class player():
    def __init__(self, name):
        self.name = name
        # CR ethan: `player_name` is never used
        self.player_name = 'player_' + name
        # CR ethan: `player_square` is never used
        self.player_square = '[' + name + ']'
        self.placement = 0
        self.placements = set()
    
    # player chooses, can add AI/computer coding here
    def choose(self):
        print('\n'+'To quit game, enter QUIT')
        while True:
            self.placement = input(self.name + ', pick your placement! ')
            # CR ethan: this is a very soft consideration (I have coworkers who would disagree with me here), but: 
            # given that you're using a hardcoded `QUIT` string multiple times, I think it'd be cleaner and safer
            # to assign it to a variable once, and then use that variable rather than string literals.
            if self.placement == 'QUIT':
                break
            try:
                self.placement = int(self.placement)
                # CR ethan: you return a value here, but I don't think you catch/use it
                # anywhere. Also in other cases you aren't returning a value, so the 
                # signature of this function is a little confusing. I'd probably just do
                # an empty return
                return self.placement
            except:
                print('Placement must be an integer. Please try again.')
                # CR ethan: (nitpick) this continue is superfluous
                continue

class game():
    def __init__(self):
        # defining instances of two players
        self.player_x = player('x')
        self.player_o = player('o')
        self.current_player = self.player_x

        # all main placement sets/dictionaries 
        self.starting_placements = set(range(1, 10))
        # CR ethan: because this is during initialization, `played_placements` will never not be an empty set
        # I think it's cleaner and more intuitive to just initialize it as such explicitly
        # CR ethan: I think you're creating more data structures than you need here. what is `starting_placements` doing
        # for you? I think you could combine `starting_placements` with `available placements`, and combine `played_placements`
        # with `current_placements`, and it would make things cleaner.
        self.played_placements = self.player_x.placements.union(self.player_o.placements)
        self.available_placements = self.starting_placements.difference(self.played_placements)
        self.current_placements = {}

        #for start of game, fill current_placements dictionary with starting placement options
        for placement in self.starting_placements:
            # CR ethan: (nitpick) I think initializing to `placement` is a bit awkward, especially since you're later putting
            # a different type in there. I'd probably prefer `None`.
            # edit: got further in the code and it makes sense given the `displayBoard` function why you do it this way. I don't
            # love it still, but it makes sense! I wonder if there's some cleaner alternative?
            self.current_placements[placement] = placement

        # digits defining the bottom of the tic tac toe board, will be used to define up-down, left-right wins
        self.columns = {1, 2, 3}

        # CR ethan: (nitpick) I like that you're adding a comment to explain that the empty cases will be filled in, but 
        # I don't like that this is necessary. why not define `up_down` and `left_right` before defining `self.wins`, and 
        # then we can just include them directly?
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
    # CR ethan: I love seeing match statements in the wild :) I don't know much about the semantics/implementation in
    # python, I think they're less expressive/powerful than in some other languages but love that you're using new 
    # language features
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
            # CR ethan: this print statement is pretty long and kinda ugly! check out this page, in particular
            # the section on Formatted String Literals https://www.skillsugar.com/python-print-formatting
            print('[' + str(self.current_placements[v]) + ']' + '[' + str(self.current_placements[v+1]) + ']' + '[' + str(self.current_placements[v+2])+ ']')

    # update played and available placements based on most recent player placements
    def updateSets(self):
        # CR ethan: I think we could do something simpler here, e.g. pop a value out of one set and 
        # push it into another. this would be a good refactor along with reducing the number of sets as 
        # suggested above
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
                # CR ethan: again, we're returning a specific value inconsistently with other cases and
                # not actually using that value. 
                return self.current_player.placements

    def checkEndGame(self):
        # check if player wants to quit, then end game if so
        if self.current_player.placement == 'QUIT':
            print('\n' + 'Goodbye and thanks for playing!')
            self.end_game = True
            # CR ethan: probably should just return here so you don't end up doing unnecessary
            # victory checking

        # checking player's placements against win cases
        for sets in self.wins.values():
            # CR ethan: minor note, `set` is a keyword in python, which this is redefining. in cases
            # where shadowing a keyword is necessary, adding a `_` (e.g., `set_`) is a common idiom.
            # but, I think a good question to ask in such cases is, "can I give a more descriptive 
            # variable name?" in this case I do think there are better, more precise alternatives,
            # e.g. `possible_wins` or `win_categories` or something like that.
            
            # CR ethan: I do think this is a much cleaner victory check than the last one, well done :)
            for set in sets:
                if set.issubset(self.current_player.placements):
                    self.end_game = True
                    break
        # if winner exists, display winner and winning board
        if (self.end_game == True) and (self.current_player.placement != 'QUIT'):
            self.displayBoard()                
            print(self.current_player.name + ' wins!')

        # display tie, if tie
        # CR ethan: (nitpick) checking for `< 1` (rather than == 0) strikes me as a little odd.
        elif len(self.available_placements) < 1:
            self.displayBoard()
            self.end_game = True
            print('Tied game. You both win!')

# CR ethan: typically this code at the bottom here would go in a function called `main`,
# and then there's a weird idiom for making that code execute when called directly. see 
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
game = game()
while game.end_game == False:
    game.displayBoard()
    game.chooseValidateAdd()
    game.checkEndGame()
    game.playerSwitch()
