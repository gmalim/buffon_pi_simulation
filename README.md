# A simulation of Buffon's needle experiment to calculate *pi*

If a needle with length *L* is randomly dropped on a grid of parallel lines with internal spacing *S*, where *S*>*L*, the probability *P* that the needle will cross a line is given by:

*P* = (2/*pi*) \* (*L*/*S*)

as [first posed](https://en.wikipedia.org/wiki/Buffon%27s_needle) in the 18th century by Georges-Louis Leclerc, Comte de Buffon. Therefore, *pi* can be approximated by dropping lots of needles on a grid of lines and calculating:

*pi* = 2 \* (*L*/*S*) \* (*N_total*/*N_crossings*)

where *N_total* is the total number of needles, and *N_crossings* is the total number of needles that crossed a line.

## Analysis

This repository contains some simple test code to simulate Buffon's needle tossing experiment and calculate *pi*, using [Matplotlib](https://matplotlib.org) and [PyROOT](https://root.cern.ch/pyroot), a Python extension module to the [ROOT](https://root.cern.ch) data analysis package.

(Not simulated but interesting: The formula is valid even if you bend the needle any way you want, subject to the constraint that it must lie in a plane ==> Buffon's ~~needle~~ noodle experiment).
