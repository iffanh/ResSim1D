#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:43:35 2019

@author: iha

Disclaimer: This code is extracted from lecture notes by Carl Fredrik Berg
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def analytical1DSolution(afx,fLength,fEta,fLeftPressure,fRightPressure,fTime,inn): 
    afSum=0.0 
    
    for ii in range(1,inn+1): 
        afSum+=np.sin(ii*math.pi*afx/fLength)*np.exp(-ii**2*math.pi**2*fEta*fTime/(fLength**2))/ii 
        afPressure=fLeftPressure+(fRightPressure-fLeftPressure)*(afx/fLength+(2.0/math.pi)*afSum) 
        
    return afPressure


##afx=np.arange(-2.0,2.0,0.01) 
#afx=np.arange(0.0,1.0,0.01) 
#fLength=1.0 
#fEta=1.0 
#fLeftPressure=2.0 
#fRightPressure=1.0 
#fTime=1E-5
#
#
##Convergence of the Fourier series solution
#
#plt.figure(1, figsize=(16,9))
#
#plt.xlabel('Length')
#plt.ylabel('Pressure')
#
#plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure,fRightPressure,fTime,1),label='1',color='r') 
#
#plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure,fRightPressure,fTime,2),label='2',color='b')
#
#plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure,fRightPressure,fTime,5),label='5',color='y')
#
#plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure,fRightPressure,fTime,10),label='10',color='g')
#
#plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure,fRightPressure,fTime,100),label='100',color='k')
#
#plt.legend()





# Real simulation
afx=np.arange(0.0,1.0,0.01) 
fLength=1.0 
fEta=1.0 
fLeftPressure=2.0 
fRightPressure=1.0 

inn = 1000


plt.figure(2, figsize=(16,9))


plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure, fRightPressure,1E-2,inn),label='1E-2',color='r') 
plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure, fRightPressure,5E-2,inn),label='5E-2',color='b') 
plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure, fRightPressure,1E-1,inn),label='1E-1',color='y') 
plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure, fRightPressure,5E-1,inn),label='5E-1',color='g') 
plt.plot(afx,analytical1DSolution(afx,fLength,fEta,fLeftPressure, fRightPressure,1,inn),label='1',color='k') 

plt.legend()