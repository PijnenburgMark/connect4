'''
This script contains the various functions that
code the moves of the AI-player.

The most simple move-function is that the AI-player
performs a random move. This is encoded in 
AI_move_random

A more advanced AI-player will for example use a
mini-,ax algorithm. This is coded in the function
AI_move_minimax  
'''
import numpy as np

def AI_move_random(position: np.ndarray, player : str) -> np.ndarray:
    """
    De AI doet een random zet. 
    """
    # welke kolommen zijn nog niet helemaal vol?
    validmoves = np.where(position[0,:]==0)[0]
    randint = np.random.randint(0,len(validmoves))
    move = validmoves[randint]
    new_board = position.copy()
    change_col = position[:, move]
    row = np.where(change_col==0)[0][-1]
    new_board[row, move] = 1 if player == 'player 1' else 2
    return new_board

def AI_move_minimax(position: np.ndarray, player : str) -> np.ndarray:
    pass
    
if __name__ == '__main__':
    position = np.zeros((6, 7))
    position[5,0] = 1
    position[5,1] = 1
    position[4,0] = 2
    print(position)
    new_pos = AI_move_random(position, 'player 1')
    print(new_pos)
