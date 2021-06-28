#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sadok Mehri"

from color import Color
from game import Game
from os import system
import pygame
import os 

class Main(Game):

    def __init__(self):
        super().__init__()
        self.gameBackground = self.getBackground()

    # Add Background Image to the widget
    def getBackground(self)-> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        gameBackground = pygame.image.load(dir_path + '/photo/background.jpg')
        gameBackground = pygame.transform.scale(gameBackground, (self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        return gameBackground
    
    # Add Menu option to the widget
    def addMenu(self)-> None:
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,100,150,50))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,190,150,50))
        self.gameDisplay.blit(self.FONT.render('Proceed', True, Color.STONE.value), (140,110))
        self.gameDisplay.blit(self.FONT.render('Exit', True, Color.STONE.value), (150,200))
        
    # You choose to return home
    def returnOption(self):
        self.initiate()

    # You choose x Option
    def xOption(self):
        self.setPlayerChoice('x')
        self.setComputerChoice('o')
        Game.initiate(self)

    # You choose o Option
    def yOption(self):
        self.setPlayerChoice('o')
        self.setComputerChoice('x')
        Game.initiate(self)

    # Offline Option
    def offlineOption(self)-> None:
        self.gameDisplay.blit(self.getBackground(), (0, 0))
        Game.addMenu(self)
        working = True
        while working:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                    break
                
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                    self.button(100,70,150,50,self.xOption)
                    self.button(100,140,150,50,self.yOption)
                    self.button(100,210,150,50,self.returnOption)

            pygame.display.update()
        self.exitOption()

    # Main Logic is implemented here
    def initiate(self)-> None:
        self.gameDisplay.blit(self.getBackground(), (0, 0))
        self.addMenu()     
        working = True
        while working:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                    break
                
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                    self.button(100,100,150,50,self.offlineOption)
                    self.button(100,190,150,50,self.exitOption)

            pygame.display.update()     
        self.exitOption()
        
    # Deconstructeur
    def __del__(self)-> None:
        print('Destructor called, Main deleted.')
        

# Main function
if __name__ == "__main__":
    system('cls')
    os.environ["SDL_VIDEO_WINDOW_POS"] = "400,200"
    game = Main()
    game.initiate()
    del game