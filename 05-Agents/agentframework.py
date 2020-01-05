# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:19:06 2019

@author: Chris M
"""
import random

class Agent():
    
    _x = 0
    _y = 0
    
    def __init__ (self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

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
            
    def set_x (inx):
        self._x = self._x + inx
    
    def set_y (iny):
        self._y = self._y + iny
    
    def get_x ():
        return(self._x)
    
    def get_y ():
        return(self._y)
        
        