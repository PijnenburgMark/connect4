# -*- coding: utf-8 -*-
"""
Created on Sun May 21 13:09:30 2023

@author: Mark Pijnenburg

Code that implements some auxiliary functions
that are used at various parts in the code.
"""
import numpy as np

def new_position(old_position: np.ndarray, player: str, move: int) \
-> np.ndarray:
    '''
    Parameters
    ----------
    old_position : np.ndarray
        Old position of the board
    player: str
        String indicating which player is putting a stone.
        Two possible values: 'player 1' and 'player 2'
    move : int
        The column in which a stone is placed

    Returns
    -------
    New postion of the board
    '''
    new_board = old_position.copy()
    change_col = old_position[:, move]
    row = np.where(change_col==0)[0][-1]
    new_board[row, move] = 1 if player == 'player 1' else 2
    return new_board


def pattern_xxxx(vec: np.ndarray) -> bool:
    """
    vec: a boolean vector with a 'True' at the
    position of a stone.
    """
    if len(vec) > 3:
        for i in range(len(vec) - 3):
            test = vec[i:i+4]
            if sum(test) == 4:
                return True
    return False

def pattern_xxx(vec: np.ndarray) -> bool:
    """
    vec: a boolean vector with a 'True' at the
    position of a stone.
    """
    if len(vec) > 2:
        for i in range(len(vec) - 2):
            test = vec[i:i+3]
            if sum(test) == 3:
                return True
    return False

def win_pattern(position: np.ndarray) -> str:
    '''

    Parameters
    ----------
    position : np.ndarray
        The Board.

    Returns
    -------
    str
        Three return possibilities: "player 1", "player 2" or "no win" 

    '''
            
    for player_nr in [1, 2]:
        for row in position:
            vec = row == player_nr
            if pattern_xxxx(vec):
                return "player" + str(player_nr)
        for col in np.rot90(position):
            vec = col == player_nr
            if pattern_xxxx(vec):
                return "player" + str(player_nr)
        for i in range(-2, 4):
            diag = position.diagonal(i)
            vec = diag == player_nr
            if pattern_xxxx(vec):
                return "player" + str(player_nr)
        for i in range(-3,3):
            antidiag = np.rot90(position).diagonal(i)
            vec = antidiag == player_nr
            if pattern_xxxx(vec):
                return "player" + str(player_nr)
    return "nowin"


def value_board(position: np.ndarray, player : str) -> float:
    '''
    Function that return the value of the board 
    from the viewpoint of player 'player'.
    A large value means a favourable position.
    We stop considering moves as soon as a player has
    wun. Therefore we expect that at max four
    connected stones of any color can occur at the board.
    Parameters
    ----------
    position : np.ndarray
        the board.
    player : str
        String with 2 possible values: 'player 1' and 'player 2'
        It indicates the active player.

    Returns
    -------
    float
    '''
    # check for a win or a loss:
    result_win = win_pattern(position)
    if result_win == player:
        return 100
    elif result_win not in(player, "no win"):
        return -100
    else: #check on 3 patterns
        return 0
