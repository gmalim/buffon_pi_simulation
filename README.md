# A simulation of Buffon's needle experiment to calculate *Pi*

If a needle with length *L* is randomly dropped on a grid of parallel lines with internal spacing *S*, where *S*>*L*, the probability that the needle will cross a line is given by:

*P* = (2/*Pi*) \* (*L*/*S*)

as first posed in the 18th century by Georges-Louis Leclerc, Comte de Buffon ([see here](https://en.wikipedia.org/wiki/Buffon%27s_needle)). Therefore, *Pi* can be approximated as:

*Pi* = 2 \* (*L*/*S*) \* *N_total*/*N_crossings*

where *N_total* is the total number of needles, and *N_crossings* is the total number of needles that crossed a line.

This simple python program simulates Buffon's needle tossing experiment to calculate *Pi* using [PyROOT](https://root.cern.ch/pyroot), a Python extension module to the ROOT data analysis package.

Fun fact: The formula is valid even if you bend the needle in any way you want (subject to the constraint that it must lie in a plane), i.e. Buffon's "noodle" experiment.
