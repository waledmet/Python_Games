#install pygame 
#pip install pygame
import pygame
from pygame.locals import *

# initialize pygame
pygame.init()

#define color
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}


size = width , height  = 640 , 240

#screen ==> Surface
screen  =  pygame.display.set_mode(size)

#change screen title
caption="Welcome to First App"
pygame.display.set_caption(caption)

background = BLACK

#fills the  screen with the specified color.
screen.fill(background)
pygame.display.update()




running= True
while  running :
    #get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
            """ if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN """

    screen.fill(background)
    pygame.display.update()

#quit pygame
pygame.quit()