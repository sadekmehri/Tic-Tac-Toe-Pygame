#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sadok Mehri"

from abc import ABC, abstractmethod
import pygame
import time
import sys
import os 
    
class Common(ABC):

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.DISPLAY_WIDTH = 345
        self.DISPLAY_HEIGHT = 345
        self.FONT = pygame.font.SysFont("comicsansms", 20)
        self.addTitle()
        self.addIcon() 
        self.gameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT))
    
    # Add Title to the widget
    def addTitle(self)-> None:
        pygame.display.set_caption("Tic Tac Toe")
    
    # Add Icon to the widget
    def addIcon(self)-> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        gameIcon = pygame.image.load(dir_path + '/photo/Tic_tac_toe.png')
        pygame.display.set_icon(gameIcon)
        
    # Add click sound effect to the widget
    def addClickSon(self)-> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        clicked = pygame.mixer.Sound(dir_path+'/sound/click.ogg')
        clicked.play()

    # Button Click event
    def button(self,x:int,y:int,w:int,h:int,action=None)-> None:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y and click[0] == 1 and action is not None:
            self.addClickSon()
            time.sleep(0.5)
            action()
    
    # Exit Option
    def exitOption(self)-> None:
        pygame.quit()
        sys.exit(0)

    # Add Background Image to the widget
    @abstractmethod
    def addBackground(self)-> None:
        pass
 
    # Main Logic is implemented here
    @abstractmethod
    def initiate(self)-> None:
        pass