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

@setting
def SYS(): return o(
    seed=1
    )

def reset(seed = None):
  setting.reset()
  rseed(seed or the.SYS.seed)
  
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

class Tree:
  "k=key, v=value, kids=subs"
  def __init__(i,k=None,v=None):
    i.k, i.v = k,v
    i.kids=[]
  def left() : return i.kids[0]
  def right(): return i.kids[1]
  def leaves(i):
    if i.kids:
      for kid in i.kids:
        yield kid.leaves()
    else:
      yield i

def tprint(t, show=identity, depth=0, pad="|.. ",lvl=0):
  print(pad*lvl + str(t.k), end="")
  print(show(t.v),":", depth+1)
  for kid in t.kids: 
    tprint(kid, show, depth+1, pad, lvl+1)
  
