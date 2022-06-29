#!/bin/sh
cp $1 tmp.epub
ebook-convert tmp.epub tmp.pdf --output-profile=tablet
pdf-crop-margins -p 0 tmp.pdf -o $2
rm tmp.epub tmp.pdf
