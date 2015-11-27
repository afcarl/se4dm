from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

# Base Level Tools

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
    print(unittest.score())
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
      i.report(test,e)
  def report(i,test,e):
    _, _, tb = sys.exc_info()
    f, line, fun, what = traceback.extract_tb(tb)[-1]
    print('{}: line {}, in {} ==> {} {}'.format(
        f, line, fun, what,e))
"""

## Generic containers

Javascript-like

"""
class o:
  def __init__(i,**d)   : i.add(**d)
  def __setitem__(i,k,v): i.__dict__[k] = v
  def __getitem__(i,k)  : return i.__dict__[k]
  def __repr__(i)       : return 'o'+str(i.__dict__)
  def add(i,**d)        : return i.__dict__.update(d)
  def items(i)          : return i.__dict__.items()
"""

## Simple settings thing

Four uses cases:

+ Let settings be defined all over the code.
+ Store all settings in a central place so we can:
  + Avoid having to pass around options 
      + Access the current settings via a simple global.
      + Print all the current settings;
+ Update parts of some setting
+ Reset settings to defaults.

"""
class setting:
  funs = o()
  all  = o()
  def __init__(i,f):
    what = f.__name__   
    def g(**d):
      tmp = f()
      tmp.add(**d)
      setting.all[what] = tmp
      return tmp
    setting.funs[what] = g
    setting.all[what]  = g()
  @staticmethod
  def reset():
    for k,v in setting.funs.items():
      setting.all[k] = v() 

the=setting.all
