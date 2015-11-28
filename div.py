from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from table import *

@setting
def DIV(): return o(
    small=0.01,
    tiny = 2,
    maxDepth=3
    )

def divide(lst, tiny=None,
           small=None, max=None,
           get=lambda z:z):
  if small is None: small = the.DIV.small
  if tiny  is None: tiny  = the.DIV.tiny
  if max   is None: max   = the.DIV.maxDepth
  class Counts(): 
    def __init__(i,inits=[]):
      i.n, i.sum = 0,0
      map(i.__add__,inits)
    def __add__(i,num):
      i.n   += 1
      i.sum += num
    def __sub__(i,num):
      i.n   -= 1
      i.sum -= num
    def mu(i):
      return i.sum/i.n
  #----------------------------------------------
  def splitter(this): # Find best divide of 'this' lst.
    l, r      = Counts(), Counts(get(x) for x in this)
    n0, mu0   = r.n, r.mu()
    cut, most = None, -1 
    for j,x  in enumerate(this):
      print("x",x)
      if l.n > tiny and r.n > tiny:
        if l.mu() * (1 + small) <  r.mu(): 
          maybe = l.n/n0 * (mu0 - l.mu())**2 + \
                  r.n/n0 * (mu0 - r.mu())**2
          if maybe > most :
            cut,most = j,maybe
      r - get(x)
      l + get(x)    
    return cut
  #----------------------------------------------
  def recurse(this, max, cut=None):
    cut = splitter(this)
    here = cut or 0
    t = Tree(get(this[here]), this)
    if max >= 0 and cut:
      left   = this[:cut]
      right  = this[cut:]
      t.kids = [recurse(left ,max - 1)
               ,recurse(right,max - 1)
               ]
    return t
  #---| main |-----------------------------------
  return recurse(sorted(lst,key=get),max-2)
