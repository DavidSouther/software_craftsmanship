#!/bin/sh

TITLE="[a-zA-Z0-9: ()\-\.]*"

sed \
	-e "s:^.subsection{\($TITLE\)}:### \1:g" \
	-e "s:^.section{\($TITLE\)}:## \1:g" \
	-e "s:^.chapter{\($TITLE\)}:# \1:g" \
	-e 's:``:":g' \
	-e 's:---: - :g' \
	-e 's/ \$\([^$]*\)\$/ `\1`/g' \
	-e 's:\\\$:$:g' \
	-e 's:{\\it \([^}]*\)}:*\1*:g' \
	-e 's:\\begin{lstlisting}:```:g' \
	-e 's:\\end{lstlisting}:```:g' \
	</dev/stdin