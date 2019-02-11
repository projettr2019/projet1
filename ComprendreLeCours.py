#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:40:28 2019

@author: 3700479
"""


from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS 

class Decorator :
    def __init__(self,state):
        self .state = state
    def __getattr__ ( self , attr ):
        return getattr(self.state,attr)
    
    
    
    
class Shoot ( Decorator ):
    def __init__ ( self , state ):
        Decorator.__init__(self,state)
    def shoot ( self , p ):
        return SoccerAction ( Vector2D (...))
    
    
    
    
class Passe ( Decorator ):
    def __init__ ( self , state ):    
        Decorator.__init__(self,state)
    def passe (self,p):
        return SoccerAction(Vector2D(...))
    
s = SuperState(state,id_team,id_player)
mystate=Shoot(Passe(state))