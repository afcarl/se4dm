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

<<<<<<< HEAD
=======
class Tree:
  id = -1
  "k=key, v=value, kids=subs"
  def __init__(i, k=None, v=None,
               kids=None, meta=None):
    i.k, i.v, i.kids = k,v,kids or []
    i.meta = meta() if meta else None 
    Tree.id = i.id = Tree.id + 1
  def copyNode(i):
    return Tree(i.k,i.v,[],
                i.meta.__class__ if i.meta else None)
  def left() : return i.kids[0]
  def right(): return i.kids[1]
  def nodes(i):
    yield i
    for kid in i.kids:
        for node in kid.nodes():
          yield node
  def branches(i,parents=[]):
    if i.kids:
      for kid in i.kids:
        for what in kid.branches(parents+[i]):
          yield what
    else:
      yield i,parents
  def prune(i,worth=None,n=None,better=lt,
            ok2split=lambda x,y:True):
    t = i.copyNode()
    here  = worth(i)
    below = 0
    for k in i.kids:
      below += n(k) / n(i) * worth(k)
    if better(below, here):
      if ok2split(i.left(),i.right()):
        t.kids = [k.prune(worth,n,better)
                  for k in i.kids]
    return t
        
def tprint(t, key=lambda z : z.k,
              val=lambda z : z.v,
              depth=0,
              pad="|.. ",
              lvl=0):
  print('%3s: '% t.id,pad*lvl + str(key(t)),end="")
  print(' =',id(val(t)),":", depth+1)
  print("kids",t.kids)
  if t.kids:
    for kid in t.kids: 
      tprint(kid, key, val, depth+1, pad, lvl+1)
>>>>>>> d554c51f8f45b8c24a5a4a4e5543ca9c0992f8e4
  
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
