#!/bin/sh

make

git reset # unstage files
git add -f out 
git commit -m "Release for gh-pages at $(date --rfc-3339=seconds)"