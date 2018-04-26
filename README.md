# A simulation of Buffon's needle experiment to calculate $\pi$

If a needle with length *L* is randomly dropped on a grid of parallel lines with internal spacing *S*, where *S*>*L*, the probability *P* that the needle will cross a line is given by:

*P* = (2/$\pi$) \* (*L*/*S*)

as first posed in the 18th century by Georges-Louis Leclerc, Comte de Buffon ([see here](https://en.wikipedia.org/wiki/Buffon%27s_needle)). Therefore, $\pi$ can be approximated as:

$\pi$ = 2 \* (*L*/*S*) \* *N_total*/*N_crossings*

where *N_total* is the total number of needles, and *N_crossings* is the total number of needles that crossed a line.

## Analysis

These Python programs and Jupyter notebooks simulate Buffon's needle tossing experiment to calculate $\pi$, using [Matplotlib](https://matplotlib.org) and [PyROOT](https://root.cern.ch/pyroot), a Python extension module to the [ROOT](https://root.cern.ch) data analysis package. The Jupyter notebooks can be viewed online using [Jupyter nbviewer](https://nbviewer.jupyter.org) (which has improved display rendering capabilities compared to Github):

- [needlesim_Matplotlib.ipynb](https://nbviewer.jupyter.org/github/gmalim/buffon_pi_simulation/blob/master/needlesim_Matplotlib.ipynb)
- [needlesim_ROOT.ipynb](https://nbviewer.jupyter.org/github/gmalim/buffon_pi_simulation/blob/master/needlesim_ROOT.ipynb)

Not simulated but interesting: The formula is valid even if you bend the needle in any way you want (subject to the constraint that it must lie in a plane), i.e. Buffon's ~~needle~~ noodle experiment.
