#!/usr/bin/python -tt
"""
Simulate Buffon's needle experiment to calculate PI. 
"""

import random
import math
import ROOT

def main():

	n = int(raw_input('Enter number of simulated needles: '))
	L = float(raw_input('Enter needle length [between 0 and 1]: '))

	lines = []

	c1 = ROOT.TCanvas('c1', 'Needle drop simulation', 0, 0, 500, 500)
	c1.SetGridx(0)
	c1.SetGridy(1)

	dummyhisto = ROOT.TH2D('dummyhisto','',100,-4.5,4.5,100,-4.5,4.5)
	dummyhisto.SetStats(0)
	dummyhisto.Draw()
	dummyhisto.GetXaxis().SetTitle('x')
	dummyhisto.GetYaxis().SetTitle('y')

	count = 0
	
	for i in range(0,n):

		x1    = 6*random.random()-3
		y1    = 6*random.random()-3
		angle = 2*math.pi*random.random()

		x2 = L*math.cos(angle) + x1
		y2 = L*math.sin(angle) + y1

		line = ROOT.TLine(x1,y1,x2,y2)
		line.Draw()
		lines.append(line) # to save line objects, otherwise they are not drawn

		crossed = False
		for k in range(-3,4):
			if ((y2>k) and (y1<k)) or ((y2<k) and (y1>k)):
				crossed = True

		if crossed:
			count += 1
				
	c1.Update()

	print 'Total number of needles (N) = {}'.format(n) 
	print 'Total number of needles crossing lines (C) = {}'.format(count)
	print 'Needle length (L) = {}'.format(L)
	print 'Spacing between grid lines (S) = 1'
	print '=> (2*L*N)/(S*C) = {}'.format(2*L*n/float(count))

	error = (math.pi-2*L*n/float(count))/math.pi*100
	
	print '(PI = {} => Error = {:.3f}%)'.format(math.pi, error)
	
	ROOT.gApplication.Run()
	
	return 0
  
if __name__ == '__main__':
	main()
