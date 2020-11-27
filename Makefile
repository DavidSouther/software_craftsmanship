textbook_spine = 00_textbook.adoc
textbook_sources = \
	00_textbook_index.adoc \
	00_introduction/00_introduction.adoc \
	01_basic_types_and_control_flow/00_types_and_control_flow.adoc

all: html pdf

clean:
	rm -rf out/*

html: clean
	asciidoctor -D out/textbook $(textbook_spine)

pdf: clean
	asciidoctor-pdf \
	--out-file=out/textbook/software_craftsmanship.pdf \
	$(textbook_spine)
