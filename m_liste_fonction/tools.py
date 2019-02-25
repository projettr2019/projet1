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

 #   def __getattr__(self,attr):
   #     return getattr(self.state,attr)  
    
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
    def mygoal(self):
        if self.id_team == 2:
             return Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
        else:
             return Vector2D(0,GAME_HEIGHT/2)
        
    
    @property
    def posdef(self):
        if self.id_team == 1:
            return Vector2D(12,GAME_HEIGHT/2)
        else:
            return Vector2D(GAME_WIDTH-12,GAME_HEIGHT/2)
        
    @property  
    def ball_dir(self):
        return (self.ball-self.player)
    
    @property  
    def goal_dir(self):
        return (self.goal-self.ball) #.normalize()
      
    @property 
    def posOpponent(self):
        posOpponent= []
        for id_team,id_player in self.state.players:
            if id_team != self.id_team:
                posOpponent.append(self.state.player_state(id_team,id_player).position)
        return posOpponent 
   
#servira probablement jamais     
    @property
    def disOpponent(self):
        distmin = 200
        for opp in self.posOpponent:
            res = self.state.players-opp
            if res < distmin :
                distmin = res
        return distmin
    
    @property
    def oppnear(self):             
        opponent = self.posOpponent
        return min([(self.player.distance(player),player)for player in opponent])[1]
    
    
    
    @property 
    def posFriend(self):
        posfriend= []
        for id_team,id_player in self.state.players:
            if id_team == self.id_team:
                posfriend.append(self.state.player_state(id_team,id_player).position)
        return posfriend 
    #il faut corriger ca marche pas ona enlever du ontest pour les match
    @property 
    def friendnear(self):             
        friend = self.posfriend
        return min([(self.player.distance(player),player)for player in friend])[1]
    
            
#vas vers la trajectoire de la balle      
    @property
    def trajballe(self): 
        return self.state.ball.position + 3*(self.state.ball.vitesse)



