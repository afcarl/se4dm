from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

from walkcsv import *

weather="""
outlook,
:temperature,
$humidity,?windy,play
sunny    , 85, 85, FALSE, no  # an interesting case
sunny    , 80, 90, TRUE , no
overcast , 83, ?, FALSE, yes
rainy    , 70, 96, FALSE, yes
rainy    , 68, 80, FALSE, yes
rainy    , 65, 70, TRUE , no
overcast , 64, 65, TRUE , 
yes
sunny    , 72, 95, FALSE, no

sunny    , 69, 70, FALSE, yes
rainy    , 75, 80, FALSE, yes
sunny    , 75, 70, TRUE , yes
overcast , 72, 90, TRUE , yes
overcast , 81, 75, FALSE, yes
rainy    , 71, 91, TRUE , no
"""

def _walk(src):
  for x in cols(src):
    print(x)
    
@ok
def _walkString():
  _walk( STRING(weather) )

@ok
def _walkFile(): 
  _walk( FILE('data/weather.csv') )

#@ok 
def _walkZip():
  _walk( ZIP('data/data.zip',
                   'weather.csv')  )

_walkZip()

