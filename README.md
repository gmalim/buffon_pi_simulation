# A simulation of Buffon's needle experiment to calculate *Pi*

If a needle with length *L* is randomly dropped on a grid of parallel lines with internal spacing *S* where *S*>*L*, the probability that the needle will cross a line is given by:

*P* = (2\**L*)/(*S*\**Pi*)

as described [here](https://en.wikipedia.org/wiki/Buffon%27s_needle). Therefore, *Pi* can be approximated as:

*Pi* = (2\**L*)/(*S*\**N_crossings*/*N_total*)

where *N_total* is the total number of needle drops, and *N_crossings* is the total number of line crossings.

[This python program](https://github.com/gmalim/buffon_pi_simulation/blob/master/buffon_pi.py) simulates the needle tossing experiment to calculate *Pi* using the [ROOT](https://root.cern.ch/) data analysis package.
