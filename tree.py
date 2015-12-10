from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from lib import *

class Tree:
  id = -1
  "k=key, v=value, kids=subs"
  def __init__(i, k=None, v=None,
               kids=None, keeper=noop):
    i.k,i.kids,i.kept = k, kids or [],keeper()
    Tree.id = i.id = Tree.id + 1
    i.keep(v)
  def copyNode(i):
    return Tree(k=i.k, v=i.v,kids=[],
                keeper=i.kept.__class__)
  def keep(i,v):
    i.v = v
    i.kept(v)
  def left(i) : return i.kids[0]
  def right(i): return i.kids[1]
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
    if i.kids:
      below = sum(map(lambda j: n(j) / n(i) * worth(j),
                    i.kids))
      if better(below, here):
        if ok2split(i.left(),i.right()):
          t.kids= map(lambda k: k.prune(worth,n,better),
                      i.kids)
    return t
        
def tprint(t, key=lambda z : z.k,
              val=lambda z : z.v,
              depth=0,
              pad="|.. ",
              lvl=0):
  print('%3s: '% t.id,pad*lvl + str(key(t)),end="")
  print(' =',val(t),"::", depth+1)
  if t.kids:
    for kid in t.kids: 
      tprint(kid, key, val, depth+1, pad, lvl+1)
      
