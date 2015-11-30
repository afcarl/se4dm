from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from div import *

def vprint(t):
  s1 =  str((t.v[0],t.v[-1])) 
  if t.kept == noop:
    return s1
  else:
    return '%s #%s' % (s1, t.kept.n)
  
#@ok
def _div1():
  DIV(small=0.01,
      maxDepth=3)
  tprint(divide([round(r()**0.5,4) for
                 _ in xrange(3000)],keeper=Num),
         val=vprint)


#@ok
def _div2():
  data =[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]
  tprint(divide(data))

#@ok
def _div3():
  data =[1,1,1,1,1,1,1,2,2,2,2,2,2,2,
         2,2,3,3,3,3,3,3,3,3,3,3]
  tprint(divide(data))

@ok
def _div4():
  data =[(22,0),(22,0),(22,0),(22,0),
         (31,0),(31,0),(31,0),(31,1),
         (44,2),(45,2),(46,2),(47,2),
         (80,3),(81,3),(81,3),(83,3),
         (90,3),(90,3),(90,3)]
  t=divide(data,get=first,keeper=Num)
  tprint(t)
  t = t.prune(worth=lambda z:z.kept.sd,
              n    =lambda z:z.kept.n)
  tprint(t)

#@ok
def _div5():
  data =[22,22,22,22,22,22,22,22,22]
  tprint(divide(data))


    
