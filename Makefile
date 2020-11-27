all: html pdf

clean:
	rm -rf out/*

html: clean
	asciidoctor \
	--out-file=out/index.html \
	00_textbook.adoc

	asciidoctor \
	--out-file=out/python.html \
	01_python.adoc

pdf: clean
	asciidoctor-pdf \
	--out-file=out/textbook/software_craftsmanship.pdf \
	00_textbook.adoc

	asciidoctor-pdf \
	--out-file=out/textbook/software_craftsmanship_python.pdf \
	01_python.adoc
