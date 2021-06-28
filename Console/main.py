#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import system
import sys

__author__ = "Sadok Mehri"

class Game:

    def __init__(self):
        self.initialize_game()
    
    # Initialise the board
    def initialize_game(self)->None:
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
        [print(row) for row in self.board]

    # Choose side
    def choose_side(self)->None:
        while True:
            side = str(input("Choose X or O : "))
            side = side.strip().lower()
            if side == "x" :
                self.setPlayerChoice("x")
                self.setComputerChoice("o")
                break
            elif side == "o":
                self.setPlayerChoice("o")
                self.setComputerChoice("x")
                break

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

    # Computer Action
    def computerMove(self)->None:
        (m, px, py) = self.minMove()
        self.board[px][py] = self.getComputerChoice()
        self.setTurn(self.getPlayerChoice())
    
    # Player Action
    def playerMove(self)->None:
        while True:
            px = self.choose('Insert the X coordinate: ')
            py = self.choose('Insert the Y coordinate: ')       
            if self.is_valid(px, py):
                self.board[px][py] = self.getPlayerChoice()
                self.setTurn(self.getComputerChoice())
                break
            else:
                print('The move is not valid! Try again.')
    
    # Choose Option
    def choose(self,msg:str)->int:
        while True:
            try:
                side = int((input(msg)).strip().lower())
            except ValueError as e:
                print("Only degit. Please Try Again !!" )
                continue
            else:
                return side 

    # Play logic here
    def play(self)-> None:
        self.choose_side()
        self.setTurn(self.getPlayerChoice())
        while True:
            self.draw_board()
            self.setResult(self.is_end())
            curr = self.getResult() 

            if curr is not None:
                if curr == 'x':
                    print('The winner is X!')
                elif curr == 'o':
                    print('The winner is O!')
                elif curr == '.':
                    print("It's a tie!")
                break

            if self.getTurn() == self.getPlayerChoice():
                self.playerMove()
            else:
                self.computerMove()        

    # Deconstructeur
    def __del__(self)-> None:
        print('Destructor called, Game deleted.')

# Main function
if __name__ == '__main__':
    system('cls')
    g = Game()
    g.play()
    del g