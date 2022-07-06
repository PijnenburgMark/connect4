
import numpy as np

def AI_move_random(position: np.ndarray, player : str) -> np.ndarray:
    """
    De AI doet een random zet. 
    """
    # welke kolommen zijn nog niet helemaal vol?
    validmoves = np.where(position[0,:]==0)[0]
    randint = np.random.randint(0,len(validmoves))
    move_ai = validmoves[randint]
    new_board = position.copy()
    change_col = position[:, move_ai]
    row = np.where(change_col==0)[0][-1]
    new_board[row, move_ai] = 1 if player == 'player 1' else 2
    return new_board

if __name__ == '__main__':
    position = np.zeros((6, 7))
    position[5,0] = 1
    position[5,1] = 1
    position[4,0] = 2
    print(position)
    new_pos = AI_move_random(position, 'player 1')
    print(new_pos)
