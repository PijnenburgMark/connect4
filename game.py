#!/usr/bin/env python

# game.py implements the class 'game' that sets up a game of connect 4

# initialize
import numpy as np
from pygame import time
from random import random

import frontend
from moves import AI_move_random

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
        self.gamewindow.opening_screen()
        time.wait(2000)
        # who starts?
        self.who_starts = 'player 1' if random() < 0.5 else 'player 2'
        if self.who_starts == 'player 1':
            self.human_move('player 1')
        else:
            self.computer_move()

    def human_move(self, player : str):
        # TO DO
        self.gamewindow.draw_board()
        self.computer_move()

    def computer_move(self, player : str):
        # TO DO: AI_move_random() aanpassen zodat ie het bord terug geeft
        self.board = AI_move_random(self.board, player)

        pass
    

speelbord.draw_board(positie)

# main loop: voorkomt dat het programma afsluit als het onderaande code is
# het prgramma stopt als running = False. Deze variabele wordt op False gezet 
# zodra de gebruiker op het kruisje rechtsboven in het window klikt.

# de klok voorkomt dat het programma een hele CPU opeet...
clock = pg.time.Clock()
player = 'human'
running = True
while running:
  eta = clock.tick(10) # 10 frames per second is enough
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

    elif event.type == pg.MOUSEBUTTONDOWN:
        posx, posy = pg.mouse.get_pos()
        x_div = speelbord.width / 7
        validmoves = np.where(positie[0,:]==0)[0]
        if int(posx/x_div) in validmoves:
            for player in('player1', 'player2'):
                # player1 = human, player2 = computer
                if player == 'player1':
                    move = int(posx / x_div)
                if player == 'player2':
                    move = AI_bestmove_1(positie)
                positie = utility.move2pos(positie, move, \
                        player)
                print(positie)
                speelbord.draw_board(positie)
                winner = checks.check_win(positie)
                if winner != "onbeslist": 
                    print("En de ", winner, " heeft gewonnen!")
                    pg.time.wait(4000)
                    running = False
                    break;
                if checks.check_finish(positie):
                    print("Game afgelopen. Gelijkspel!")
                    pg.time.wait(5000)
                    running = False
                    break;
                pg.time.wait(1000) # 1 sec nadenk tijd voor AI
        else:
            print('invalid move')
       

    
