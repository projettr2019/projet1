#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:20:21 2019

@author: 3700479
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS 
from m_liste_fonction.tools import SuperState
from m_liste_fonction import DefenceStrategy, FonceStrategy
from m_liste_fonction.goalsearch import GoalSearch

# Create teams

team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("FonceStrategy",FonceStrategy())  # Random strategy
# =============================================================================
#team1.add("DefenceStrategy", DefenceStrategy())   # Static strategy
# =============================================================================
team2.add("DefenceStrategy",DefenceStrategy())
#team2.add("FonceStrategy",FonceStrategy())
# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

# if (state.ball.position).distance(state.player_state(id_team,id_player)) < PLAYER_RADIUS + BALL_RADIUS:
#while (state.ball.position).distance(state.player_state(id_team,id_player)) > PLAYER_RADIUS + BALL_RADIUS:  

