#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:05:44 2019

@author: 3700479
"""
from .ontest import DefenceStrategy, FonceStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS 

def get_team(nb_players):

    team = SoccerTeam( name = " baker's Team " )
    if nb_players == 1:
        team.add("defence1",DefenceStrategy())
    if nb_players == 2:
        team.add("defence1",DefenceStrategy())
        team.add("fonceur2",FonceStrategy())
    if nb_players == 3:
        team.add("defence1",DefenceStrategy())
        team.add("fonceur2",FonceStrategy())
        team.add("fonceur1",FonceStrategy())
    if nb_players == 4:
        team.add("defence1",DefenceStrategy())
        team.add("fonceur1",FonceStrategy())   
        team.add("defence2",DefenceStrategy())
        team.add("fonceur2",FonceStrategy())
    return team