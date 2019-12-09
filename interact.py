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
    def __init__(self, x, y, xcenter, ycenter, color, text, transparency=0.5):
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.x = x
        self.y = y
        self.text = str(text)
        self.color = color
        self.selfButton = Rect(xcenter - (x / 2), ycenter - (y / 2), x, y)
        self.transparency = transparency

    def draw(self, screen): #x and y is dimensions of the box (size), and xcenter and ycenter are coordinates (where to draw)

        pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2], self.transparency), Rect(self.xcenter - (self.x/2), self.ycenter - (y/2), self.x, self.y)) #Draw Button

        newText = smallFont.render(self.text, True, (0,0,255)) #Add text to buttons, at small font
        textSize = medFont.size(self.text) ## marked for future review...
        screen.blit(newText, (self.xcenter - (textSize[0] / 2.), self.ycenter - (textSize[1] / 2.)))

    def inBox(self, x, y): #if mouse in box
        if self.selfButton.collidepoint((x, y)):
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
