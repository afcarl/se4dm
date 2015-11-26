from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Lib

"""
import random
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

def identity(x): return x

class DefaultDict(dict):
    """Dictionary with a default value for unknown keys."""
    def __init__(i, default):
        i.default = default
    def __getitem__(i, key):
        if key in i: return i.get(key)
        return i.setdefault(key, i.default())
