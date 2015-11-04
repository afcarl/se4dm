from __future__ import print_function, division
import sys
sys.dont_write_bytecode = True

"""

## Table

Tables keep `Some` values for each column in a string.

"""
class Table:
  def __init__(i,header,what="_all_",rows=[]):
    i.header= header
    i.what  = what
    i.dep   = o(less=[], more=[], klass=None)
    i.indep = o(nums=[], syms=[])
    i.nums, i.syms, i.all = [],[],[]
    i.rows  = Some(keep = the.COLS.rowsCache)
    for pos,name in enumerate(header):
      col(t,pos,name)
    map(i.__iadd__, rows)
    i.there = There(i)
  def clone(i,what=None,keep=None,rows=[]):
    return Table(i.header,
                 what= what or i.what,
                 keep= keep or i.rows.keep,
                 rows= rows)
  def __iadd__(i,cells):
    i.rows.add(Row(cells))
    for col in i.all:
      col += cells[col.pos]
    return i
"""

## Helper: map column name to column types

"""
def col(t,pos,name):
  def klassp(i,x) : return "=" in x
  def lessp( i,x) : return "<" in x
  def morep( i,x) : return ">" in x
  def nump(  i,x) : return "$" in x or morep(x) or lessp(x)
  what   = Num if i.nump(name) else Sym
  z      = what()
  z.pos  = pos
  z.name = name
  also   = t.nums 
  if   t.morep(name) : t.dep.more += [z]
  elif t.lessp(name) : t.dep.less += [z]
  elif t.nump(name)  : t.indep.nums += [z]
  else:
    also = t.syms
    if t.klassp(name): t.dep.klass = z
    else             : t.indep.syms += [z]
  t.all += [z]
  also  += [z]

