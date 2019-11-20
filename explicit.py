#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:43:35 2019

@author: iha

Disclaimer: This code is extracted from lecture notes by Carl Fredrik Berg
"""

import numpy as np
import matplotlib.pyplot as plt

def explicitTimeStep(afPressure,fAlpha,fLeftPressure, fRightPressure):
    afPressureNextTimestep=afPressure[:] 
    afPressureNextTimestep[0]=afPressure[0]+(4.0/3.0)*fAlpha*(afPressure[1]-3.0*afPressure[0]+2.0*fLeftPressure) 
    afPressureNextTimestep[-1]=afPressure[-1]+(4.0/3.0)*fAlpha*(2.0* fRightPressure-3.0*afPressure[-1]+afPressure[-2]) 
    afPressureNextTimestep[1:-1]=afPressure[1:-1]+fAlpha*(afPressure[2:]-2.0*afPressure[1:-1]+afPressure[:-2]) 
    return afPressureNextTimestep

#Initialization of parameters 
iNumberCells=100 #number of grid cells 
fDeltat=1.0E-5 #time step 
fEta=1.0 
fModelLength=1.0 #meters 
fInitialPressure=1.0 #pascal 
fLeftPressure=2.0 #pascal 
fRightPressure=1.0 #pascal

fDeltax=fModelLength/iNumberCells 

fAlpha=fEta*fDeltat/fDeltax**2 


#Main Loop
fTime=0.0
iNumberLoops=30000 
fMaxtime=fDeltat*iNumberLoops 

afPressure = fInitialPressure*np.ones(iNumberCells)

plt.figure(figsize=(16,9))
plt.xlabel('Grid number')
plt.ylabel('Pressure (Pascal)')

i = 0
while(fTime<fMaxtime): 

    fTime+=fDeltat
    afPressure=explicitTimeStep(afPressure,fAlpha,fLeftPressure,fRightPressure)
    
    if i in [1,10,50,100,500,1000,5000,10000]:
        pressure = []
        pressure.append(fLeftPressure)
        pressure.extend(afPressure)
        pressure.append(fRightPressure)
        
    
        plt.plot(pressure, color=(0.4,1-i/iNumberLoops, i/iNumberLoops), label='time = %.3f' %fTime)
        
    
    i += 1

plt.legend(loc='upper right')
plt.show()
plt.close()