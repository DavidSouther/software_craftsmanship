#!/bin/bash

shopt -s extglob 

rm -r -- !(out|release.sh|serve.sh)
mv out/* .
rm -r out

git add .
git commit -m "Release for gh-pages at $(date --rfc-3339=seconds)"