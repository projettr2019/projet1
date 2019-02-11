#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:15:01 2019
@author: 3700479
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS 

from ontest import DefenceStrategy, FonceStrategy
# =============================================================================
# from soccersimulator import SoccerTeam
# =============================================================================



def get_team(nb_players):

    team = SoccerTeam( name = " baker's Team " )
    if nb_players == 1:
        team.add("fonceur1",FonceStrategy())
    if nb_players == 2:
        team.add("defence1",DefenceStrategy())
        team.add("fonceur2",FonceStrategy())
    return team
    
if __name__ == " __main__ ":
# from soccersimulator import Simulation, show_simu
# Check teams with 1 player and 2 players
    team1 = get_team(2)
    team2 = get_team(2)
# Create a match
    simu = Simulation( team1 , team2 )
# Simulate and display the match
    show_simu(simu)
        
        
        
        