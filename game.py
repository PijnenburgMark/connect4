#!/usr/bin/env python

# game.py implements the class 'game' that sets up a game of connect 4

# initialize
import numpy as np
import pygame as pg
from random import random
from typing import Literal

import frontend
from moves import AI_move_random, AI_move_minimax

from util import win_pattern, new_position

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
        self.whose_turn =  'player 1' if random() < 0.5 else 'player 2'
        
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
        if self.whose_turn == 'player 1':
            if self.player1.player_type == 'human':
                move = self.gamewindow.get_event(valid_moves)
                self.board = new_position(self.board, 'player 1', move)
            else:
                self.board = AI_move_minimax(self.board, 3, 'player 1') 
            self.gamewindow.draw_board(self.board)
            if win_pattern(self.board) == 'nowin':
                self.whose_turn = 'player 2'
                self.next_move()
            else: 
                # TO DO: win screen
                print(win_pattern(self.board) + ' won!!')

        else:
            if self.player2.player_type == 'human':
                move = self.gamewindow.get_event(valid_moves)
                self.board = new_position(self.board, 'player 2', move)
            else:
                self.board = AI_move_minimax(self.board, 3, 'player 2')
            self.gamewindow.draw_board(self.board)
            if win_pattern(self.board) == 'nowin':
                self.whose_turn = 'player 1'
                self.next_move()
            else: 
                # TO DO: win screen
                print(win_pattern(self.board) + ' won!!')       


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
        return 

    