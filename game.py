#!/usr/bin/env python

# game.py implements the class 'game' that sets up a game of connect 4

# initialize
import numpy as np
import pygame as pg
from random import random
from typing import Literal

import frontend
from moves import AI_move_random

# definr custom data types:
Color = Literal['yellow', 'red']
PlayerType = Literal['human', 'machine']

class Game:
    def __init__(self):
        self.board = np.zeros((6, 7))
        """ board is a 6 x 7 matrix that represents the board of the
            game connect 4. Each element of the matrix can have
            a value of 0, 1, 2:
            0: there is no piece at this position
            1: there is a piece of player 1 at this position
            2: there is a piece of player 2 at this position
        """
        self.gamewindow = frontend.Gamewindow()
        self.player1 = Player('yellow', 'human')
        self.player2 = Player('red', 'machine')
        # initially there is a 50% chance for each player to start:
        self.whose_turn =  'player1' if random() < 0.5 else 'player2'
        
        # show the start screen for a while:
        pg.time.wait(2000)

        self.gamewindow.draw_board(self.board)
        self.next_move()
        
    def next_move(self):
        valid_moves = np.where(self.board[0,:] == 0)[0]
        if valid_moves.size == 0:
            self.gamewindow.endscreen_draw()
            pg.time.wait(4000)
            exit()
        if self.whose_turn == 'player1':
            if self.player1.player_type == 'human':
                move = self.gamewindow.get_event(valid_moves)
                self.board = self.player1.human_move(self.board, move)
            else:
                self.board = self.player1.ai_move(self.board)
            self.gamewindow.draw_board(self.board)
            if self.check_win() == 'nowin':
                self.whose_turn = 'player2'
                self.next_move()
            else: 
                # TO DO: win screen
                print(self.check_win() + ' won!!')

        else:
            if self.player2.player_type == 'human':
                move = self.gamewindow.get_event(valid_moves)
                self.board = self.player2.human_move(self.board, move)
            else:
                self.board = self.player2.ai_move(self.board)
            self.gamewindow.draw_board(self.board)
            if self.check_win() == 'nowin':
                self.whose_turn = 'player1'
                self.next_move()
            else: 
                # TO DO: win screen
                print(self.check_win() + ' won!!')

    def check_win(self) -> str:
        """
        Checks whether we have 4 connected stones
        """
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
        
        for player_nr in [1, 2]:
            for row in self.board:
                vec = row == player_nr
                if pattern_xxxx(vec):
                    return "player" + str(player_nr)
            for col in np.rot90(self.board):
                vec = col == player_nr
                if pattern_xxxx(vec):
                    return "player" + str(player_nr)
            for i in range(-2, 4):
                diag = self.board.diagonal(i)
                vec = diag == player_nr
                if pattern_xxxx(vec):
                    return "player" + str(player_nr)
            for i in range(-3,3):
                antidiag = np.rot90(self.board).diagonal(i)
                vec = antidiag == player_nr
                if pattern_xxxx(vec):
                    return "player" + str(player_nr)
        return "nowin"
        


class Player:
    def __init__(self, color : Color, player_type: PlayerType):
        self.color = color
        self.player_type : PlayerType = player_type
        self.conversion_table = {'yellow': 1, 'red': 2}
        self.col_num = self.conversion_table[self.color]

    def ai_move(self, board: np.ndarray) -> np.ndarray:
        '''
        We store the algorithms for the AI moves in a 
        separate file. This function is thus just a call
        to the function in this file.
        '''
        return AI_move_random(board, self.col_num)

    def human_move(self, board: np.ndarray, move: int) -> np.ndarray:
        change_col = board[:, move]
        row = np.where(change_col == 0)[0][-1]
        new_board = board.copy()
        new_board[row, move] = self.col_num 
        return new_board    
