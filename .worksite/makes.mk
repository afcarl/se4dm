P=$(PWD)/.worksite

Pys=$(wildcard *.py)
Marks=$(wildcard *.md)

Pys2Html=$(Pys:.py=.html)
Mds2Html=$(Marks:.md=.html)

ifdef GATEWAY_INTERFACE
	python=$P/../env/bin/python
else
	python=$(shell which python)
endif

Py2md = $(python) $P/py2md
Page  = bash $P/page $P

md2html=$(python) -m markdown            \
         -x markdown.extensions.extra     \
         -x markdown.extensions.codehilite \
         -x markdown.extensions.toc

publish: htmls

htmls: $(Mds2Html) $(Pys2Html)

%.html : %.py
	@ cat $< | $(Py2md) | $(md2html) | $(Page) > $@;
	@ git add $@

%.html : %.md
	@ cat $<            | $(md2html) | $(Page) > $@;
	@ git add $@


typo: ready
	@- git status
	@- git commit -am "saving"
	@- git push origin master # <== update as needed

commit: ready
	@- git status
	@- git commit -a
	@- git push origin master

update: ready
	@- git pull origin master

status: ready
	@- git status

ready:
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'


