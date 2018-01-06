# A simulation of Buffon's needle experiment to calculate PI

Given a grid of parallel lines with internal spacing $S$, the probability that a needle with length L that is dropped on the grid will cross a line is given by [1]:

P = (2*L)/(S*PI)

Therefore, PI can be approximated as:

PI = (2*L)/(S*N_crossings/N_total)

This python program simulates the needle tosses using the ROOT package to get an approximation for PI.

[1]: https://en.wikipedia.org/wiki/Buffon%27s_needle
