all: html pdf

clean:
	rm -rf docs/*

html: clean
	asciidoctor \
	--out-file=docs/index.html \
	00_textbook.adoc

	asciidoctor \
	--out-file=docs/python.html \
	01_python.adoc

pdf: clean
	asciidoctor-pdf \
	--out-file=docs/textbook/software_craftsmanship.pdf \
	00_textbook.adoc

	asciidoctor-pdf \
	--out-file=docs/textbook/software_craftsmanship_python.pdf \
	01_python.adoc
