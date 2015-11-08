from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

import  lib
"""

# Walk

"""

import zipfile,re,sys

"""

# Iterators for Walking CSV Data

Can handing raw strings, files, zip files.

Assumes if lines end in ',' then that line continues to the next.

Also assumes first line is column names.

## Handing Raw String, Files, Zip Files.

The function `FROM` returns iterators that can handle different kinds of data.

"""
def lines(x):
  "Yields one line at a time."
  def strings(str):
    tmp=""
    for ch in str:
      if ch == "\n":
        yield tmp
        tmp = ''
      else:
        tmp += ch
    if tmp:
      yield tmp
  def zips((zipfile,file)):
    with zipfile.ZipFile(zipfile,'r') as z:
      with z.open(file) as f:
        for line in f:
          yield line
  def files(filename):
    with open(filename) as f:
      for line in f:
        yield line.replace("\n", "")
  # ---------------------------------
  if   isinstance(x,tuple) : f=zips
  elif x[-4:]==".csv"      : f=files
  else                     : f=strings
  for line in f(x):
    yield line
"""

## Iterators

"""
def rows(src):
  "Yield all non-blank lines,joining lines that end in ','."
  b4 = ''
  for line in src:
    line = re.sub(r"[\r\t ]*","",line)
    line = re.sub(r"#.*","",line)
    if not line: continue # skip blanks
    if line[-1] == ',':   # maybe, continue lines
      b4 += line
    else:
      yield b4 + line
      b4 = ''

def cols(src):
  """Coerce row values to floats, ints or strings.
     Jump over any cols we are ignoring."""
  def compile(x):
    if "<" in x or ">" in x or "$" in x:
      return float
    return identity
  want = None
  n=-1
  for row in rows(src):
    n += 1
    lst  = row.split(',')
    if want:
      yield n,[ comp(lst[col]) for col,comp in want ]
    else:
      want = [(col,complier(name))
               for col,name in enumerate(lst)
               if name[0] != "?" ]
      yield n,[name for name in list if name[0] != "?"] 
      
