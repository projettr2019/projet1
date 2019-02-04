#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:45:20 2019

@author: 3700479
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS
from tools import SuperState

 # id_team is 1 or 2
 # id_player starts at 0
        
class FonceStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonce")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
            #ne pas tirer n'importe quand
        s = SuperState(state,id_team,id_player)
        if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction((s.ball-s.player),None)
        else:
            if id_team == 1: 
                return SoccerAction((s.ball+ -s.player),(s.goal)-s.player)
            else: 
                return SoccerAction((s.ball-s.player),(s.goal)-s.player)
                
                

        
"""class Dribleur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "drible")
        
    def compute_strategy(self, state, id_team, id_player):
          s = SuperState(state,id_team,id_player)
          if s.posOpposant-s.player<40:
             return SoccerAction((Vector2D(0,0)-s.player),None)
          else:                 
             return SoccerAction((s.goal-s.player),None)
             
 """       
        
class DefenceStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "defence")
        
    def compute_strategy(self, state, id_team, id_player):
      s = SuperState(state,id_team,id_player)  
      if s.ball.distance(s.player) < 30: 
          if id_team == 1:
              return SoccerAction(((s.trajballe)-s.player),((s.goal)-s.player))
      else:   
          if id_team == 1:
              return SoccerAction((s.posdef-s.player),None)
          else:
              return SoccerAction((s.posdef-s.player),None)

class Passe(Strategy):   
    def __init__(self):
        Strategy.__init__(self, "passe")
         

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction((s.ball-s.player),None)
        
        else:
            if id_player!=0:
                return SoccerAction((s.ball-s.player),((state.player_state(id_team,id_player-1).position)-state.player_state(id_team,id_player).position))
            else:
                return SoccerAction((s.ball-s.player),((state.player_state(id_team,id_player+1).position)-state.player_state(id_team,id_player).position))




#a tester plus tard
class But():
    def __init__(self):
        Strategy.__init__(self, "but")
         

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if(state.ball.position.distance(s.goal)<40):
            if  state.ball.position.distance(state.player_state(id_team,id_player).position) > PLAYER_RADIUS + BALL_RADIUS:
                if id_team == 1:
                    return SoccerAction((s.ball-s.player),(s.goal-s.player)/10)
                else: 
                    return SoccerAction(((s.ball-state.player_state(id_team,id_player).position),(s.goal)-state.player_state(id_team,id_player).position)/10)
                
                
                
                
                

    
