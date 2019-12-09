import pygame
import math
import os
from pygame.locals import *
import time


smallFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 8)
medFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 16)
largeFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 24)
hugeFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 32)

class Button: #a crude button, no color change when hover or click. Add if needed
    def __init__(self):
        pass
    def draw(self,x, y, xcenter, ycenter, color, text): #x and y is dimensions, and xcenter and ycenter are coordinates
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.x = x
        self.y = y

        self.text = text
        self.color = color

        self.selfButton = Rect(xcenter - (x/2), ycenter - (y/2), x, y)

        pygame.draw.rect(screen,color,Rect(xcenter - (x/2), ycenter - (y/2), x, y)) #Draw Button

        newText = smallFont.render(text, True, (0,0,255)) #Add text to buttons, at small font
        textSize = myfont.size(text)
        screen.blit(newText, (xcenter- (textSize[0] / 2.),ycenter - (textSize[1] / 2.)))
        pygame.display.update()

    def inBox(self): #if mouse in box

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if selfButton.collidepoint(mouse):
                return True

'''
How to detect clicks
events = pygame.event.get()
for event in events:
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        if starBut.inBox() == True:
            l.debug("START BUTTON CLICKED")

'''

class Music:
    def __init__(self, musicPath):
        self.musicPath = musicPath
        pygame.mixer.music.load(self.musicPath)
