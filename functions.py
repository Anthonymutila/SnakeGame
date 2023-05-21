# this inilize the functions to be used
# Game Over
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
# Pause and unpuase 
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)