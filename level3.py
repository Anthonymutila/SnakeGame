#! /usr/bin/env python
############################################################################
# Purpose : A very small,basic and my first game
# Usages : Learning purpose
# Start date : 30/12/2018
# End date : 29/02/2019
# Author : Antony Mutiia
# Version : 0.0.2
# Modification history : Level3 - Stone Fall 
############################################################################



import pygame
from  pygame.locals import *
from sys import exit
from random import randint
import os

import level1
import level2
import level3

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,150,0)
BLACK = (0,0,0)

Bright_green = (0,255,0)
Bright_red = (150,0,0)

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

item_collect = pygame.mixer.Sound("asserts/eat.wav")
explosion = pygame.mixer.Sound("asserts/explo2.wav")

img_dir = os.path.join(os.path.dirname(__file__),"asserts")
# sounds = os.path.join(os.path.dirname(__file__),"asserts/audio")
background = pygame.image.load(os.path.join(img_dir, 'select_level_img.png')).convert()

counter = 0
score = 0

pause = False
fullscreen=False
small_font = pygame.font.SysFont("comicsansms", 20)
medium_font =pygame.font.SysFont("comicsansms", 30)
font_large =pygame.font.SysFont("comicsansms", 50)
xsmall_font = pygame.font.SysFont("comicsansms", 15)



def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def terminateGame():
    pygame.quit()
    exit()
    quit()


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

def unpause():
    global pause
    pause = False
    pygame.mixer_music.unpause()

def paused():
    drawText('Paused', small_font, screen, 233, 150)
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminateGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                            pause = False
                            unpause()



        button('Resume', 175, 300, 100, 50, GREEN, Bright_green,unpause)
        button('Quit', 350, 300, 100, 50, Bright_red,RED,terminateGame)

        pygame.display.update()

def gameOver():
 global score
 
 gameover = True
 drawText('Game Over', font_large, screen, 200, 90)
 drawText("Highest Score: " +  str(score),medium_font,screen,200,170)
 score = score - score
 while gameover:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    terminateGame()

  button('Replay', 175, 300, 100, 50, GREEN, Bright_green,action= main)
  button('Quit', 350, 300, 100, 50, Bright_red, RED, action=terminateGame)

  pygame.display.update()

def gameWon():
 global score
 score = 0
 while True:
  for event in pygame.event.get():
          if event.type==pygame.QUIT:
              terminateGame()
          if event.type==pygame.KEYDOWN:
              pass

  screen.fill(BLACK)
  drawText("You Win Nice work", font_large, screen, 100, 150)
  button('levels',250, 420, 100, 50, RED, Bright_red, action=game_level_screen)

  button("Quit", 350, 360, 100, 50, Bright_red, RED, action=terminateGame)

  pygame.display.update()


def game_level_screen():

    while True:
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


        l1 = pygame.font.SysFont("comicsansms",50)
        l2 = pygame.font.SysFont("comicsansms",30)
        l3 = pygame.font.SysFont("comicsansms",30)
        l4 = pygame.font.SysFont("comicsansms",30)


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








def main():
 while True:
  b = []
  def update():
   global counter
   counter = (counter+1)%7
  def blast(w,h):
   # image = pygame.image.load("asserts/images/explosed-sprite.png").convert_alpha()

   image = pygame.image.load(os.path.join(img_dir,'explosed-sprite.png')).convert()
   width,height = image.get_size()
   for i in range(int(width/w)):
    b.append(image.subsurface((i*w,0,w,h)))
   #print red_apple
  up = 1
  down = 2
  right = 3
  left = 4
  step = 20
  block = [20,20]
  x = randint(1,20)
  y = randint(2,22)
  applexy = []
  x3 = randint(1,25)
  check = [x3*20,-20]
  snakexy =[int(x*20),int(y*20)]
  snakelist = [[x*20,y*20],[(x-20)*20,(y*20)]]
  apple = 0
  running =  False
  grow = 0
  direction = right
  global score
 
  start = 0
  draw = []
  # screen = pygame.display.set_mode((screen_width,screen_height),0,24)
  clock = pygame.time.Clock()

#game loop
  pygame.mixer.music.play(-1,0.0)
  pygame.mixer.music.set_volume(0.15)
  while not running:
   global score
   global pause
   global fullscreen
   global screen
   pressed = pygame.key.get_pressed()
   for event in pygame.event.get():
       if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_SPACE:
               pause = True
               pygame.mixer_music.pause()
               paused()
           if event.key == pygame.K_f:
               fullscreen = not fullscreen
               if fullscreen:
                   screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN, 32)
               else:
                   screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)



       elif event.type == QUIT or pressed[K_q]:
        terminateGame()
   # image2 = pygame.image.load("asserts/images/stone.png").convert_alpha()
   image2 = pygame.image.load(os.path.join(img_dir, "stone.png")).convert_alpha()

   pygame.transform.scale(image2,(20,20))
   check[1] = check[1]+step
   if check[1]>480:
    x2 = randint(1,25)
    check[0] = x2 * 20
    check[1] = 0

   if pressed[K_LEFT] or pressed[K_a] and direction!=right:
     direction = left
   elif pressed[K_RIGHT] or pressed[K_d] and direction!=left:
      direction = right
   elif pressed[K_UP] or pressed[K_w] and direction!=down:
      direction = up
   elif pressed[K_DOWN] or pressed[K_s] and direction!=up:
      direction=down
   if direction==right:
    snakexy[0]=snakexy[0]+step
    if snakexy[0]>=640:
     snakexy[0]=0

   elif direction==left:
    snakexy[0]=snakexy[0]-step
    if snakexy[0]<0:
     snakexy[0]=620

   elif direction == up:
    snakexy[1] = snakexy[1]-step
    if snakexy[1]<0:
     snakexy[1] = 460
   elif direction == down:
    snakexy[1]=snakexy[1]+step
    if snakexy[1] >= 480:
     snakexy[1] = 0

   if snakelist.count(snakexy) >0:
    for i in snakelist:
     if i == snakexy:
      draw.append(i)
      break
    running = True
   if apple == False:
    x1 = randint(1,31)
    y1 = randint(2,22)
    applexy =[int(x1*step),int(y1 * step)]
    apple = 1

   snakelist.insert(0,list(snakexy))
   if snakexy[0] == applexy[0] and snakexy[1] ==  applexy[1]:
    apple = 0
    score = score + 1
    if score >=5:######################work on this next time 
        gameWon()
      
        
      

    # score = score+1
   
    print(str(score))
    item_collect.play()
   else:
    snakelist.pop()

   if snakelist.count(check)>0:
    for i in snakelist:
     if i == check:
      draw.append(i)
      break
    running = True

#display on the screen
   screen.fill(BLACK)

  
        # pygame.mixer.music.stop()
        # gameWon()
   drawText("Score :{}".format(int(score)), small_font, screen, 500, 10)
   drawText("Level  : 3", small_font, screen, 10, 10)

   screen.blit(image2,check)
   pygame.draw.rect(screen,(RED),Rect(applexy,block),0)
   for i in snakelist:
    pygame.draw.rect(screen,(GREEN),Rect(i,block))
   pygame.display.flip()
   clock.tick(15)

  if running == True:
   blast(20,20)
   explosion.play()
   pygame.mixer_music.stop()
   for i in range(7):
    screen.blit(b[counter],(tuple(draw)))
    update()
    pygame.display.update()
    clock.tick(10)

# Game over display

   # screen.fill(BLACK)
   gameOver()




if __name__=='__main__':
 main()

















