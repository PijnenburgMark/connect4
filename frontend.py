# dit script bevat alle visuele elementen voor het spel 
# "4 op een rij". Dus met name het speelbord.

import pygame as pg

class Gamewindow():
    def __init__(self):
        self.width = 700
        self.height = int((self.width / 7) * 6)
        self.black = (255, 255, 255)
        self.blue = (10, 10, 235)
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.screen = pg.display.set_mode((self.width, self.height))
        
        pg.display.set_caption('Vier op een rij!')
        self.screen.fill(self.black)
        pg.display.update()

    def opening_screen(self):
        openingsscherm = pg.image.load("vieropeenrij_image.png")
        openingsscherm = pg.transform.scale(openingsscherm, \
                                            (self.width, self.height))
        self.screen.blit(openingsscherm, (0,0))
        pg.display.update()
        pg.time.wait(2000)

    def draw_board(self, position):
        
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
                pg.draw.circle(self.screen, self.black, (x, y), step / 2 - smalldist)

        ## vul de schijven
        # loop over de rijen
        for i in range(6):
            # loop over de kolommen
            for j in range(7):
                if position[i,j] == 1:
                    y = i * step + step / 2
                    x = j * step + step / 2
                    pg.draw.circle(self.screen, self.red, (x,y), \
                            step / 2 - smalldist)
                if position[i,j] == 2:
                    y = i * step + step / 2
                    x = j * step + step / 2
                    pg.draw.circle(self.screen, self.yellow, (x,y), \
                            step / 2 - smalldist)

        pg.display.update()


