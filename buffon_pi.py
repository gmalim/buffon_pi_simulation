#!/usr/bin/python -tt
"""
Simulate Buffon's needle experiment to calculate PI. 
"""

import random
import math
import ROOT

def main():

    print("-----------------------------------------------------------------------")
    print("  This is a simulation of Buffon's needle experiment to calculate PI:  ")
    print("-----------------------------------------------------------------------")

    # Get input form user:
    
    bullshitinput = True
    
    while (bullshitinput):
        n = int(raw_input('Enter number of simulated needles: '))
        if (n > 0):
            if (n > 1000000):
                print('Not enough needles! Try again...')
            else:
                bullshitinput = False
        else:
            print('Unfortunately number is not a positive integer, try again...')
        
        
    bullshitinput = True
    
    while (bullshitinput):
        LSratio = float(raw_input('Enter needle length over grid spacing ratio [between 0 and 1]: '))
        if (0 < LSratio < 1):
            bullshitinput = False
        else:
            print('Unfortunately needle length to grid spacing ratio is not between 0 and 1, try again...')

    # Create ROOT canvas:
            
    c1 = ROOT.TCanvas('c1', "Simulation of Buffon's needle experiment", 0, 0, 500, 500)
    #c1.SetGridx(0)
    #c1.SetGridy(1)
    c1.SetLeftMargin(0.15)
    c1.SetRightMargin(0.15)
    c1.SetTopMargin(0.2)
    c1.SetBottomMargin(0.2)

    dummyhisto = ROOT.TH2D('dummyhisto', '', 100, -5, 5, 100, -5, 5)
    dummyhisto.SetStats(0)
    #dummyhisto.Draw()
    #dummyhisto.GetXaxis().SetTitle('x')
    #dummyhisto.GetYaxis().SetTitle('y')
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

    for i in range(0,n):

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

    # Create text:
        
    text0 = "Simulation of Buffon's needle experiment:"
    text0_ttext = ROOT.TText(-5.5, 7, text0);
    text0_ttext.SetTextSize(0.03);
    text0_ttext.Draw();

    text1 = "Needle length / Grid spacing (L/S) = {}".format(LSratio)
    text1_ttext = ROOT.TText(-5.5, 6, text1);
    text1_ttext.SetTextSize(0.03);
    text1_ttext.Draw();
        
    textnt_ttext = ROOT.TText(-4.5, 4.32, "N_total = {}".format(n));
    textnt_ttext.SetTextSize(0.03);
    textnt_ttext.Draw();
        
    textnc_ttext = ROOT.TText(-4.5, -4.62, "N_crossings = {}".format(count));
    textnc_ttext.SetTextSize(0.03);
    textnc_ttext.SetTextColor(2);
    textnc_ttext.Draw();
        
    # Calculate PI:
    
    pi_approx = 2*LSratio*n/float(count)
    
    print 'Needle length / Grid spacing (L/S)           = {}'.format(LSratio)
    print 'Total # of needles (N_t)                     = {}'.format(n) 
    print 'Total # of needles that crossed a line (N_c) = {}'.format(count)
    print ''
    print '=> PI ~= 2*(L/S)*(N_t/N_c) = {}'.format(pi_approx)

    text2 = "Pi ~= 2*(L/S)*(N_total/N_crossings) = {}*{}/{} = {:.6f}".format(2*LSratio,n,count,pi_approx)
    text2_ttext = ROOT.TText(-5.5, -6.25, text2);
    text2_ttext.SetTextSize(0.03);
    text2_ttext.Draw();

    # Calculate error wrt real Pi:
    
    error = (pi_approx - math.pi)/math.pi * 100

    print '=> (Pi_sim - Pi_real) / Pi_real * 100 = {:.3f}%'.format(error)
    
    text3 = "(Pi_sim - Pi_real) / Pi_real * 100 = {:.3f}%".format(error)
    text3_ttext = ROOT.TText(-5.5, -7, text3);
    text3_ttext.SetTextSize(0.03);
    text3_ttext.Draw();
    
    c1.Update()
    
    ROOT.gApplication.Run()
    
    return 0
  
if __name__ == '__main__':
    main()
