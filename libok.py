from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from lib import *

@ok
def _rseed():
  rseed(1)
  one = list('abcdefghijklm')
  assert shuffle(one) == ['m', 'h', 'j', 'f', 'a',
           'g', 'l', 'd', 'e', 'c', 'i', 'k', 'b']

@ok
def _defDict():
  d = DefaultDict(lambda: [])
  for n,c in enumerate(list('tobeornottobe')):
    d[c].append(n)
  assert d ==  {'b': [2, 11], 'e': [3, 12],
                'o': [1, 4, 7, 10], 'n': [6],
                'r': [5], 't': [0, 8, 9]}
    
