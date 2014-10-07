#regen pdf
inkscape handout-side2.svg --export-pdf handout-side2.pdf
#stick both together
pdftk A=handout-side1.pdf B=handout-side2.pdf cat A B1-end output handout.pdf
