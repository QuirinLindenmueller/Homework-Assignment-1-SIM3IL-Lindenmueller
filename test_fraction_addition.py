# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:37:43 2020

@author: Quirin
"""

from fraction_addition import ggt
from fraction_addition import add_frac

def test_ggt():
    assert ggt(10,5) == 5
    
def test_add_frac():
    assert add_frac(3,4,6,8) == "Der Ergebnis-Bruch ist:  3 / 2"