# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:19:06 2019

@author: Chris M
"""
import random

class Agent():
    
    _x = 0
    _y = 0
    environment = []
    agents = []
    
    def __init__ (self, environment:list, agents:list):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents

    def move(self):        
        #move agent
        if random.random() < 0.5:
            self._x = (self._x +1) % 99
        else:
            self._x = (self._x -1) % 99
    
        if random.random() > 0.5:
            self._y = (self._y +1) % 99
        else:
            self._y = (self._y -1) % 99
            
    def eat(self): # can you make it eat what is left?
        if self.store <100:
            if self.environment[self.y][self.x] > 10:
               self.environment[self.y][self.x] -= 10
               self.store += 10    
            elif self.environment[self.y][self.x] > 1:
                self.environment[self.y][self.x] -= 1
                self.store += 1 
        else:
            self.environment[self.y][self.x] += 97
            self.store -= 97
            
            
    def __str__ (self):
        return("Location is X: "+str(self.x)+ " Y: "+str(self.y)+ " and has "+str(self.store)+ " stored")
    
    def set_x (self, inx):
        self._x = self._x + inx
    
    def set_y (self, iny):
        self._y = self._y + iny
    
    def get_x (self):
        return(self._x)
    
    def get_y (self):
        return(self._y)
        
        