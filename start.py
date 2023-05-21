#! /usr/bin/env python 3.4.1
############################################################################
# Purpose : A very small,basic  and challenging and my first game
# Start date : 12/11/2018
# End date : 29/02/2019
# Author : Antony Mutila
# Version : 0.0.2
# Modification history : Start of the game takes place by running this script
############################################################################
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
import os
from random import randint
import level1
import level2
import level3

# setup screen diemetions
screen_width = 640
screen_height = 480

# Initialise colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,150,0)
BLACK = (0,0,0)

Bright_green = (0,255,0)
Bright_red = (150,0,0)

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
caption = pygame.display.set_caption("Hungry Snake")
clock = pygame.time.Clock()

fullscreen = False
running = True
img_dir = os.path.join(os.path.dirname( __file__ ),"asserts")
background = pygame.image.load(os.path.join(img_dir, 'select_level_img.png')).convert()
intro_image = pygame.image.load(os.path.join(img_dir,"intro_image.png")).convert_alpha()



small_font = pygame.font.SysFont("comicsansms", 20)
medium_font = pygame.font.SysFont("comicsansms", 30)
font_large = pygame.font.SysFont("comicsansms", 50)
xsmall_font = pygame.font.SysFont("comicsansms", 15)

l1 = pygame.font.SysFont("comicsansms",50)
l2 = pygame.font.SysFont("comicsansms",30)
l3 = pygame.font.SysFont("comicsansms",30)
l4 = pygame.font.SysFont("comicsansms",30)



def button(msg,x,y,w,h,ic,ac,action = None):

    mouse = pygame.mouse.get_pos() #get mouse position on the screen
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(screen, ac, (x,y,w,h))

        if click[0]==1 and action != None:
            action()


    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))
    drawText(msg, small_font, screen, (x + w / 5), (y + h / 5))


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def terminateGame():
    pygame.quit()
    exit()
    quit()

def game_level_screen():

    while running:
        global fullscreen,screen


        press = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN, 32)
                    else:
                        screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

            if event.type == pygame.QUIT or press[K_q]:
                terminateGame()

        screen.fill(GREEN)
        screen.blit(background, (0, 0))


        mousepress = pygame.mouse.get_pressed()

        drawText("Select Your Level ", font_large, screen, 100, 100)
        drawText("Press 1 for Level 1 ", small_font, screen, 100, 200)
        drawText("Press 2 for Level 2 ", small_font, screen, 100, 250)
        drawText("Press 3 for Level 3 ", small_font, screen, 100, 300)


        r2 = Rect((100, 200), l2.size("Text does Nothing here only place holders 1 "))
        r3 = Rect((100, 250), l3.size("Text does Nothing here only place holders 2 "))
        r4 = Rect((100, 300), l3.size("Text does Nothing here only place holders 3 "))

        pygame.display.update()

        # using the mouse to select a level
        if press[K_1] or (r2.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
            level1.main()
        elif press[K_2] or (r3.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
            level2.main()
        elif press[K_3] or (r4.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
            level3.main()


# making out the starting screen
def gameAbout():
    global fullscreen
    global screen
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN, 32)
                    else:
                        screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

            if event.type==pygame.QUIT:
                    terminateGame()

        screen.fill(WHITE)

        drawText("Hungry snake",small_font,screen,200,10)

        drawText("Grow your snake by eating apples and avoid hitting walls,obstacles as well as your snake's", xsmall_font, screen, 10, 50)
        drawText("own tail. ", xsmall_font, screen, 10, 80)
        drawText("A Hungry snake is made up of 3 levels:", xsmall_font, screen, 10, 100)
        drawText("Level I: Never collide in its self ", xsmall_font, screen, 10, 120)
        drawText("Level II: Avoid hitting the red boundary box hence red. ", xsmall_font, screen, 10, 140)
        drawText("Level III: Never collide in its self and avoid the falling stone. ", xsmall_font, screen, 10, 160)
        drawText("The score line in both (level I and level II) stands at 50 and  level III stands at 40. ", xsmall_font, screen, 10, 180)
        drawText("The game is won when you hit the score line of 30 in level III", xsmall_font, screen, 10, 200)
        drawText("Controls", small_font, screen, 200, 240)
        drawText("To control the snake, direction keys are used:  UP,  DOWN,  LEFT,  RIGHT or " , xsmall_font, screen, 10, 280)
        drawText("WASD short for W,A,S,D ", xsmall_font, screen,
                 10, 300)
        drawText("SPACE BAR for pause and to unpause the game ", xsmall_font, screen, 10, 320)
        drawText("f :  toggle on/off full screen mode ", xsmall_font, screen, 10, 350)
        drawText(' "play Hungry snake at your own risk and have fun"', xsmall_font, screen, 5, 370)





        button('Start', 100, 420, 100, 50, RED, Bright_red, action=level1.main)
        button('levels',250, 420, 100, 50, RED, Bright_red, action=game_level_screen)
        button('Quit', 400, 420, 100, 50, RED, Bright_red, action=terminateGame)
        pygame.display.update()

def game_intro():

    running=True
    while running:
        global screen
        global fullscreen


        screen.fill(WHITE)
        screen.blit(intro_image, (300, 200))

        drawText("Hungry Snake", font_large, screen, 150, 40)
        # drawText("Press s to start", small_font, screen, 300, 300)
        # drawText("Press q to quit", small_font, screen, 300, 350)


        button('Levels', 100, 202, 100, 50, RED, Bright_red, action=game_level_screen)
        button('Start', 100, 250, 100, 50, RED, Bright_red, action=level1.main)
        button('About', 100, 300, 100, 50, RED, Bright_red, action=gameAbout)
        button('Quit', 100, 350, 100, 50, RED, Bright_red, action=terminateGame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminateGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:

                     game_level_screen()

                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen_width,screen_height),FULLSCREEN,32)
                    else:
                        screen = pygame.display.set_mode((screen_width, screen_height),0,32)





        pygame.display.update()
        clock.tick(10)



game_intro()
