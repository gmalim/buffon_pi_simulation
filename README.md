# A simulation of Buffon's needle experiment to calculate *Pi*

If a needle with length *L* is randomly dropped on a grid of parallel lines with internal spacing *S*, where *S*>*L*, the probability that the needle will cross a line is given by:

*P* = (2/*Pi*) \* (*L*/*S*)

as first posed in the 18th century by Georges-Louis Leclerc, Comte de Buffon ([see here](https://en.wikipedia.org/wiki/Buffon%27s_needle)). Therefore, *Pi* can be approximated as:

*Pi* = 2 \* (*L*/*S*) \* *N_total*/*N_crossings*

where *N_total* is the total number of needles, and *N_crossings* is the total number of needles that crossed a line.

These simple python programs simulates Buffon's needle tossing experiment to calculate *Pi*, using [Matplotlib](https://matplotlib.org) and [PyROOT](https://root.cern.ch/pyroot), a Python extension module to the ROOT data analysis package.

Not simulated here but still a fun fact: The formula is valid even if you bend the needle in any way you want (subject to the constraint that it must lie in a plane), turning Buffon's needle experiment into a noodle experiment.
