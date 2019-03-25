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
        
   #pour posdef :y=ax+b (a=diffy/diffx, b = ycages- a*xcage) 
    @property
    def posdef(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(20, (self.ball.y+(GAME_HEIGHT/2))/2)

        else:
            return Vector2D(GAME_WIDTH-20, (self.ball.y+(GAME_HEIGHT/2))/2)
        
        
        
    @property
    def posdef5(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(15, ((self.ball.y+(GAME_HEIGHT/2))/2 ))

        else:
            return Vector2D(GAME_WIDTH-15, (self.ball.y+(GAME_HEIGHT/2))/2 )
        
        
        
    @property
    def posdef6(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(30, ((self.ball.y+(GAME_HEIGHT/2))/2))

        else:
            return Vector2D(GAME_WIDTH-30, ((self.ball.y+(GAME_HEIGHT/2))/2))
        
        
    @property
    def top(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(GAME_WIDTH/2, GAME_HEIGHT)

        else:
            return Vector2D(GAME_WIDTH/2, GAME_HEIGHT)
        
        
        
    @property
    def bottom(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(GAME_WIDTH/2, 0)

        else:
            return Vector2D(GAME_WIDTH/2, 0)
        
        
        
#-----------------------------------------------------------------------------------------------------
            
        
    @property
    def posdef1(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(7, ((GAME_HEIGHT/2)-2))

        else:
            return Vector2D(GAME_WIDTH-7, (GAME_HEIGHT/2)-2)
           
    @property
    def posdef2(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(7, (GAME_HEIGHT/2 -1))

        else:
            return Vector2D(GAME_WIDTH-7,(GAME_HEIGHT/2)-1)
           
    @property
    def posdef3(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(7, (GAME_HEIGHT/2 )+1)

        else:
            return Vector2D(GAME_WIDTH-7,(GAME_HEIGHT/2)+1)
           
    @property
    def posdef4(self):
        if self.id_team == 1:
           #if self.state.goal.distance(self.state.player) > GAME_WIDTH/2 :          
            return Vector2D(7, (GAME_HEIGHT/2)+2)

        else:
            return Vector2D(GAME_WIDTH-7,(GAME_HEIGHT/2)+2)
           

           
 #-------------------------------------------------------------------------------------------------------
        
        
#  posatt ---------------------------------------------------------------------------------------    
    @property
    def posatt(self):      
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH/2 + 1, (self.ball.y))
        else:
            return Vector2D(GAME_WIDTH/2 -1, (self.ball.y))
        
        
        
    @property
    def posatt2(self):      
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH/2 + 1, (self.ball.y))
        else:
            return Vector2D(GAME_WIDTH/2 -1, (self.ball.y))
        
        
    @property
    def posatt3(self):      
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH/2 + 1, (self.ball.y) +5)
        else:
            return Vector2D(GAME_WIDTH/2 -1, (self.ball.y )+5)
           
#----------------------------------------------------------------------------------------------        
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
        return self.state.ball.position +0.28*((self.state.ball.position).distance(self.state.player_state(self.id_team,self.id_player).position))*(self.state.ball.vitesse)  #distance*x (a la place de 3)

#pour posdef :y=ax+b (a=diffy/diffx, b = ycages- a*xcage)

    @property
    def milieu(self):
        return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)
#-------------------------------------------------------------------------------------------------------------------------------------------
 