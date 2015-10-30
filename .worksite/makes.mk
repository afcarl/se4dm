Dirs = $(shell find . -type d | grep -v '^\.')
Here=$(PWD)/.worksite
P=$(Here)

Pys=$(wildcard *.py)
Marks=$(wildcard *.md)

Pys2Html=$(Pys:.py=.html)
Mds2Html=$(Marks:.md=.html)

ifdef GATEWAY_INTERFACE
	python=$(HERE)/../env/bin/python
else
	pythton=python
endif

md2html="$(python) -m markdown"

all: 
	@$(foreach x,$(Dirs), \
		echo $x     ;  \
		cd   $x     ;   \
		$(MAKE) -f $P/makes.mk htmls; )

htmls: $(Mds2Html) $(Pys2Html)

%.html : %.py
	cat $< | $P/py2md | $(md2html) | $P/page "$P"  >> $@
	@ git add $@

%.html : %.md
	@ cat $< |  $(md2html) | $/page "$P$"  >> $@
	@ git add $@

