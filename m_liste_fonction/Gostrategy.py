#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:15:01 2019
@author: 3700479
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS 
from tools import SuperState
from ontest import DefenceStrategy, FonceStrategy, Move, Shoot

# =============================================================================
# from soccersimulator import SoccerTeam
# =============================================================================
class GoStrategy ( Strategy ):
    def __init__( self ):
        Strategy.__init__(self," Go - getter ")
    def compute_strategy (self,state,id_team,id_player):
        s = SuperState(state,id_team,id_player)
        move=Move(s)
        shoot=Shoot(s)
        return move.to_ball()+shoot.to_goal()
