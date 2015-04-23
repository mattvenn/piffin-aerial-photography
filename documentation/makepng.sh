#!/bin/bash
for svg in *svg; do
    base=$(basename $svg .svg)
    png=$base.png
    echo $svg
    convert -density 200 -resize 800 $svg $png
done
