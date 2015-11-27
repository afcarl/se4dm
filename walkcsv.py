from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True


"""

# Walk

"""
import zipfile,re,sys
from lib import *

@setting
def CSV(): return o(
    whitespace = r"[\n\r\t ]*",
    comment    = r"#.*",
    delimiter  = ",",
    ignore     = "?",
    klass      = "=",
    less       = "<",
    more       = ">",
    float      = "$",
    int        = ":"
    )
"""

# Iterators for Walking CSV Data

Can handing raw strings, files, zip files.

Assumes if lines end in ',' then that line continues to the next.

Also assumes first line is column names.

## Handing Raw String, Files, Zip Files.

The function `FROM` returns iterators that can handle different kinds of data.


"""

def lines(f):
  def yieldLines(*lst):
    for line in f(*lst):
      yield line
  return yieldLines

@lines
def STRING(str):
  for line in str.splitlines():
    yield line

@lines
def ZIP(zip,file):
  with zipfile.ZipFile(zip, 'r') as z:
    with z.open(file) as f:
      for line in f:
        yield line

@lines        
def FILE(filename):
  with open(filename) as f:
    for line in f:
      yield line
"""

## Iterators

"""
def rows(src):
  """Yield all non-blank lines,joining lines that end in ','.
     Usually called as a sub-routine inside 'cols'.
  """
  b4 = ''
  for line in src:
    line = re.sub(the.CSV.whitespace,"",line)
    line = re.sub(the.CSV.comment,   "",line)
    if not line: continue # skip blanks
    if line[-1] == the.CSV.delimiter: # maybe, continue lines
      b4 += line
    else:
      yield b4 + line
      b4 = ''

def cols(src):
  """Coerce row values to floats, ints or strings.
     Jump over any cols we are ignoring."""
  want = None
  for row in rows(src):
    lst  = row.split(the.CSV.delimiter)
    if want:
      yield [make(lst[col],how) for col,_,how in want]
    else:
      want = [(col,name,maker(name))
               for col,name in enumerate(lst)
               if not the.CSV.ignore in name ]
      yield [name for col,name, how,in want] 

def make(str,how):
  return str if str==the.CSV.ignore else how(str)

def maker(x):
  if the.CSV.int in x:
    return int
  if the.CSV.less in x or the.CSV.more in x or the.CSV.float in x:
    return float
  return identity
