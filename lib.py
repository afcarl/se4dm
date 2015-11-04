from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Lib

"""
from base import *
"""

## Basic Utilities

"""
r     = random.random
rseed = random.seed
gt    = lambda x,y: x > y
lt    = lambda x,y: x < y

def shuffle(lst):
  random.shuffle(lst)
  return lst
