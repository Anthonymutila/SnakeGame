#! /usr/bin/env python 3.4.1
############################################################################
# Purpose : A very small,basic  and challenging and my first game

# Start date : 13/12/2018
# End date : 29/02/2019
# Author : Antony Mutila
# Version : 0.0.2
# Modification history : Start of the game takes place by running this script
############################################################################

import pygame
from  pygame.locals import *
from sys import exit
from random import randint
import os
import level3
import level2
counter = 0
score = 0
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,150,0)
BLACK = (0,0,0)

screen_width = 640
screen_height = 480

Bright_green = (0,255,0)
Bright_red = (150,0,0)
pause = False
fullscreen =False

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

item_collect = pygame.mixer.Sound("asserts/eat.wav")
explosion = pygame.mixer.Sound("asserts/explo2.wav")
pygame.mixer.music.load("asserts/background.ogg")
img_dir = os.path.join(os.path.dirname(__file__),"asserts")

pygame.display.set_caption('hungry snake')
small_font = pygame.font.SysFont("comicsansms", 20)
medium_font =pygame.font.SysFont("comicsansms", 30)
font_large =pygame.font.SysFont("comicsansms", 50)
xsmall_font = pygame.font.SysFont("comicsansms", 15)

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1,WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def terminateGame():
    pygame.quit()
    exit()
    quit()


def button(msg, x, y, w, h, ic, ac, action=None):
 mouse = pygame.mouse.get_pos()  # get mouse position on the screen
 click = pygame.mouse.get_pressed()

 # button("Start", 100, 300, 100, 40, RED, Bright_red, action=None)

 if x + w > mouse[0] > x and y + h > mouse[1] > y:
  pygame.draw.rect(screen, ac, (x, y, w, h))
  if click[0] == 1 and action != None:
   action()


 else:
  pygame.draw.rect(screen, ic, (x, y, w, h))
 drawText(msg, small_font, screen, (x + w / 5), (y + h / 5))


def unpause():
 global pause
 pause = False
 pygame.mixer_music.unpause()


def paused():
 drawText('Paused', medium_font, screen, 233, 150)
 global pause
 while pause:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    terminateGame()
   if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
     pause = False

     unpause()

    # do not forgot to add pause functionality here! keys and evryyhing

  button('Resume', 175, 300, 100, 50, GREEN, Bright_green, unpause)
  button('Quit', 350, 300, 100, 50, Bright_red, RED, terminateGame)

  pygame.display.update()


def switchLevevel():
 while True:
  for event in pygame.event.get():
          if event.type==pygame.QUIT:
              terminateGame()
  screen.fill(BLACK)
  drawText("Level II complete", font_large, screen, 100, 150)
  drawText("hey there you're done with level II\
   ", small_font, screen, 100, 220)
  drawText("Press the Green button for level III!\
    ", small_font, screen, 100, 250)

  button("Level III", 150, 360, 100, 50, GREEN, Bright_green, action=level3.main)
  button("Quit", 330, 360, 100, 50, Bright_red,RED, action=terminateGame)

  pygame.display.update()




def gameOver():
 global score
 gameover = True
 drawText('Game Over', font_large, screen, 200, 90)
 drawText("Highest Score: " +  str(score),medium_font,screen,200,170)
 while gameover:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    terminateGame()

  button('Replay', 175, 300, 100, 50, GREEN, Bright_green,action= level2.main)
  button('Quit', 350, 300, 100, 50, Bright_red, RED, action=terminateGame)

  pygame.display.update()

def gameOver():
 global score


 global screen
 gameover = True
 drawText('Game Over', font_large, screen, 200, 90)
 drawText("Highest Score: " +  str(score),medium_font,screen,200,170)
 score = score - score
 while gameover:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    terminateGame()


  # screen.fill(WHITE)
  button('Replay', 175, 300, 100, 50, GREEN, Bright_green,action= main)
  button('Quit', 350, 300, 100, 50, Bright_red, RED, action=terminateGame)

  pygame.display.update()




def main():
 while True:
  b = []
  def update():
   global counter
   counter = (counter+1)%7
  def blast(w,h):
   image = pygame.image.load(os.path.join(img_dir, 'explosed-sprite.png')).convert()
   width,height=image.get_size()
   for i in range(int( width / w)):
    b.append(image.subsurface((i*w,0,w,h)))

  up = 1
  down = 2
  right = 3
  left = 4
  step = 20
  block =[20,20]
  x = randint(1,20)
  y = randint(2,22)
  applexy = []
  snakexy = [int(x * 20),int(y * 20)]
  snakelist = [[x * 20,y * 20],[(x - 20) * 20,(y * 20)]]
  apple = 0
  running = 0
  grow = 0
  direction = right
  global score

  start = 0
  # screen = pygame.display.set_mode((screen_width,screen_height),0,24)
  clock = pygame.time.Clock()

#game loop
  pygame.mixer.music.play(-1, 0.0)
  pygame.mixer.music.set_volume(0.15)
  while not running:
   global score
   global  pause
   global fullscreen
   global screen
   pressed = pygame.key.get_pressed()
   for event in pygame.event.get():
    if event.type == QUIT or pressed[K_q]:
     terminateGame()

    if event.type == pygame.KEYDOWN:

     if event.key == pygame.K_SPACE:
          pause = True
          pygame.mixer_music.pause()
          paused()
     if event.key == pygame.K_f:
      fullscreen = not fullscreen
      if fullscreen:
       screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN, 32)
      else:
       screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

   if pressed[K_LEFT]or pressed[K_a] and direction!=right:
     direction = left
   elif pressed[K_RIGHT] or pressed[K_d] and direction != left:
      direction = right
   elif pressed[K_UP] or pressed[K_w] and direction != down:
      direction = up
   elif pressed[K_DOWN] or pressed[K_s] and direction != up:
      direction = down
   if direction == right:

    snakexy[0] = snakexy[0]+ step
    if snakexy[0]>= 620:
     running = True


#snake movement
   elif direction == left:
    snakexy[0] = snakexy[0] - step
    if snakexy[0]<20:
     running = True

   elif direction==up:
    snakexy[1]= snakexy[1]-step
    if snakexy[1]<20:
        running = True
   elif direction == down:
    snakexy[1] = snakexy[1] + step
    if snakexy[1] >= 460:
        running = True
   if snakelist.count(snakexy) > 0:
       running = True
   if apple == 0:
    x1 = randint(2,30)
    y1 = randint(2,22)
    applexy = [int(x1 * step),int(y1 * step)]
    apple = 1

   snakelist.insert(0,list(snakexy))
   if snakexy[0] == applexy[0] and snakexy[1] == applexy[1]:
    apple = 0
    score = score+1
    item_collect.play()

   else:
    snakelist.pop()

#display on the screen

   screen.fill(BLACK)##############################################################################3333
   if score >=2:
      pygame.mixer.music.stop()
      switchLevevel()



   drawText("Score :{}".format(str(score)), small_font, screen, 500, 10)
   drawText("Level  : 2", small_font, screen, 10, 10)

   pygame.draw.line(screen,RED,(0,0),(0,480),20)
   pygame.draw.line(screen,RED,(0,0),(640,0),20)
   pygame.draw.line(screen,RED,(640,0),(640,480),20)
   pygame.draw.line(screen,RED,(0,480),(640,480),20)
   pygame.draw.rect(screen,RED,Rect(applexy,block),0)
   for event in snakelist:
    pygame.draw.rect(screen,(GREEN),Rect(event,block))
   pygame.display.flip()
   clock.tick(15)

  if  running == True:
   blast(20,20)
   explosion.play()
   pygame.mixer.music.stop()
   for event in range(7):
    screen.blit(b[counter],(snakexy[0],snakexy[1]))
    update()
    pygame.display.update()
    clock.tick(10)

   gameOver()



















   # drawText("GAME OVER", font_large, screen, 50, 50)
   # drawText("Press s To Play Again",small_font, screen, 50, 250)
   # drawText("Press l For Level Selection ", small_font, screen, 50, 300)
   # drawText("Score :{}".format(int(score)), small_font, screen, 200, 200)
   # over = pygame.small_font.SysFont("comicsansms",40)
   # text5=over.render("GAME OVER",True,(0,255,0))
   # s1 = pygame.small_font.SysFont("comicsansms",30)
   # s2 = pygame.small_font.SysFont("comicsansms",30)
   # screen.blit(text5,(50,50))
   # screen.blit(text4,(200,200))
   # screen.blit(s1.render("Press snake To Play Again",True,(0,255,0)),(50,250))
   # screen.blit(s2.render("Press l For Level Selection ",True,(0,255,0)),(50,300))

   # pygame.display.flip()
   # while True:
   #  for event in pygame.event.get():
   #   if event.type == QUIT:
   #     terminateGame()
   #  pressed = pygame.key.get_pressed()
   #  if pressed[K_q]:
   #   terminateGame()
   #  if pressed[K_s]:
   #   main()
   #  if pressed[K_l]:
   #   break
   # break

 
 

if __name__=='__main__':
 main() 



















