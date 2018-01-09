#!/usr/bin/python -tt
"""
Simulate Buffon's needle experiment to calculate PI. 
"""

import random
import math
import ROOT
import time

def needlesim_ROOT():

    random.seed(42)
    
    print("-----------------------------------------------------------------------")
    print("  This is a simulation of Buffon's needle experiment to calculate PI:  ")
    print("-----------------------------------------------------------------------")
    
    # Get input form user:
    
    badinput = True
    
    while (badinput):
        n = int(raw_input('Enter number of simulated needles: '))
        if (n > 0):
            if (n > 1000000):
                print('Not enough needles! Try again...')
            else:
                badinput = False
        else:
            print('Unfortunately number is not a positive integer, try again...')
        
    badinput = True
    
    while (badinput):
        LSratio = float(raw_input('Enter needle length over grid spacing ratio [between 0 and 1]: '))
        if (0 < LSratio < 1):
            badinput = False
        else:
            print('Unfortunately needle length over grid spacing ratio is not between 0 and 1, try again...')

    start = time.time()

    # Create ROOT canvas:
            
    mycanvas = ROOT.TCanvas('mycanvas', "Simulation of Buffon's needle experiment", 0, 0, 500, 500)
    #mycanvas.SetGridx(0)
    #mycanvas.SetGridy(1)
    mycanvas.SetLeftMargin(0.15)
    mycanvas.SetRightMargin(0.15)
    mycanvas.SetTopMargin(0.2)
    mycanvas.SetBottomMargin(0.2)

    dummyhisto = ROOT.TH2D('dummyhisto', '', 100, -5, 5, 100, -5, 5)
    dummyhisto.SetStats(0)
    dummyhisto.Draw("AH")

    gridlines = [] # to save TLine objects, otherwise they are not drawn

    for i in range(-4, 5):
        gridline = ROOT.TLine(-5, i, 5, i)
        gridline.SetLineColor(1)
        gridline.Draw()
        gridlines.append(gridline)

    # Loop over needles:
        
    needles = [] # to save TLine objects, otherwise they are not drawn

    count = 0

    for i in range(n):

        # Create needle:
        
        x1    = 6*random.random()-3
        y1    = 6*random.random()-3
        angle = 2*math.pi*random.random()

        x2 = LSratio*math.cos(angle) + x1
        y2 = LSratio*math.sin(angle) + y1
        
        needle = ROOT.TLine(x1,y1,x2,y2)

        # Check if needle crossed a gridline:
        
        crossed = False
        for k in range(-3,4):
            if ((y2>k) and (y1<k)) or ((y2<k) and (y1>k)):
                crossed = True
                
        if crossed:
            count += 1
            needle.SetLineColor(2)
        else:
            needle.SetLineColor(4)

        needle.Draw()
        needles.append(needle)        

    # Calculate PI and error wrt real PI:

    if (count > 0):
        pi_approx = 2*LSratio*n/float(count)
    else:
        pi_approx = 0
    error = (pi_approx - math.pi)/math.pi * 100
    
    print('Needle length / Grid spacing (L/S)           = {}'.format(LSratio))
    print('Total # of needles (N_t)                     = {}'.format(n)) 
    print('Total # of needles that crossed a line (N_c) = {}'.format(count))
    print('')
    print('=> Pi_sim ~= 2*(L/S)*(N_t/N_c) = {}'.format(pi_approx))
    print('=> (Pi_sim - Pi) / Pi * 100 = {:.3f}%'.format(error))

    # Create text:
        
    text1 = ROOT.TText(-5.5, 7, "Simulation of Buffon's needle experiment:");
    text1.SetTextSize(0.03);
    text1.Draw();

    text2 = ROOT.TText(-5.5, 6, "Needle length / Grid spacing (L/S) = {}".format(LSratio));
    text2.SetTextSize(0.03);
    text2.Draw();
        
    text3 = ROOT.TText(-4.5, 4.32, "N_total = {}".format(n));
    text3.SetTextSize(0.03);
    text3.Draw();
        
    text4 = ROOT.TText(-4.5, -4.62, "N_crossings = {}".format(count));
    text4.SetTextSize(0.03);
    text4.SetTextColor(2);
    text4.Draw();
        
    text5 = ROOT.TText(-5.5, -6.25, "Pi ~= 2*(L/S)*(N_total/N_crossings) = {}*{}/{} = {:.6f}".format(2*LSratio,n,count,pi_approx));
    text5.SetTextSize(0.03);
    text5.Draw();

    text6 = ROOT.TText(-5.5, -7, "(Pi_sim - Pi) / Pi * 100 = {:.3f}%".format(error));
    text6.SetTextSize(0.03);
    text6.Draw();
    
    mycanvas.Update()

    end = time.time()
    print('time = {} ms'.format((end - start)*1000))

    ROOT.gApplication.Run()
        
    return 0
  
if __name__ == '__main__':
    needlesim_ROOT()
