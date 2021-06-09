#!/bin/sh
# convert Chinese epub to txt with fixed line width
ebook-convert $1 $2 --force-max-line-length --max-line-length 38 --remove-paragraph-spacing
