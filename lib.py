from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Lib

"""
import random
from base import *
import  math 
"""

## Basic Utilities

"""
r      = random.random
rseed  = random.seed
gt     = lambda x,y: x > y
lt     = lambda x,y: x < y
log    = math.log
first  = lambda z:z[0]
second = lambda z:z[1]
last   = lambda z:z[-1]
isa    = isinstance
listp  = lambda x: isa(x,list)
tuplep = lambda x: isa(x,tuple)
boxp   = lambda x: listp(x) or tuplep(x)

def noop(*l,**d): return noop

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

  
"""
what the hell: how does kids end up being a Sym?
###  _div4
  5:  80 = 4444622432 : 1
kids [<lib.Tree instance at 0x108f1f878>, <lib.Tree instance at 0x108f1fcb0>]
  6:  |.. 44 = 4444620848 : 2
kids [<lib.Tree instance at 0x108f1f950>, <lib.Tree instance at 0x108f1f998>]
  7:  |.. |.. 31 = 4444621424 : 3
kids cols.Sym
/Users/timm/gits/txt/se4dm/lib.py: line 96, in tprint ==> for kid in t.kids: 'classobj' object is not iterable
"""
