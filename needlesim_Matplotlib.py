#!/usr/local/bin/python3 -tt
"""
Simulate Buffon's needle experiment to calculate PI. 
"""

import math
import random
import matplotlib.pyplot as plt
import time

def needlesim_Matplotlib():

    random.seed(42)    
    
    print("-----------------------------------------------------------------------")
    print("  This is a simulation of Buffon's needle experiment to calculate PI:  ")
    print("-----------------------------------------------------------------------")

    # Get input form user:
    
    badinput = True
    
    while (badinput):
        n = int(input('Enter number of simulated needles: '))
        if (n > 0):
            if (n > 1000000):
                print('Not enough needles! Try again...')
            else:
                badinput = False
        else:
            print('Unfortunately number is not a positive integer, try again...')
        
    badinput = True
    
    while (badinput):
        LSratio = float(input('Enter needle length over grid spacing ratio [between 0 and 1]: '))
        if (0 < LSratio < 1):
            badinput = False
        else:
            print('Unfortunately needle length over grid spacing ratio is not between 0 and 1, try again...')

    start = time.time()
            
    # Create Matplotlib figure with gridlines:
    
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    for i in range(-4, 5):
        plt.plot([-4.5, 4.5], [i, i], color='black', linewidth=1)

    plt.xlim(-5,5)
    plt.ylim(-5,5)
        
    # Loop over needles:

    count = 0

    xcoords_crossed    = [] # Needed for faster plotting
    ycoords_crossed    = [] # Needed for faster plotting
    xcoords_notcrossed = [] # Needed for faster plotting
    ycoords_notcrossed = [] # Needed for faster plotting
    
    for i in range(n):

        # Create needle:
        
        x1    = 6*random.random()-3
        y1    = 6*random.random()-3
        angle = 2*math.pi*random.random()

        x2 = LSratio*math.cos(angle) + x1
        y2 = LSratio*math.sin(angle) + y1
        
        # Check if needle crossed a gridline:
        
        crossed = False
        for k in range(-3,4):
            if ((y2>k) and (y1<k)) or ((y2<k) and (y1>k)):
                crossed = True

        # Count & save needles:
               
        if crossed:
            count += 1            
            xcoords_crossed.append(x1)
            xcoords_crossed.append(x2)
            xcoords_crossed.append(None)
            ycoords_crossed.append(y1)
            ycoords_crossed.append(y2)
            ycoords_crossed.append(None)
            #plt.plot([x1, x2], [y1, y2], color='red', linewidth=1) # Slow
        else:
            xcoords_notcrossed.append(x1)
            xcoords_notcrossed.append(x2)
            xcoords_notcrossed.append(None)
            ycoords_notcrossed.append(y1)
            ycoords_notcrossed.append(y2)
            ycoords_notcrossed.append(None)
            #plt.plot([x1, x2], [y1, y2], color='blue', linewidth=1) # Slow

    plt.plot(xcoords_crossed,    ycoords_crossed,    color='red',  linewidth=1) # Fast
    plt.plot(xcoords_notcrossed, ycoords_notcrossed, color='blue', linewidth=1) # Fast
            
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
    
    plt.subplots_adjust(top = 0.8)
    
    plt.title("Simulation of Buffon's needle experiment with {} needles ($N_{{total}}$)\n where the needle length over grid spacing ratio ($L/S$) equals {}:\n\n".format(n, LSratio)) 

    plt.subplots_adjust(bottom = 0.3)

    plt.text(6, -2, r"$N_{{crossings}} = {}$".format(count), color='red')
    
    #plt.text(-8, -8, r"$\pi_{{sim}} \approx 2\;\left(\frac{{L}}{{S}}\right)\;\left(\frac{{N_{{total}}}}{{N_{{crossings}}}}\right) = {}*{}/{} = {:.6f}$".format(2*LSratio,n,count,pi_approx))
    plt.text(-8, -8, r"$\pi_{{sim}} \approx 2\;(L/S)\;N_{{total}}/N_{{crossings}} = {}*{}/{} = {:.6f}$".format(2*LSratio,n,count,pi_approx))

    #plt.text(-8, -9.5, r"$\frac{{\pi_{{sim}} - \pi}}{{\pi}} * 100 = {:.3f}\%$".format(error))
    plt.text(-5, -9.5, r"$(\pi_{{sim}} - \pi)/\pi * 100 = {:.3f}\%$".format(error))
    
    end = time.time()
    print('\ntime = {} ms'.format((end - start)*1000))

    plt.show()

    return 0
  
if __name__ == '__main__':
    needlesim_Matplotlib()
