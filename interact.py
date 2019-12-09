import pygame
import math
import os
from pygame.locals import *
import time


#smallFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 8)
#medFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 16)
#largeFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 24)
#hugeFont = pygame.font.Font("../libs/PressStart2P-Regular.ttf", 32)

class Button: #a crude button, no color change when hover or click. Add if needed
    def __init__(self, width, height, x, y, color, text, transparency=0.5):
        pygame.font.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = str(text)
        self.color = color
        self.selfButton = Rect(x, y, width, height)
        self.transparency = transparency

        self.smallFont = pygame.font.Font("libs/PressStart2P-Regular.ttf", 8)
        self.medFont = pygame.font.Font("libs/PressStart2P-Regular.ttf", 16)
        self.largeFont = pygame.font.Font("libs/PressStart2P-Regular.ttf", 24)
        self.hugeFont = pygame.font.Font("libs/PressStart2P-Regular.ttf", 32)

    def draw(self, screen): #x and y is dimensions, and xcenter and ycenter are coordinates

        pygame.draw.rect(screen, self.color, self.selfButton) #Draw Button

        newText = self.smallFont.render(self.text, True, (0,0,255)) #Add text to buttons, at small font
        textSize = self.smallFont.size(self.text) ## marked for future review...
        #screen.blit(newText, (self.xcenter - (textSize[0] / 2.), self.ycenter - (textSize[1] / 2.)))
        screen.blit(newText, (self.x, self.y)) # marked for review

    def inBox(self, x, y): #if mouse in box
        if (self.x + self.width) > x > (self.x) and (self.y + self.width) > y > (self.y):
            return True
        else:
            return False

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
