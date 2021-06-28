#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sadok Mehri"

from common import Common
from color import Color
import pygame
import time
import sys
import os 

class Game(Common):
    
    def __init__(self,id = 0):
        super().__init__()
        self.board = [["." for _ in range(3)] for _ in range(3)]
        self.computer = None
        self.player = None
        self.turn = None
        self.result = None
       
    # Return Computer Choice
    def getComputerChoice(self):
        return self.computer
    
    # Return Player Choice
    def getPlayerChoice(self):
        return self.player
    
    # Set player choice
    def setPlayerChoice(self,choice:str)->None:
        self.player = choice
    
    # Set Computer choice
    def setComputerChoice(self,choice:str)->None:
        self.computer = choice

    # Return Result 
    def getResult(self):
        return self.result

    # Set Result
    def setResult(self,result:str)->None:
        self.result = result
    
    # Get Current board
    def getBoard(self):
        return self.board

    # Set Current Board
    def setBoard(self,board)->None:
        self.board = board

    # Get current turn
    def getTurn(self):
        return self.turn
    
    # Set current turn
    def setTurn(self,turn:str):
        self.turn = turn

    # Display the board
    def draw_board(self)->None:
        for i in range(0,3):
            for j in range(0,3):
                x = i* (self.DISPLAY_WIDTH  // 3)
                y = j* (self.DISPLAY_HEIGHT // 3)
                if self.board[j][i] == self.getPlayerChoice():
                    self.gameDisplay.blit(self.playerImage(),(x,y))
                elif self.board[j][i] == self.getComputerChoice():
                    self.gameDisplay.blit(self.computerImage(),(x,y))
    
    # Player Image
    def playerImage(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        imgPlayer = pygame.image.load(dir_path + '/photo/{}.png'.format(self.getPlayerChoice()))
        imgPlayer = pygame.transform.scale(imgPlayer, (110, 110))
        return imgPlayer
    
    # Computer Image
    def computerImage(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        imgComputer = pygame.image.load(dir_path + '/photo/{}.png'.format(self.getComputerChoice()))
        imgComputer = pygame.transform.scale(imgComputer, (110, 110))
        return imgComputer

    def addMenu(self)-> None:
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,70,150,50))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,140,150,50))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,210,150,50))
        self.gameDisplay.blit(self.FONT.render('X', True, Color.STONE.value), (165,80))
        self.gameDisplay.blit(self.FONT.render('O', True, Color.STONE.value), (165,150))
        self.gameDisplay.blit(self.FONT.render('Back', True, Color.STONE.value), (150,220))

    # Computer Action
    def computerMove(self)->None:
        (m, px, py) = self.minMove()
        self.board[px][py] = self.getComputerChoice()
        self.setTurn(self.getPlayerChoice())
    
    # Player Action
    def playerMove(self,px:int,py:int)->None:      
        if self.is_valid(px, py):
            self.board[px][py] = self.getPlayerChoice()
            self.setTurn(self.getComputerChoice())

    # Add Background Image to the widget
    def addBackground(self)-> None:
        self.gameDisplay.fill(Color.WHITE.value)
        self.drawGrid(self.DISPLAY_WIDTH)
    
    # Draw Grid
    def drawGrid(self,size:int)-> None:
        grid_lines = [
            ((0, size// 3),(size,size // 3)),
            ((0,2 * size // 3),(size,2* size // 3)),
            ((size // 3, 0),(size // 3,size)),
            ((2* size // 3,0),(2* size // 3,size)) 
        ]
        
        for line in grid_lines:
            pygame.draw.line(self.gameDisplay,(165,165,141),line[0],line[1],5)
    
    # Convert Coordinates From Tuple
    def convert_coordinate(self,position:tuple,size:int)->tuple:
        return (str(position[0] // (size // 3)), str(position[1] // (size // 3))) 

    # Check is it a legal move
    def is_valid(self, px:int, py:int)->bool:
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        if self.board[px][py] != '.':
            return False
        return True
    
    # Check If 3 strings are equal
    def equality(self,a:str, b:str, c:str)->bool:
        return a == b and b == c and a != "."
  
    # Check the game is over or not
    def is_end(self):   
        board = self.getBoard() 
        for i in range(0,3):
            if self.equality(board[i][0],board[i][1], board[i][2]): 
                return board[i][0]
        
        for i in range(0,3):
            if self.equality(board[0][i], board[1][i], board[2][i]): 
                return board[0][i]
                
        if self.equality(board[0][0], board[1][1], board[2][2]): 
            return board[0][0]
            
        if self.equality(board[2][0], board[1][1], board[0][2]): 
            return board[2][0]
        
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == '.'):
                    return None
        
        return '.'
    
    # Find max move for a player
    def maxMove(self):
        max_move = sys.maxsize * -1
        px = None
        py = None
        result = self.is_end()
        
        if result == self.getComputerChoice():
            return (-1, 0, 0)
        if result == self.getPlayerChoice():
            return (1, 0, 0)
        if result == '.':
            return (0, 0, 0)
   
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    self.board[i][j] = self.getPlayerChoice()
                    (m, min_i, min_j) = self.minMove()
                    if m > max_move:
                        max_move = m
                        px = i
                        py = j
                    self.board[i][j] = '.' 

        return (max_move, px, py)

    # Find min move for a player
    def minMove(self):
        min_move = sys.maxsize
        px = None
        py = None
        result = self.is_end()
        
        if result == self.getComputerChoice():
            return (-1, 0, 0)
        if result == self.getPlayerChoice():
            return (1, 0, 0)
        if result == '.':
            return (0, 0, 0)
        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    self.board[i][j] = self.getComputerChoice()
                    (m, max_i, max_j) = self.maxMove()
                    if m < min_move:
                        min_move = m
                        px = i
                        py = j
                    self.board[i][j] = '.'
                  
        return (min_move, px, py)

    # Add Menu option to the widget Win Menu
    def addMenu_win(self)-> None:
        pygame.draw.rect(self.gameDisplay,Color.WHITE.value,(73,40,205,250))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,210,150,50))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,140,150,50))
        self.gameDisplay.blit(self.FONT.render('You Win !!', True, Color.STONE.value), (130,70))
        self.gameDisplay.blit(self.FONT.render('Try Again', True, Color.STONE.value), (130,150))
        self.gameDisplay.blit(self.FONT.render('Exit', True, Color.STONE.value), (155,220))

    # Add Menu option to the widget Loosing Menu
    def addMenu_loss(self)-> None:
        pygame.draw.rect(self.gameDisplay,Color.WHITE.value,(73,40,205,250))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,210,150,50))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,140,150,50))
        self.gameDisplay.blit(self.FONT.render('You Loose !!', True, Color.STONE.value), (125,70))
        self.gameDisplay.blit(self.FONT.render('Try Again', True, Color.STONE.value), (130,150))
        self.gameDisplay.blit(self.FONT.render('Exit', True, Color.STONE.value), (155,220))
    
    # Add Menu option to the widget Draw Menu
    def addMenu_draw(self)-> None:
        pygame.draw.rect(self.gameDisplay,Color.WHITE.value,(73,40,205,250))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,210,150,50))
        pygame.draw.rect(self.gameDisplay,Color.SUN.value ,(100,140,150,50))
        self.gameDisplay.blit(self.FONT.render('Tie game !!', True, Color.STONE.value), (125,70))
        self.gameDisplay.blit(self.FONT.render('Try Again', True, Color.STONE.value), (130,150))
        self.gameDisplay.blit(self.FONT.render('Exit', True, Color.STONE.value), (155,220))

    # Winning sound
    def winningSound(self)-> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        win = pygame.mixer.Sound(dir_path+'/sound/win.ogg')
        win.play()

    # Loosing sound
    def loosingSound(self)-> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        loose = pygame.mixer.Sound(dir_path+'/sound/loose.ogg')
        loose.play()

    # Draw sound
    def drawSound(self)-> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        draw = pygame.mixer.Sound(dir_path+'/sound/tie.ogg')
        draw.play()

    # Try Again Option
    def tryAgainOption(self)-> None:
        pygame.mixer.pause()
        self.board = [["." for _ in range(3)] for _ in range(3)]
        self.initiate()
        
    # Main Logic is implemented here replay after draw
    def replay_draw(self)-> None:
        self.addMenu_draw() 
        self.drawSound()    
        working = True
        while working:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                    break
                
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                    self.button(100,140,150,50,self.tryAgainOption)
                    self.button(100,210,150,50,self.exitOption)

            pygame.display.update()
        self.exitOption()

    # Main Logic is implemented here replay after loosing
    def replay_loss(self)-> None:
        self.addMenu_loss() 
        self.loosingSound()
        working = True
        while working:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                    break
                
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                    self.button(100,140,150,50,self.tryAgainOption)
                    self.button(100,210,150,50,self.exitOption)

            pygame.display.update()
        self.exitOption()

    # Main Logic is implemented here replay after winning
    def replay_win(self)-> None:
        self.addBackground()
        self.addMenu_win() 
        self.loosingSound()
        working = True
        while working:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                    break
                
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                    self.button(100,140,150,50,self.tryAgainOption)
                    self.button(100,210,150,50,self.exitOption)

            pygame.display.update()
        self.exitOption()

    # Main Logic is implemented here
    def initiate(self)-> None:
        self.setTurn(self.getPlayerChoice())
        self.addBackground()
        working = True
        while working:
            self.clock.tick(60)
            self.setResult(self.is_end())
            curr = self.getResult() 
            if curr is not None:
                if curr == self.getPlayerChoice():
                    time.sleep(0.5)
                    self.replay_win()     
                elif curr == self.getComputerChoice():
                    time.sleep(0.5)
                    self.replay_loss()
                elif curr == '.':
                    time.sleep(0.5)
                    self.replay_draw()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                    break

                if self.getTurn() == self.getPlayerChoice():
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                        position = pygame.mouse.get_pos()
                        self.addClickSon()
                        coordinate = self.convert_coordinate(position,self.DISPLAY_WIDTH)
                        self.playerMove(int(coordinate[1]),int(coordinate[0]))
                        self.draw_board()                   
                else:
                    self.computerMove()                     
                    self.draw_board()

            pygame.display.update() 
        self.exitOption()
    
    # Deconstructeur
    def __del__(self)-> None:
        print('Destructor called, Game deleted.')