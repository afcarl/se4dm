from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

## Table

Tables keep `Some` values for each column in a string.

"""
from walkcsv import *
from row import *
from cols import *

def tables(src):
  overall = all = header = None
  for cells in cols(src):
    if all is None:
      header = cells
      all     = DefaultDict(lambda: Table(header))
      overall = Table(header)
    else:
      klass      = cells[overall.dep.klass.pos]
      all[klass] + cells
      overall    + cells
  return all,overall
  
class Table:
  def __init__(i,header,what="_all_",rows=[],row=identity):
    i.header  = header
    i.what    = what
    i.row     = row
    i.dep     = o(less=[], more=[], klass=None)
    i.indep   = o(nums=[], syms=[])
    i.nums, i.syms, i.all = [],[],[]
    i.rows    = Some(keep = the.COL.rowsCache)
    for pos,name in enumerate(header):
      col(i,pos,name)
    map(i.__add__, rows)
  def clone(i,what=None,keep=None,rows=[]):
    return Table(i.header,
                 what=  what or i.what,
                 keep=  keep or i.rows.keep,
                 row = i.row,
                 rows=  rows)
  def __add__(i,cells):
    i.rows + i.row(cells)
    for col in i.all:
      col += cells[col.pos]
    return i
  
"""

## Helper: map column name to column types

"""

def col(t,pos,name):
  def klassp(x) : return the.CSV.klass in x
  def lessp( x) : return the.CSV.less  in x
  def morep( x) : return the.CSV.more  in x
  def intp(  x) : return the.CSV.int   in x
  def nump(  x) : return the.CSV.float in x or \
                         morep(x) or lessp(x) or intp(x) 
  #---  
  what   = Num if nump(name) else Sym
  z      = what()
  z.pos  = pos
  z.name = name
  also   = t.nums 
  if   morep(name) : t.dep.more += [z]
  elif lessp(name) : t.dep.less += [z]
  elif nump(name)  : t.indep.nums += [z]
  else:
    also = t.syms
  if klassp(name): t.dep.klass = z
  else           : t.indep.syms += [z]
  t.all += [z]
  also  += [z] 

