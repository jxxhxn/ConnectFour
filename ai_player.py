#
# AI Player for use in Connect Four  
#

import random  
from playing import *

class AIPlayer(Player):
    """ intelligent” computer player – one that uses techniques from artificial intelligence (AI) to choose its next move
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        return 'Player' + ' ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' +str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score
        """
        max_score = max(scores)
        max_i_list = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_i_list += [i]
        if self.tiebreak == 'LEFT':
            return max_i_list[0]
        elif self.tiebreak == 'RIGHT':
            return max_i_list[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_i_list)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores for the columns in b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opponent_score = opponent.scores_for(b)
                if max(opponent_score) == 0:
                    scores[col] = 100
                elif max(opponent_score) == 100:
                    scores[col] = 0
                elif max(opponent_score) == 50:
                    scores[col] = 50
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
