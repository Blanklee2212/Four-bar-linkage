import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin, fminbound

#r = 2.0
# 2.圆心坐标
#a, b = (0., 0.)
#t = sp.symbols("t")

t = np.arange(0, 20, 0.01)
#theta = np.arange(0, 2*np.pi, 0.01)

#x = 2+2*(((5+COS(D4))^(1/2))*(SIN(D4))/((5-4*COS(D4))^(1/2)))
#Y = 2*(((5+COS(D4))^(1/2))*(2-COS(D4))/((5-4*COS(D4))^(1/2)))
#theta= 0.05*t**2; D4=theta

#x = 0.2+0.2*(sp.np.np.sqrt(5+sp.cos(0.05*t**2))*(sp.sin(0.05*t**2))/(sp.np.np.sqrt(5-4*sp.cos(0.05*t**2))))
#y = 0.2*(sp.np.np.sqrt(5+sp.cos(0.05*t**2))*(2-sp.cos(0.05*t**2))/(sp.np.np.sqrt(5-4*sp.cos(0.05*t**2))))
#print(sp.diff(x, t, 2))
#print(sp.diff(y, t, 2))
#print(np.diff(t))
#When acceleration is 0.1rad/s^2
#x = (-0.002*t**2*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*np.sin(0.05*t**2 + 4.89) - 0.003*t**2*np.sin(0.05*t**2 + 4.89)*np.cos(0.05*t**2 + 4.89)/np.sqrt(np.cos(0.05*t**2 + 4.89) + 5) - 0.0005*t**2*np.sin(0.05*t**2 + 4.89)**3/(np.cos(0.05*t**2 + 4.89) + 5)**(3/2) - 0.012*t**2*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*np.sin(0.05*t**2 + 4.89)*np.cos(0.05*t**2 + 4.89)/(5 - 4*np.cos(0.05*t**2 + 4.89)) + 0.004*t**2*np.sin(0.05*t**2 + 4.89)**3/((5 - 4*np.cos(0.05*t**2 + 4.89))*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)) + 0.024*t**2*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*np.sin(0.05*t**2 + 4.89)**3/(5 - 4*np.cos(0.05*t**2 + 4.89))**2 + 0.02*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*np.cos(0.05*t**2 + 4.89) - 0.01*np.sin(0.05*t**2 + 4.89)**2/np.sqrt(np.cos(0.05*t**2 + 4.89) + 5) - 0.04*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*np.sin(0.05*t**2 + 4.89)**2/(5 - 4*np.cos(0.05*t**2 + 4.89)))/np.sqrt(5 - 4*np.cos(0.05*t**2 + 4.89))
#y = (-0.002*t**2*np.sin(0.05*t**2 + 4.89)**2/np.sqrt(np.cos(0.05*t**2 + 4.89) + 5) - 0.004*t**2*(np.cos(0.05*t**2 + 4.89) - 2)*np.sin(0.05*t**2 + 4.89)**2/((5 - 4*np.cos(0.05*t**2 + 4.89))*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)) - 0.008*t**2*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*np.sin(0.05*t**2 + 4.89)**2/(5 - 4*np.cos(0.05*t**2 + 4.89)) + 0.2*(0.01*t**2*np.cos(0.05*t**2 + 4.89) + 0.1*np.sin(0.05*t**2 + 4.89))*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5) + 0.2*(np.cos(0.05*t**2 + 4.89) - 2)*(0.005*t**2*np.cos(0.05*t**2 + 4.89) + 0.0025*t**2*np.sin(0.05*t**2 + 4.89)**2/(np.cos(0.05*t**2 + 4.89) + 5) + 0.05*np.sin(0.05*t**2 + 4.89))/np.sqrt(np.cos(0.05*t**2 + 4.89) + 5) + 0.2*(np.cos(0.05*t**2 + 4.89) - 2)*np.sqrt(np.cos(0.05*t**2 + 4.89) + 5)*(0.02*t**2*np.cos(0.05*t**2 + 4.89) + 0.12*t**2*np.sin(0.05*t**2 + 4.89)**2/(4*np.cos(0.05*t**2 + 4.89) - 5) + 0.2*np.sin(0.05*t**2 + 4.89))/(5 - 4*np.cos(0.05*t**2 + 4.89)))/np.sqrt(5 - 4*np.cos(0.05*t**2 + 4.89))
#when acceleration is 1rad/s^2
#x = (-0.2*t**2*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*np.sin(0.5*t**2 + 4.89) - 0.3*t**2*np.sin(0.5*t**2 + 4.89)*np.cos(0.5*t**2 + 4.89)/np.sqrt(np.cos(0.5*t**2 + 4.89) + 5) - 0.05*t**2*np.sin(0.5*t**2 + 4.89)**3/(np.cos(0.5*t**2 + 4.89) + 5)**(3/2) - 1.2*t**2*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*np.sin(0.5*t**2 + 4.89)*np.cos(0.5*t**2 + 4.89)/(5 - 4*np.cos(0.5*t**2 + 4.89)) + 0.4*t**2*np.sin(0.5*t**2 + 4.89)**3/((5 - 4*np.cos(0.5*t**2 + 4.89))*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)) + 2.4*t**2*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*np.sin(0.5*t**2 + 4.89)**3/(5 - 4*np.cos(0.5*t**2 + 4.89))**2 + 0.2*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*np.cos(0.5*t**2 + 4.89) - 0.1*np.sin(0.5*t**2 + 4.89)**2/np.sqrt(np.cos(0.5*t**2 + 4.89) + 5) - 0.4*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*np.sin(0.5*t**2 + 4.89)**2/(5 - 4*np.cos(0.5*t**2 + 4.89)))/np.sqrt(5 - 4*np.cos(0.5*t**2 + 4.89))
#y = (-0.2*t**2*np.sin(0.5*t**2 + 4.89)**2/np.sqrt(np.cos(0.5*t**2 + 4.89) + 5) - 0.4*t**2*(np.cos(0.5*t**2 + 4.89) - 2)*np.sin(0.5*t**2 + 4.89)**2/((5 - 4*np.cos(0.5*t**2 + 4.89))*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)) - 0.8*t**2*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*np.sin(0.5*t**2 + 4.89)**2/(5 - 4*np.cos(0.5*t**2 + 4.89)) + 0.2*(t**2*np.cos(0.5*t**2 + 4.89) + np.sin(0.5*t**2 + 4.89))*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5) + 0.2*(np.cos(0.5*t**2 + 4.89) - 2)*(0.5*t**2*np.cos(0.5*t**2 + 4.89) + 0.25*t**2*np.sin(0.5*t**2 + 4.89)**2/(np.cos(0.5*t**2 + 4.89) + 5) + 0.5*np.sin(0.5*t**2 + 4.89))/np.sqrt(np.cos(0.5*t**2 + 4.89) + 5) + 0.2*(np.cos(0.5*t**2 + 4.89) - 2)*np.sqrt(np.cos(0.5*t**2 + 4.89) + 5)*(2.0*t**2*np.cos(0.5*t**2 + 4.89) + 12.0*t**2*np.sin(0.5*t**2 + 4.89)**2/(4*np.cos(0.5*t**2 + 4.89) - 5) + 2.0*np.sin(0.5*t**2 + 4.89))/(5 - 4*np.cos(0.5*t**2 + 4.89)))/np.sqrt(5 - 4*np.cos(0.5*t**2 + 4.89))
#1.5rad/s^2
#x = (-0.45*t**2*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*np.sin(0.75*t**2 + 4.89) - 0.675*t**2*np.sin(0.75*t**2 + 4.89)*np.cos(0.75*t**2 + 4.89)/np.sqrt(np.cos(0.75*t**2 + 4.89) + 5) - 0.1125*t**2*np.sin(0.75*t**2 + 4.89)**3/(np.cos(0.75*t**2 + 4.89) + 5)**(3/2) - 2.7*t**2*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*np.sin(0.75*t**2 + 4.89)*np.cos(0.75*t**2 + 4.89)/(5 - 4*np.cos(0.75*t**2 + 4.89)) + 0.9*t**2*np.sin(0.75*t**2 + 4.89)**3/((5 - 4*np.cos(0.75*t**2 + 4.89))*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)) + 5.4*t**2*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*np.sin(0.75*t**2 + 4.89)**3/(5 - 4*np.cos(0.75*t**2 + 4.89))**2 + 0.3*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*np.cos(0.75*t**2 + 4.89) - 0.15*np.sin(0.75*t**2 + 4.89)**2/np.sqrt(np.cos(0.75*t**2 + 4.89) + 5) - 0.6*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*np.sin(0.75*t**2 + 4.89)**2/(5 - 4*np.cos(0.75*t**2 + 4.89)))/np.sqrt(5 - 4*np.cos(0.75*t**2 + 4.89))
#y = (-0.45*t**2*np.sin(0.75*t**2 + 4.89)**2/np.sqrt(np.cos(0.75*t**2 + 4.89) + 5) - 0.9*t**2*(np.cos(0.75*t**2 + 4.89) - 2)*np.sin(0.75*t**2 + 4.89)**2/((5 - 4*np.cos(0.75*t**2 + 4.89))*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)) - 1.8*t**2*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*np.sin(0.75*t**2 + 4.89)**2/(5 - 4*np.cos(0.75*t**2 + 4.89)) + 0.2*(2.25*t**2*np.cos(0.75*t**2 + 4.89) + 1.5*np.sin(0.75*t**2 + 4.89))*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5) + 0.2*(np.cos(0.75*t**2 + 4.89) - 2)*(1.125*t**2*np.cos(0.75*t**2 + 4.89) + 0.5625*t**2*np.sin(0.75*t**2 + 4.89)**2/(np.cos(0.75*t**2 + 4.89) + 5) + 0.75*np.sin(0.75*t**2 + 4.89))/np.sqrt(np.cos(0.75*t**2 + 4.89) + 5) + 0.2*(np.cos(0.75*t**2 + 4.89) - 2)*np.sqrt(np.cos(0.75*t**2 + 4.89) + 5)*(4.5*t**2*np.cos(0.75*t**2 + 4.89) + 27.0*t**2*np.sin(0.75*t**2 + 4.89)**2/(4*np.cos(0.75*t**2 + 4.89) - 5) + 3.0*np.sin(0.75*t**2 + 4.89))/(5 - 4*np.cos(0.75*t**2 + 4.89)))/np.sqrt(5 - 4*np.cos(0.75*t**2 + 4.89))
#2rad/s^2

x = (-0.2*np.sqrt(np.cos(1.0*t + 4.712) + 5) - 0.3*np.cos(1.0*t + 4.712)/np.sqrt(np.cos(1.0*t + 4.712) + 5) - 0.05*np.sin(1.0*t + 4.712)**2/(np.cos(1.0*t + 4.712) + 5)**(3/2) - 1.2*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.cos(1.0*t + 4.712)/(5 - 4*np.cos(1.0*t + 4.712)) + 0.4*np.sin(1.0*t + 4.712)**2/((5 - 4*np.cos(1.0*t + 4.712))*np.sqrt(np.cos(1.0*t + 4.712) + 5)) + 2.4*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.sin(1.0*t + 4.712)**2/(5 - 4*np.cos(1.0*t + 4.712))**2)*np.sin(1.0*t + 4.712)/np.sqrt(5 - 4*np.cos(1.0*t + 4.712))
y = (0.2*(0.5*np.cos(1.0*t + 4.712) + 0.25*np.sin(1.0*t + 4.712)**2/(np.cos(1.0*t + 4.712) + 5))*(np.cos(1.0*t + 4.712) - 2)/np.sqrt(np.cos(1.0*t + 4.712) + 5) + 0.2*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.cos(1.0*t + 4.712) - 0.2*np.sin(1.0*t + 4.712)**2/np.sqrt(np.cos(1.0*t + 4.712) + 5) + 0.2*(np.cos(1.0*t + 4.712) - 2)*np.sqrt(np.cos(1.0*t + 4.712) + 5)*(2.0*np.cos(1.0*t + 4.712) + 12.0*np.sin(1.0*t + 4.712)**2/(4*np.cos(1.0*t + 4.712) - 5))/(5 - 4*np.cos(1.0*t + 4.712)) - 0.4*(np.cos(1.0*t + 4.712) - 2)*np.sin(1.0*t + 4.712)**2/((5 - 4*np.cos(1.0*t + 4.712))*np.sqrt(np.cos(1.0*t + 4.712) + 5)) - 0.8*np.sqrt(np.cos(1.0*t + 4.712) + 5)*np.sin(1.0*t + 4.712)**2/(5 - 4*np.cos(1.0*t + 4.712)))/np.sqrt(5 - 4*np.cos(1.0*t + 4.712))
def f(k):
    return (-0.2 * np.sqrt(np.cos(1.0 * k + 4.712) + 5) - 0.3 * np.cos(1.0 * k + 4.712) / np.sqrt(
        np.cos(1.0 * k + 4.712) + 5) - 0.05 * np.sin(1.0 * k + 4.712) ** 2 / (np.cos(1.0 * k + 4.712) + 5) ** (
                     3 / 2) - 1.2 * np.sqrt(np.cos(1.0 * k + 4.712) + 5) * np.cos(1.0 * k + 4.712) / (
                     5 - 4 * np.cos(1.0 * k + 4.712)) + 0.4 * np.sin(1.0 * k + 4.712) ** 2 / (
                     (5 - 4 * np.cos(1.0 * k + 4.712)) * np.sqrt(np.cos(1.0 * k + 4.712) + 5)) + 2.4 * np.sqrt(
        np.cos(1.0 * k + 4.712) + 5) * np.sin(1.0 * k + 4.712) ** 2 / (5 - 4 * np.cos(1.0 * k + 4.712)) ** 2) * np.sin(
        1.0 * k + 4.712) / np.sqrt(5 - 4 * np.cos(1.0 * k + 4.712))


k = np.linspace(0, 10, num=500)
min_global = fmin(f, 2)
print(min_global)



#x = a + r * np.cos(theta)
#y = b + r * np.sin(theta)
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(t, x)
axes.axis('equal')
plt.title('Acceleration with t, x')
plt.show()