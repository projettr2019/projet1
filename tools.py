#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:13:14 2019

@author: 3700479

"""
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

class SuperState(object):
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player

    def __getattr__(self,attr):
        return getattr(self.state,attr)  
    
    @property
    def ball(self):
        return self.state.ball.position

    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
    
    @property
    def goal(self):
        if self.id_team == 2:
            return Vector2D(0,GAME_HEIGHT/2)
        else:
            return Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
        
    @property
    def posdef(self):
        if self.id_team == 1:
            return Vector2D(5,GAME_HEIGHT/2)
        else:
            return Vector2D(GAME_WIDTH-5,GAME_HEIGHT/2)
        
    
      
    @property 
    def posOpponent(self):
        posOpponent= []
        for it,ip in self.state.player:
            if it!=self.id_team:
                posOpponent.append(self.state.player_state(it,ip).position)
                
        return posOpponent 
        
    @property
    def trajballe(self): 
        return self.state.ball.position + 5*(self.state.ball.vitesse)


