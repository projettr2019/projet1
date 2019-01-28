#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:45:20 2019

@author: 3700479
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS
from tools import SuperState, Passe, But

 # id_team is 1 or 2
 # id_player starts at 0
        
class FonceStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonce")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
            #ne pas tirer n'importe quand
             if state.ball.position.distance(state.player_state(id_team,id_player).position) > PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),None)
             else:
                if id_team == 1: 
                    return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)/100)
                else: 
                    return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),(Vector2D(0,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)/100)
                
                
class FonceStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonce")

    def compute_strategy(self, state, id_team, id_player):
       
        #ne pas tirer n'importe quand
        s = SuperState(state,id_team,id_player)
        if state.ball.position.distance(state.player_state(id_team,id_player).position) > PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction((Vector2D(GAME_HEIGHT/2,GAME_WIDTH-100)-state.player_state(id_team,id_player).position),None)
        else:
            if id_team == 1: 
                return s.But
            else: 
                return s.But



        
        
class DefenceStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "defence")
        
    def compute_strategy(self, state, id_team, id_player):
      #  s = SuperState(state,id_team,id_player)
        if state.ball.position.distance(state.player_state(id_team,id_player).position) < 20: 
            if id_team == 1:
                return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)/10)
            else: 
                return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),(Vector2D(0,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position)/10)
        else:   
            if id_team ==1:
           #     if state.player_state(id_team,id_player).position != Vector2D(10,GAME_HEIGHT/2):
           #        return SoccerAction(None,None)
           #     else:       
                    return SoccerAction((Vector2D(5,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position),None)
            else:
                return SoccerAction((Vector2D(GAME_WIDTH-5,GAME_HEIGHT/2)-state.player_state(id_team,id_player).position),None)
    

    
    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("DefenceStrategy",FonceStrategy2())  # Random strategy
team1.add("DefenceStrategy", Passe())   # Static strategy
team2.add("DefenceStrategy",DefenceStrategy())
team2.add("passe",DefenceStrategy()) 
# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

# if (state.ball.position).distance(state.player_state(id_team,id_player)) < PLAYER_RADIUS + BALL_RADIUS:
#while (state.ball.position).distance(state.player_state(id_team,id_player)) > PLAYER_RADIUS + BALL_RADIUS: .