#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:39:37 2019

@author: 3700479
"""

from m_liste_fonction.gene import GeneSearch 
from m_liste_fonction.ontest import GoTestStrategy
from m_liste_fonction.tools import SuperState

expe = GeneSearch(strategy = GoTestStrategy(),params={'strength' : [0.1,6]})
expe.start()
print(expe.get_res())
print(expe.get_best())
