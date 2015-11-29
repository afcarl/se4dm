from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Cols

## Configuration

"""
from lib import *

@setting
def COL(): return o(
    cache     = 256,
    rowsCache = 100,
    dull  = [0.147, # small
             0.33,  # medium
             0.474  # large
            ][0],
    missing="?"
    )
"""

## Some

"""
class Some:
  "Keep some things."
  def __init__(i, keep=None):
    # note, usually 256 or 128 or 64 (if brave)
    i.keep = keep or the.COL.cache
    i.n, i.any  = 0,[]
  def __add__(i,x):
    i.n += 1
    now = len(i.any)
    if now < i.keep:       
      i.any += [x]
    elif r() <= now/i.n:
      i.any[ int(r() * now) ]= x
"""

## Log

Keeping information on columns containing numerics of symbols

"""      
class Log:
  def __init__(i,inits=[]):
    i.reset()
    i.n = 0 
    i.cache = Some()
    map(i.__add__,inits)
  def __add__(i,x):
    if x != the.COL.missing:
      i.n += 1
      i.cache + x
      i._add(x)

class Num(Log):
  def reset(i):
    i.hi = i.lo = None
    i.mu = i.sd = i.m2 = 0  
  def _add(i,z):
    i.lo  = min(z,i.lo)
    i.hi  = max(z,i.hi)
    delta = z - i.mu;
    i.mu += delta/i.n
    i.m2 += delta*(z - i.mu)
    if i.n > 1:
      i.sd = (i.m2/(i.n - 1))**0.5
  def norm(i,z):
    return (z - i.lo) / (i.hi - i.lo + 10e-32)
  
class Sym(Log):
  def reset(i):
    i.most, i.mode, i.all = 1,0,{}
  def _add(i,z):
    tmp = i.all[z] = i.all.get(z,0) + 1
    if tmp > i.most:
      i.most,i.mode = tmp,z
  def entropy(i,p=0):
    for k,v in i.all.items():
      p1 = v/i.n
      if p1 > 0:
        p += p1*log(p1,2)
    return abs(p)
