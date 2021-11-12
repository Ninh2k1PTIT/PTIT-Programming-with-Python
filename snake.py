import pygame, sys, random
from pygame.locals import *
import setting as st

UP = (0, -st.UNIT, 270)
DOWN = (0, st.UNIT, 90)
RIGHT = (st.UNIT, 0, 180)
LEFT = (-st.UNIT, 0, 0)

class Snake:
    def __init__(self):
        self.color = (148, 57, 107)
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.body = [[st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2]]
        self.saveDir = [self.direction[2]]
        self.length = 1
        self.score = 0
        self.alive = True
    
    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        flag = True
        for point, dir in zip(self.body, self.saveDir):
            img = pygame.Surface((st.UNIT, st.UNIT))
            if flag:
                img = pygame.image.load("assets/images/head_snake1.png")
                flag = False
            else:
                img = pygame.image.load("assets/images/body_snake.png")
            img = pygame.transform.scale(img, (st.UNIT, st.UNIT))
            img = pygame.transform.rotate(img, dir)
            surface.blit(img, (point[0], point[1]))

    def move(self, wall):
        old = self.body[0]
        new = [(old[0]+self.direction[0])%st.SCREEN_WIDTH, (old[1]+self.direction[1])%st.SCREEN_HEIGHT]
        if (new in wall) or (self.length > 2 and new in self.body[2:]):
            self.alive = False
        else:
            self.saveDir.insert(0, self.direction[2])
            self.body.insert(0, new)
            if len(self.body) > self.length:
                self.body.pop()
