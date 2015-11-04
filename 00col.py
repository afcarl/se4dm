from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

import 
"""

# Columns

"""

def setting(f):
  what = f.__name_
  def g(**d):
    tmp = f()
    tmp.update(d)
    the[what] = tmp
    return tmp
  return g
    
  

