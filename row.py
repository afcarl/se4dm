from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Rows

"""
from lib import *

class Row:
  n = -1
  def __init__(i,t):
    Row.n = i.n = Row.n + 1
    i.t, i.dists = t,{}
  def dist(j,k):
    if j.n == k.n : return 0
    if j.n > k.n  : return k.dist(j)
    key = (j.n, k.n)
    if not key in j.dists :
      j.dists[key] = dist(i.t,j,k)
    return j.dists[key]
  def furthest(j,lst=None,best=-1,better=gt):
    lst = lst or t.rows
    out = j
    for k in lst:
      tmp = dist(i.t,j,k)
      if tmp and better(tmp,best):
        out,best = k,tmp
    return best
  def closest(j,lst=None):
    return j.furthest(lst,best=1e32,better=lt)
  def knn(i,k=1,lst=None):
    lst = lst or t.rows
    out = {}
    for r1 in lst:
      for r2 in lst:
        all = [(dist(i.t,r1,r2),r2) for r2 in lst]
      out[r1] = sorted(all)[:k]
    return out

def dist(t,j,k):
  def colxy(cols,xs,ys):
    for col in cols:
      x = xs[col.pos]
      y = ys[col.pos]
      if x == "?" and y=="?": continue
      yield col,x,y
  def far(col,x,y):
    y = col.norm(y)
    x = 0 if y > 0.5 else 1
    return x,y
  #---------
  n = all = 0
  for col in colsxy(t.indep.syms,j,k):
    if x== "?" or y == "?":
      n   += 1
      all += 1
    else:
      inc = 0 if x == y else 1
      n   += 1
      all += inc
  for col,x,y in colxy(t.indep.nums,j,k):
    if   x == "?" : x,y = far(col,x,y)
    elif y == "?" : y,x = far(col,y,x)
    else          : x,y = col.norm(x), col.norm(y)
    n   += 1
    all += (x-y)**2
  return all**0.5 / n**0.5   
