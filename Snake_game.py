import pygame
import time
from random import random, randint

pygame.init()
screen = pygame.display.set_mode ((601, 601))
pygame.display.set_caption ("Snake")
running = True
clock = pygame.time.Clock()

# color
GREEN = (0, 238, 118)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128,128,128)

font_small = pygame.font.SysFont ('Arial', 30)
font_medium = pygame.font.SysFont ('Arial', 45, True, True)
font_big = pygame.font.SysFont ('Arial', 60, True)
font_troll = pygame.font.SysFont ('Arial', 25, False, True)
font_cre = pygame.font.SysFont ('Arial', 14, True, True)

score = 0
pause = False

# toa do snake
snakes = [[2, 5]]
direction = "right"

# toa do apple
apple = [randint (0, 19), randint (0, 19)]
while (apple == snakes[0]):
    apple = [randint (0, 19), randint (0, 19)]

while (running == True):
    clock.tick (60)
    screen.fill (BLACK)
    
    # draw grid
    for i in range (21):
        pygame.draw.line (screen, GRAY, (0, i * 30), (600, i * 30))
        pygame.draw.line (screen, GRAY, (i * 30, 0), (i * 30, 600))
        
    tail_x = snakes[0][0]
    tail_y = snakes[0][1]
    
    # draw snake
    for snake in snakes:
        if (snake == snakes[-1]):
            pygame.draw.rect (screen, GREEN, (snake[0] * 30 + 1, snake[1] * 30 + 1, 25, 25))
        pygame.draw.rect (screen, GREEN, (snake[0] * 30 + 1, snake[1] * 30 + 1, 29, 29))
    
    # draw apple
    pygame.draw.rect (screen, RED, (apple[0] * 30 + 7, apple[1] * 30 + 7, 17, 17))
    
    # draw score
    score_screen = font_small.render ("Score: " + str (score), True, WHITE)
    screen.blit (score_screen, (10, 10))
    
    
    # check poin
    if (snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]):
        snakes.insert (0, [tail_x, tail_x]) 
        apple = [randint (0, 19), randint (0, 19)]
        score += 1
        while (apple in snakes):
            apple = [randint (0, 19), randint (0, 19)]
        
        
    # draw game OVER
    if (pause == True):
        game_over = font_big.render ("Game OVER!!", True, WHITE)
        score_point = font_medium.render ("Score: " + str (score), True, WHITE)
        replay = font_small.render ("Press Space to Replay", True, WHITE)
        ga_VCL = font_troll.render ("Ban choi Ga VCL :)))))", True, GRAY)
        cre = font_cre.render ("@NSTCrystal", True, WHITE)
        screen.blit (game_over, (140, 110))
        screen.blit (score_point, (420, 200))
        screen.blit (replay, (175, 380))
        screen.blit (ga_VCL, (20, 550))
        screen.blit (cre, (520, 580))
        
        
    # snake move
    if (pause == False):
        if (direction == "up"):
            snakes.append ([snakes[-1][0], snakes[-1][1] - 1])
            snakes.pop (0)        
        if (direction == "down"):
            snakes.append ([snakes[-1][0], snakes[-1][1] + 1])
            snakes.pop (0)  
        if (direction == "left"):
            snakes.append ([snakes[-1][0] - 1, snakes[-1][1]])
            snakes.pop (0)   
        if (direction == "right"):
            snakes.append ([snakes[-1][0] + 1, snakes[-1][1]])
            snakes.pop (0)    
    
    
    # check crash
    if (snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19):
        # print ("Ban da Thua!!")
        pause = True
        
    # for i in range (len (snakes) - 1):
    #     if (snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]):
    #         pause = True
    if (snakes[-1] in snakes[:-1]):
        pause = True
    
    
    time.sleep (0.15)
    # time.sleep (1)
    
    
    # keydown
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_UP and direction != "down"):
                direction = "up"
            if (event.key == pygame.K_DOWN and direction != "up"):
                direction = "down"
            if (event.key == pygame.K_LEFT and direction != "right"):
                direction = "left"
            if (event.key == pygame.K_RIGHT and direction != "left"):
                direction = "right"
            if (event.key == pygame.K_SPACE and pause == True):
                pause = False
                snakes = [[2, 5]]
                direction = "right"
                apple = [randint (0, 19), randint (0, 19)]
                while (apple == snakes[0]):
                    apple = [randint (0, 19), randint (0, 19)]
                score = 0
                
            
    pygame.display.flip()
    
pygame.quit()