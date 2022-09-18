import pygame
from pygame.locals import *


size = width, height = 640, 320

GREEN = (150, 255, 150)
RED = (255, 0, 0)


ball_x = 0
ball_y = 0

pygame.init()
screen = pygame.display.set_mode(size)

radius = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        keys=pygame.key.get_pressed()
        print("keys==",keys[K_LEFT])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x -= 1
            if event.key == pygame.K_RIGHT:
                ball_x += 1
            if event.key == pygame.K_UP:
                ball_y -= 1
            if event.key == pygame.K_DOWN:
                ball_y += 1
    
    
    screen.fill(GREEN)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius,0)
    pygame.display.update()

pygame.quit()