# dit script bevat alle visuele elementen voor het spel 
# "4 op een rij". Dus met name het speelbord.

import pygame as pg
import numpy as np

class Gamewindow:
    def __init__(self):
        self.width = 700
        self.height = int((self.width / 7) * 6)
        self.black = (0, 0, 0)
        self.blue = (10, 10, 235)
        self.yellow = (255, 255, 0)
        self.pink = (242, 10, 242)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.screen = pg.display.set_mode((self.width, self.height))
        
        self.font = pg.font.SysFont("monospace", int(min(self.width, self.height) / 10))

        pg.display.set_caption('Vier op een rij!')
        openingsscherm = pg.image.load("startscreen.png")
        openingsscherm = pg.transform.scale(openingsscherm, \
                                            (self.width, self.height))
        self.screen.blit(openingsscherm, (0,0))
        pg.display.update()

    def draw_board(self, board):
        
        ## teken het lege bord
        self.screen.fill(self.blue)
        step = self.width / 7
        smalldist = step / 20
        # loop over de rijen    
        for i in range(6):
            y = i * step + step / 2
            # loop over de kolommen
            for j in range(7):
                x = j * step + step / 2
                pg.draw.circle(self.screen, self.white, (x, y), step / 2 - smalldist)

        ## vul de schijven
        # loop over de rijen
        for i in range(6):
            # loop over de kolommen
            for j in range(7):
                if board[i,j] == 1:
                    y = i * step + step / 2
                    x = j * step + step / 2
                    pg.draw.circle(self.screen, self.red, (x,y), \
                            step / 2 - smalldist)
                if board[i,j] == 2:
                    y = i * step + step / 2
                    x = j * step + step / 2
                    pg.draw.circle(self.screen, self.yellow, (x,y), \
                            step / 2 - smalldist)

        pg.display.update()

    def get_event(self, valid_moves: np.ndarray) -> int:
        # clear event cache first:
        pg.event.clear() 
        while True:
            event = pg.event.wait()
            '''
            Since the human move typically takes much longer
            than the AI move, we check only during the human move
            on the clicking of the quit-button.
            '''
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                posx, posy = pg.mouse.get_pos()
                x_div = self.width / 7
                move = int(posx / x_div)
                if move in valid_moves:
                    return  move
                else:
                    print('Invalid Move. Try again.')

    def endscreen_draw(self):
        self.screen.fill(self.blue)
        label = self.font.render("DRAW", 1, self.pink)
        self.screen.blit(label, (int(self.width / 2), \
                int(self.height / 2)))
        pg.display.update()

