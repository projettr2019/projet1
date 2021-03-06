    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:45:20 2019

@author: 3700479
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS
from .tools import SuperState


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
            
            if id_team==1 : 
                if s.ball.x < GAME_WIDTH/2:
                    if s.player.distance(s.ball) < 15 :
                        if (s.player).distance(s.milieu) < 10 :   
                            return SoccerAction(s.trajballe- s.player,None)                      
                    else:
                        return SoccerAction(s.posatt - s.player,None) 
            else:
                 if s.ball.x > GAME_WIDTH/2:
                     if s.player.distance(s.ball) < 15 :
                        if (s.player).distance(s.milieu) < 10 :
                            return SoccerAction(s.trajballe - s.player,None)
                     else :
                        return SoccerAction(s.posatt - s.player,None) 
            return SoccerAction((s.ball-s.player),None)
        
        else:
            
            #    return SoccerAction(0,0)
            
         #   if s.oppnear.distance(s.player) < 25 :
          #      return SoccerAction((s.ball-s.player).normalize()*10,((s.player)-s.friendnear))
            if s.goal.distance(s.player)< 55 :
                return SoccerAction((s.trajballe-s.player),((s.goal)-s.player).normalize()*10)
            else:
                return SoccerAction((s.trajballe-s.player).normalize()*100,((s.goal)-s.player).normalize()*1.5)
                
              #
              #if s.oppnear< 15:
             #   return SoccerAction((s.ball-s.player).nVector2D(GAME_WIDTH-12,GAME_HEIGHT/2)ormalize()*10,((s.player)-s.goal))
             #  

        

class FonceStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonce")

    def compute_strategy(self, state, id_team, id_player):
        
        s = SuperState(state,id_team,id_player)
        # s'assure que le joueur n'est pas a distance de frappe de la balle
        if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS: 
            
            if id_team==1 : 
                if s.ball.x < GAME_WIDTH/2:  #ce bouge
                    if s.player.distance(s.ball) < 15 :
                        if (s.player).distance(s.milieu) < 10 :   
                            return SoccerAction(s.trajballe- s.player,None)                      
                    else:
                        return SoccerAction(s.posatt - s.player,None) 
            else: # id team 2:
                 if s.ball.x > GAME_WIDTH/2:
                     if s.player.distance(s.ball) < 15 :
                        if (s.player).distance(s.milieu) < 10 :
                            return SoccerAction(s.trajballe - s.player,None)
                     else :
                        return SoccerAction(s.posatt - s.player,None) 
            return SoccerAction((s.ball-s.player),None)
        
        else:
            if s.goal.distance(s.player)< 55 :
                return SoccerAction((s.trajballe-s.player),((s.goal)-s.player).normalize()*10)
            else:
                return SoccerAction((s.trajballe-s.player).normalize()*100,((s.goal)-s.player).normalize()*1.5)
                

        

class FonceStrategy3(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonce")

    def compute_strategy(self, state, id_team, id_player):
        
        s = SuperState(state,id_team,id_player)
        # s'assure que le joueur n'est pas a distance de frappe de la balle
        if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS: 
            
            if id_team==1 : 
                if s.ball.x < GAME_WIDTH/2:  #ce bouge
                    if s.player.distance(s.ball) < 15 :
                        if (s.player).distance(s.milieu) < 10 :   
                            return SoccerAction(s.trajballe- s.player,None)                      
                    else:
                        return SoccerAction(s.posatt3 - s.player,None) 
            else: # id team 2:
                 if s.ball.x > GAME_WIDTH/2:
                     if s.player.distance(s.ball) < 15 :
                        if (s.player).distance(s.milieu) < 10 :
                            return SoccerAction(s.trajballe - s.player,None)
                     else :
                        return SoccerAction(s.posatt3 - s.player,None) 
            return SoccerAction((s.ball-s.player),None)
        
        else:
            if s.goal.distance(s.player)< 55 :
                return SoccerAction((s.trajballe-s.player),((s.goal)-s.player).normalize()*10)
            else:
                return SoccerAction((s.trajballe-s.player).normalize()*100,((s.goal)-s.player).normalize()*1.5)
                



  
class DefenceStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "defence")
        
    def compute_strategy(self, state, id_team, id_player):
      s = SuperState(state,id_team,id_player) 
 
   #if s.player.x < GAME_WIDTH/2 :       
      if s.ball.distance(s.player) < 35: 
          if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS:
             # if s.player.x  < 50 :    
              return SoccerAction((s.trajballe-s.player),None)
          else:
              if s.goal.distance(s.player)< 55 :
                  return SoccerAction((s.trajballe-s.player),((s.goal)-s.player).normalize()*20)
              else:
                  if s.ball.y > GAME_WIDTH/2 :
                      return SoccerAction((s.trajballe-s.player),(s.top-s.player).normalize()*30)
                  else:
                      return SoccerAction((s.trajballe-s.player),(s.bottom-s.player).normalize()*30)
      else:   
          return SoccerAction((s.posdef6-s.player),None)
          

        

        
class DefenceStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "defence")
        
    def compute_strategy(self, state, id_team, id_player):
      s = SuperState(state,id_team,id_player)  
      if s.ball.distance(s.player) < 35: 
          if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS:
              return SoccerAction((s.trajballe-s.player),None)
          else:
              if s.goal.distance(s.player)< 55 :
                  return SoccerAction((s.trajballe-s.player),((s.goal)-s.player).normalize()*2)
              else:
                  if s.ball.y > GAME_WIDTH/2 :
                      return SoccerAction((s.trajballe-s.player),(s.goal-s.player).normalize()*30)
                  else:
                      return SoccerAction((s.trajballe-s.player),(s.goal-s.player).normalize()*30)
      else:   
          return SoccerAction((s.posdef5-s.player),None)        
        
        
        
        
        
        
        
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


class Move(object):
    def __init__(self,superstate):
        self.superstate = superstate
    def move(self,acceleration = None):
        return SoccerAction(acceleration = acceleration)
    def to_ball(self):
        return self.move(self.superstate.ball_dir)
    

class Shoot (object):
    def __init__(self,superstate):
        self.superstate = superstate
    def shoot(self,direction=None):
        dist = self.superstate.player.distance(self.superstate.ball)
        if dist < PLAYER_RADIUS + BALL_RADIUS :
            return SoccerAction(shoot=direction)
        else :
            return SoccerAction()
    def to_goal (self,strength=None):
            #print(self.superstate.goal_dir*strength)
            return self.shoot(self.superstate.goal_dir*strength)  


class GoTestStrategy(Strategy):
    def __init__(self, strength = 1):
        Strategy.__init__(self," Go-getter")
        self.strength = strength
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball() + shoot.to_goal(self.strength)
    
    
    
    
    
class Cage(Strategy):
    def __init__(self):
        Strategy.__init__(self, "defence")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if s.ball.distance(s.player) < 15:
            if s.ball.distance(s.player) > PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction((s.trajballe-s.player),(s.goal-s.player).normalize()*30)
        else:         
            if (id_player == 0):
                return SoccerAction((s.posdef1-s.player),None)
            if (id_player == 1):
                return SoccerAction((s.posdef2-s.player),None)
            if (id_player == 2):
                return SoccerAction((s.posdef3-s.player),None)
            if (id_player == 3):
                return SoccerAction((s.posdef4-s.player),None)
            
            #il faut s'assurer que seulement le jouer le plus pres de la balle tire