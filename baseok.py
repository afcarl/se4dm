from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True
from base import *

@ok
def _o():
  x=o(name='tim',age=55)
  x['name'] = 'tom'
  assert x.name == 'tom'
  x.name = 'tony'
  assert x.name == 'tony'
  assert str(x) == "o{'age': 55, 'name': 'tony'}" 
  
@setting
def _s1(): return o(
    fname='tim',
    lname='menzies'
    )

@ok
def _set():
  assert 'tim' == the._s1.fname
  the._s1.fname = "tom"
  assert 'tom' == the._s1.fname
    
@ok
def _t0():
  "happy function. All asserts true"
  assert True
  
@ok
def _t1():
  "sadder function.. crashed halfway done"
  assert 1==1
  assert 2==1
  assert 3==1

@ok
def _t2():
  "still runs, even after _t1 crashes"
  assert 3==4

