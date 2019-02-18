#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:11:12 2019

@author: 3700479
"""


from m_liste_fonction.goalsearch import GoalSearch 
from m_liste_fonction.ontest import GoTestStrategy

expe = GoalSearch(strategy = GoTestStrategy(),params={'strength' : [0.1,6]})
expe.start()
print(expe.get_res())
print(expe.get_best())
