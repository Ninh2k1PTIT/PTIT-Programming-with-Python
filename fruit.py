import pygame, sys, random
from pygame.locals import *
import setting as st

class Fruit:
    def __init__(self, wall, snake):
        self.position = random.choice([p for p in st.GRID if (p not in wall) and (p not in snake)])
        #self.position = [random.randrange(0, st.SCREEN_WIDTH, st.UNIT), random.randrange(0, st.SCREEN_HEIGHT, st.UNIT)]
        img = pygame.image.load(random.choice(["assets/images/apple.png", "assets/images/banana.png", "assets/images/grape.png"])).convert_alpha()
        self.img = pygame.transform.scale(img, (st.UNIT, st.UNIT))

    def draw(self, surface):
        surface.blit(self.img, (self.position[0] , self.position[1]))