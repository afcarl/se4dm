from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from cols import *

@ok
def _some():
  rseed(1)
  s = Some(8)
  for _ in xrange(1000):
    for c in list('teafortwo'):
      s + c
  print(s.any)

print(22)
