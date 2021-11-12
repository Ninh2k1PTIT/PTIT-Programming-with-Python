import pygame, sys, random, fruit, snake, wall
from pygame.locals import *
import setting as st
       
def play(SCREEN):
    SCREEN.fill((255, 255, 255))
    s = snake.Snake()
    w = wall.Wall()
    f = fruit.Fruit(w.position, s.body)
    FONT = pygame.font.SysFont("times new roman", 20)

    background_game = pygame.image.load("assets/images/background_game.jpg").convert_alpha()
    background_game = pygame.transform.scale(background_game, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))

    background_over = pygame.image.load("assets/images/gameover.png").convert_alpha()
    background_over = pygame.transform.scale(background_over, (200, 200))
    while True:
        while s.alive:
            SCREEN.blit(background_game, (0, 0))
            s.control()
            s.move(w.position)
            if s.body[0][:2] == f.position:
                f = fruit.Fruit(w.position, s.body)
                s.score += 1
                s.length += 1
            w.draw(SCREEN)
            s.draw(SCREEN)
            f.draw(SCREEN)
            SCREEN.blit(FONT.render(f"Score: {s.score}", True, (255, 0, 0)), (5, 10))
            pygame.display.update()
            pygame.time.Clock().tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if pos[0] in range(st.SCREEN_WIDTH//2-100, st.SCREEN_WIDTH//2+101) and pos [1] in range(st.SCREEN_HEIGHT//2-100, st.SCREEN_HEIGHT//2+101):
                    play(SCREEN)
        pygame.display.update()
        SCREEN.blit(background_over, (st.SCREEN_WIDTH/2-100, st.SCREEN_HEIGHT/2-100))
    
def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE GAME")
    FONT = pygame.font.SysFont("", 50)

    #Hinh nen menu
    BACKGROUND = pygame.image.load("assets/images/background_menu.jpg").convert_alpha()
    BACKGROUND = pygame.transform.scale(BACKGROUND, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
    SCREEN.blit(BACKGROUND, (0, 0))

    #Button play game
    BUTTON = pygame.image.load("assets/images/button_play.png").convert_alpha()
    BUTTON = pygame.transform.scale(BUTTON, (100, 50))
    possition_button = pygame.Rect(st.SCREEN_WIDTH/2-50, st.SCREEN_HEIGHT/2-25, 100, 50)
    SCREEN.blit(BUTTON, possition_button)

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if pos[0] in range(possition_button.left, possition_button.right+1) and pos [1] in range(possition_button.top, possition_button.bottom+1):
                    play(SCREEN)

main()