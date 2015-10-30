Dirs = $(shell find . -type d | grep -v '^\.')
Here=$(PWD)/.worksite
P=$(Here)

Pys=$(wildcard *.py)
Marks=$(wildcard *.md)

Pys2Html=$(Pys:.py=.html)
Mds2Html=$(Marks:.md=.html)

all: 
	@$(foreach x,$(Dirs), \
		echo $x     ;  \
		cd   $x     ;   \
		$(MAKE) -f $P/makes.mk htmls; )

htmls: $(Mds2Html) $(Pys2Html)

%.html : %.py
	$(P)/header "$P" $< > $@
	cat $< | $P/py2md | $P/md2html >> $@
	$(P)/footer  >> $@	
	@ git add $@

%.html : %.md
	$(P)/header "$P" $< > $@
	@ cat $< |  $P/md2html >> $@
	$(P)/footer  >> $@	
	@ git add $@

