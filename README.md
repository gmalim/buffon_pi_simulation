# A simulation of Buffon's needle experiment to calculate *Pi*

If a needle with length *L* is randomly dropped on a grid of parallel lines with internal spacing *S*, where *S*>*L*, the probability that the needle will cross a line is given by:

*P* = (2\**L*)/(*S*\**Pi*)

as first posed in the 18th century by Georges-Louis Leclerc, Comte de Buffon [see here](https://en.wikipedia.org/wiki/Buffon%27s_needle). Therefore, *Pi* can be approximated as:

*Pi* = (2\**L*\**N_total*)/(*S*\**N_crossings*)

where *N_total* is the total number of needle drops, and *N_crossings* is the total number of line crossings.

This program simulates Buffon's needle tossing experiment to calculate *Pi* using [PyROOT](https://root.cern.ch/pyroot), a Python extension module to the [ROOT](https://root.cern.ch) data analysis package.
