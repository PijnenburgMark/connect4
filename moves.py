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
    new_board = position.copy()
    change_col = position[:, move]
    row = np.where(change_col==0)[0][-1]
    new_board[row, move] = 1 if player == 'player 1' else 2
    return new_board

def AI_move_minimax(position: np.ndarray, 
                    depth: int, 
                    player : str) -> np.ndarray:
    """
    AI follows the minimax algorithm. It goes several moves deep
    (determined by depth) and then evaluates the position based 
    on an evaluation function. It assumes that the player takes the
    move with the best evaluation, while the opponent will pick the move
    with the most unfavorable evaluation for the current player.
    position - The board at this moment
               0: there is no piece at this position
               1: there is a piece of player 1 at this position
               2: there is a piece of player 2 at this position
    depth    - The number of moves that will be played before evaluating
               the position with the evaluation function.
    player   - String with 2 possible values: 'player 1' and 'player 2'
               It indicates the active player.
    """
    move = minimax(position, depth, player)
    new_board = position.copy()
    change_col = position[:, move]
    row = np.where(change_col==0)[0][-1]
    new_board[row, move] = 1 if player == 'player 1' else 2
    return new_board
    
def minimax(position: np.ndarray, 
                    depth: int, 
                    player : str) -> float:
    '''
    Returns
    '''

    Parameters
    ----------
    position : np.ndarray
        DESCRIPTION.
    depth : int
        DESCRIPTION.
    player : str
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    '''
    valid_moves = np.where(position[0,:]==0)[0]
    # current board is in a terminal state
    if len(valid_moves) == 0:
        return 
    

    if current board state is a terminal state :
        return value of the board
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each move in board :
            value = minimax(board, depth+1, false)
            bestVal = max( bestVal, value) 
        return bestVal

    else :
        bestVal = +INFINITY 
        for each move in board :
            value = minimax(board, depth+1, true)
            bestVal = min( bestVal, value) 
        return bestVal 


if __name__ == '__main__':
    position = np.zeros((6, 7))
    position[5,0] = 1
    position[5,1] = 1
    position[4,0] = 2
    print(position)
    new_pos = AI_move_random(position, 'player 1')
    print(new_pos)
