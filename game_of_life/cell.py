import pygame as pg
from constants import *

class Cell(pg.sprite.Sprite):
    def __init__(self, state, x, y):
        pg.sprite.Sprite.__init__(self)
        # True = Alive, False = Dead
        self.state = state
        self.image = pg.Surface((CELL_SIZE, CELL_SIZE))
        color = WHITE if state else BLACK
        self.image.fill(color)
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * CELL_SIZE, y * CELL_SIZE

    def change_state(self):
        self.state = not self.state
        color = WHITE if self.state else BLACK
        self.image.fill(color)
