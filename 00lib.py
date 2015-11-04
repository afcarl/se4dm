from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Lib

"""
import traceback
"""

## Unit tests

"""

def ok(*lst):
  print("### ",lst[0].__name__)
  for one in lst: unittest(one)
  return one

class unittest:
  tries = fails = 0  #  tracks the record so far
  @staticmethod
  def enough():
    print(unittest.score()); exit()
  @staticmethod
  def score():
    t = unittest.tries
    f = unittest.fails
    return "# TRIES= %s FAIL= %s %%PASS = %s%%"  % (
      t,f,int(round(t*100/(t+f+0.001))))
  def __init__(i,test):
    unittest.tries += 1
    try:
      test()
    except Exception,e:
      unittest.fails += 1
      i.report(test)
  def report(i,test):
    print(traceback.format_exc())
    print(unittest.score(),':',test.__name__)

"""

## Generic containers

Javascript-like

"""
class o:
  def __init__(i,**d)    : i.__dict__.update(d)
  def __setitem__(i,k,v) : i.__dict__[k] = v
  def __getitem__(i,k)   : return i.__dict__[k]
  def __repr__(i)        : return 'o'+str(i.__dict__)

