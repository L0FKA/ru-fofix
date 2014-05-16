# -*- coding: utf-8 -*-
#   FoFiX skin helper
#   Nickman 2009
#   L0FKA 2014
import sys, os, pygame
from pygame.locals import * 

CAPTION = "FoFiX skin helper"
fontname = "menu.ttf"
logoname = "gameresults.png"
RESOLUTION = (1024, 512)
screen_x,screen_y = RESOLUTION

pygame.init()
pygame.mouse.set_visible(1)
pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(CAPTION)
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

logo = os.path.join("skin", logoname)
if not os.path.exists(logo):
    pygame.display.quit()
    sys.exit("No logo Texture")

logo_surface = pygame.image.load(logo)
logo_surface = pygame.transform.scale(logo_surface, RESOLUTION)

cFont= os.path.join("skin", fontname)
if pygame.font:
    font = pygame.font.SysFont("default", 26)
    if os.path.exists(cFont):
        font = pygame.font.Font(cFont, 26)

def toPrc(x,y):
    """Converts 'Coordinates' to 'Precentage' format"""
    return float(x) / float(screen_x), float(y) / float(screen_y)

def printmousecords():
    x,y = pygame.mouse.get_pos()
    new_x, new_y = toPrc(x,y)

    mouse_x = str(round(new_x,5))
    mouse_y = str(round(new_y,5))

    stringX = ("Mouse X: " + mouse_x + "|>|" + `x`)
    stringY = ("Mouse Y: " + mouse_y + "|>|" + `y`)
    # Centered (jumpy) [screen_x/2 - fSize[0]/2, screen_y/2 - fSize[1]/2]
    fSize = font.size(stringX)
    textpos1 = screen_x/2.5, screen_y/2 - fSize[1]/2
    textpos2 = screen_x/2.5, screen_y/2 + fSize[1]/2
    
    text1 = font.render(stringX, 1, (255, 255, 255))
    text2 = font.render(stringY, 1, (255, 255, 255))
    screen.blit(logo_surface, (0, 0))
    screen.blit(text1, textpos1)
    screen.blit(text2, textpos2)
    
    return
   
def input(events): 
   for event in events: 
      if event.type == QUIT:
         pygame.display.quit()
         sys.exit(0)
      elif event.type == KEYDOWN and event.key == K_ESCAPE:
         pygame.display.quit()
         sys.exit(0)
      else: 
         return

# MainLoop
while True:
   clock.tick(60)
   input(pygame.event.get())
   printmousecords()
   pygame.display.flip() 
