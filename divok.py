from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from div import *

def showt(x):
  return " _" if x is None \
         else " (%5.4f .. %5.4f)*%d"  % \
              (x[0],x[-1],len(x))
  
@ok
def _div1():
  DIV(small=0.01,
      maxDepth=3)
  tprint(divide([round(r()**2,4) for
                 _ in xrange(300)]),
         show=showt)
 

@ok
def _div1():
  data =[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]
  tprint(divide(data),show=showt)


@ok
def _div1():
  data =[1,1,1,1,1,1,1,2,2,2,2,2,2,2,
         2,2,3,3,3,3,3,3,3,3,3,3],
  tprint(divide(data),show=showt)
