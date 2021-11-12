import pygame, sys, random
from pygame.locals import *
import setting as st

class Wall:
    def __init__(self):
        self.position = []
        for i in range(0, st.SCREEN_HEIGHT, st.UNIT):
            for j in range(0, st.SCREEN_WIDTH, st.UNIT):
                if i == 0 or i == st.SCREEN_HEIGHT-st.UNIT:
                    self.position.append([j, i])
                else:
                    if j == 0 or j == st.SCREEN_WIDTH-st.UNIT:
                        self.position.append([j, i])

    def draw(self, surface):
        for point in self.position:
            img = pygame.image.load("assets/images/wall.png")
            img = pygame.transform.scale(img, (st.UNIT, st.UNIT))
            surface.blit(img, point)