'''
This script contains the various functions that
code the moves of the AI-player.

The most simple move-function is that the AI-player
performs a random move. This is encoded in the function 
AI_move_random

A more advanced AI-player will for example use a
minimax algorithm. This is coded in the function
AI_move_minimax  
'''
import numpy as np
from typing import Tuple
from util import new_position, value_board

def AI_move_random(position: np.ndarray, player : str) -> np.ndarray:
    """
    AI performs a random move.
    position - The board at this moment
               0: there is no piece at this position
               1: there is a piece of player 1 at this position
               2: there is a piece of player 2 at this position
    player   - String with 2 possible values: 'player 1' and 'player 2'
               It indicates the active player.
    """
    # welke kolommen zijn nog niet helemaal vol?
    valid_moves = np.where(position[0,:]==0)[0]
    randint = np.random.randint(0,len(valid_moves))
    move = valid_moves[randint]
    return new_position(position, player, move)

def AI_move_minimax(position: np.ndarray, 
                    depth: int, 
                    player : str) -> np.ndarray:
    """
    Selects the best move using the minimax function. 
    position - The board at this moment
               0: there is no piece at this position
               1: there is a piece of player 1 at this position
               2: there is a piece of player 2 at this position
    depth    - The number of moves that will be played before evaluating
               the position with the evaluation function.
    player   - String with 2 possible values: 'player 1' and 'player 2'
               It indicates the active player.
    """
    move = minimax(position, depth, True, player)[1]
    return new_position(position, player, move)
    
def minimax(position: np.ndarray, 
                    depth: int, 
                    is_maximizing_player : bool,
                    player: str) -> Tuple[float, int]:
    '''
    The algorithm goes several moves deep (determined by depth) 
    and then evaluates the position based 
    on an evaluation function. It assumes that the player takes the
    move with the best evaluation, while the opponent will pick the move
    with the most unfavorable evaluation for the current player.

    Parameters
    ----------
    position : np.ndarray
        The current position if the board
    depth : int
        The depth at which the minimax algorithm is working.
    is_maximizing_player : bool
        A boolean indicating whether the minimax algorithm should
        take the max or the minimum vlaue of the possible moves.
    player : str
        A string with two possible values 'player 1' of 'player 2'.
        Needed to tell the computer what the '1' and '2' mean of the board.

    Returns
    -------
    Tuple[float, int]
        Returns a tuple. The first element of the tuple represents the value 
        of the best move according to the minimax algorithm. The second element
        represents the latest move that let to this value.

    '''
    
    other_player = 'player 2' if player == 'player 1' else 'player 1'
    valid_moves = np.where(position[0,:]==0)[0]
    # current board is in a terminal state
    if (len(valid_moves) == 0) or (depth == 0):
        if is_maximizing_player:
            # we evaluate the board from the perspective of the maximizing
            # player
            return (value_board(position, player), 0)
            # the move does not matter, so we randomly return 0
        else:
            # we evaluate the board from the perspective of the maximizing
            # player
            return (value_board(position, other_player), 0)
            # the move does not matter, so we randomly return 0
            
        
       
    if is_maximizing_player:
        best_value = -10000.0
        best_move = valid_moves[0] # random initial value
        for move in valid_moves:
            new_board = new_position(position, player, move)
            value , mmmove = minimax(new_board, depth - 1, False, other_player)
            best_value = max( best_value, value)
            if value == best_value:
                best_move = mmmove
        return (best_value, best_move)

    else :
        best_value = +10000.0
        best_move = valid_moves[0] # random initial value
        for move in valid_moves:
            new_board = new_position(position, player, move)
            value , mmmove = minimax(new_board, depth - 1, True, other_player)
            best_value = min( best_value, value) 
            if value == best_value:
                best_move = mmmove
        return (best_value, best_move) 


if __name__ == '__main__':
    position = np.zeros((6, 7))
    position[5,0] = 1
    position[5,1] = 1
    position[4,0] = 2
    print(position)
    new_pos = AI_move_random(position, 'player 1')
    print(new_pos)
