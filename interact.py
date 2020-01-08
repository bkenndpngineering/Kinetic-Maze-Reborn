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
    def __init__(self, width, height, x, y, text, fontSize):
        pygame.font.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = str(text)
        self.color = (255,0,0)
        self.selfButton = Rect(x, y, width, height)

        self.smallFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 8)
        self.medFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 16)
        self.largeFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)
        self.hugeFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 32)

        self.pushed = False
        self.push_count = 0

        self.fontSize = fontSize #1 for small, 2 for med, 3 for large, 4 for huuge


    def reset(self):
        self.push_count = 0
        self.pushed = False

    def push(self):
        self.push_count += 1
        if self.push_count > 255:
            self.push_count = 255

        if self.push_count >= 255:
            self.pushed = True


    def get_pushed(self):
        return self.pushed

    def draw(self, screen): #x and y is dimensions, and xcenter and ycenter are coordinates

        pygame.draw.rect(screen, (self.color[0]-self.push_count, self.color[1]+self.push_count, self.color[2]), self.selfButton) #Draw Button

        newText = self.medFont.render(self.text, True, (0,0,255)) #Add text to buttons, at small font
        textSize = self.medFont.size(self.text) ## marked for future review...
        screen.blit(newText, (self.x + self.width/2 - newText.get_rect().width / 2, self.y + self.height/2 - newText.get_rect().height / 2))
        #screen.blit(newText, (self.x, self.y)) # marked for review

    def inBox(self, x, y): #if coords in box
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


class Music: #Unused for now, maybe I'll compose a quick 8bit tune to use as a theme or something
    def __init__(self, musicPath):
        self.musicPath = musicPath
        pygame.mixer.music.load(self.musicPath)
