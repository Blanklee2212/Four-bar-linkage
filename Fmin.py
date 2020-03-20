import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin, fminbound

t = np.linspace(0, 20, num=500)


def x(t):
    return (-0.2*np.sqrt(np.cos(1.0*t + 4.712) + 5) - 0.3*np.cos(1.0*t + 4.712)/np.sqrt(np.cos(1.0*t + 4.712) + 5) - 0.05*np.sin(1.0*t + 4.712)**2/(np.cos(1.0*t + 4.712) + 5)**(3/2) - 1.2*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.cos(1.0*t + 4.712)/(5 - 4*np.cos(1.0*t + 4.712)) + 0.4*np.sin(1.0*t + 4.712)**2/((5 - 4*np.cos(1.0*t + 4.712))*np.sqrt(np.cos(1.0*t + 4.712) + 5)) + 2.4*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.sin(1.0*t + 4.712)**2/(5 - 4*np.cos(1.0*t + 4.712))**2)*np.sin(1.0*t + 4.712)/np.sqrt(5 - 4*np.cos(1.0*t + 4.712))


def y(t):
    return (0.2*(0.5*np.cos(1.0*t + 4.712) + 0.25*np.sin(1.0*t + 4.712)**2/(np.cos(1.0*t + 4.712) + 5))*(np.cos(1.0*t + 4.712) - 2)/np.sqrt(np.cos(1.0*t + 4.712) + 5) + 0.2*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.cos(1.0*t + 4.712) - 0.2*np.sin(1.0*t + 4.712)**2/np.sqrt(np.cos(1.0*t + 4.712) + 5) + 0.2*(np.cos(1.0*t + 4.712) - 2)*np.sqrt(np.cos(1.0*t + 4.712) + 5)*(2.0*np.cos(1.0*t + 4.712) + 12.0*np.sin(1.0*t + 4.712)**2/(4*np.cos(1.0*t + 4.712) - 5))/(5 - 4*np.cos(1.0*t + 4.712)) - 0.4*(np.cos(1.0*t + 4.712) - 2)*np.sin(1.0*t + 4.712)**2/((5 - 4*np.cos(1.0*t + 4.712))*np.sqrt(np.cos(1.0*t + 4.712) + 5)) - 0.8*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.sin(1.0*t + 4.712)**2/(5 - 4*np.cos(1.0*t + 4.712)))/np.sqrt(5 - 4*np.cos(1.0*t + 4.712))


minx = fmin(x, 2)
miny = fmin(y, 2)
print(minx)
print(miny)