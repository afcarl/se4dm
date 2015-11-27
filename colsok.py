from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from cols import *

@ok
def _some():
  reset()
  s = Some(8)
  for _ in xrange(1000):
    for c in list('teafortwo'):
      s + c
  print(s.any)

@ok
def _num():
  reset()
  n = Num()
  for _ in xrange(1000):
    n + r()
  assert (n.sd,n.mu) == (0.29235813539098815,
                         0.5069480985636412)
