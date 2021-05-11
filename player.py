#
# A Connect-Four Player class 
#  

from game_board import Board

# write your class below.

class Player:
    """ a data type for a Player for a Connect Four
    """ 
    
    def __init__(self, checker):
        """ constructs a new Player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object """
        return 'Player' + ' ' + str(self.checker)
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of 
            the Player object’s opponent 
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ Get a next move for this player that is valid
        for the board b.
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            print('Try again!')
                
                
