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

    @property
    def ball(self):
        return self.state.ball.position

    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
    
    @property
    def goal1(self):
        return self.Vector2D(0,GAME_HEIGHT/2)
    
    @property
    def goal2(self):
        return self.Vector2D(GAME_WIDTH,GAME_HEIGHT/2)



class Passe(Strategy):   
    def __init__(self):
        Strategy.__init__(self, "passe")
         

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if state.ball.position.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),None)
        
        else:
            if id_player!=0:
                return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),((state.player_state(id_team,id_player-1).position)-state.player_state(id_team,id_player).position))
            else:
                return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),((state.player_state(id_team,id_player+1).position)-state.player_state(id_team,id_player).position))


#a tester plus tard
class But():
    def __init__(self):
        Strategy.__init__(self, "but")
         

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if(state.ball.position.distance(s.goal2)<40):
            if  state.ball.position.distance(state.player_state(id_team,id_player).position) > PLAYER_RADIUS + BALL_RADIUS:
                if id_team == 1:
                    return SoccerAction((state.ball.position-s.player),(s.goal2-s.player)/10)
                else: 
                    return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),(Vector2D(0,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)/10)