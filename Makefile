textbook_spine = 00_textbook.adoc

all: html pdf

clean:
	rm -rf out/*

html: clean
	asciidoctor -D out/textbook $(textbook_spine)

pdf: clean
	asciidoctor-pdf \
	--out-file=out/textbook/software_craftsmanship.pdf \
	$(textbook_spine)
