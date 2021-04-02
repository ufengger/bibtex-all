#!/bin/sh
# convert English epub to txt with fixed line width.
ebook-convert $1 $2 --force-max-line-length --max-line-length 78
