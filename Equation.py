import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#r = 2.0
# 2.圆心坐标
#a, b = (0., 0.)
t = sp.symbols("t")
#t = np.arange(0, 3, 0.01)
#theta = np.arange(0, 2*np.pi, 0.01)

#x = 2+2*(((5+COS(D4))^(1/2))*(SIN(D4))/((5-4*COS(D4))^(1/2)))
#Y = 2*(((5+COS(D4))^(1/2))*(2-COS(D4))/((5-4*COS(D4))^(1/2)))
#theta= 0.05*t**2; D4=theta
Judge = float(input("What motion do you want: \n1. Constant angular velocity \n2. Acceleration movement\n"))
if Judge == 1:
    v = float(input("Input the angular velocity (rad/s): "))
    o = round(sp.pi / 180 * float(input("Input the starting angle(degree): ")), 3)
    x = 0.2+0.2*(sp.sqrt(5+sp.cos(v*t+o))*(sp.sin(v*t+o))/(sp.sqrt(5-4*sp.cos(v*t+o))))
    y = 0.2*(sp.sqrt(5+sp.cos(v*t+o))*(2-sp.cos(v*t+o))/(sp.sqrt(5-4*sp.cos(v*t+o))))
    ax = str(sp.diff(x, t, 2))
    ay = str(sp.diff(y, t, 2))
    def convert(s):
        s1 = ((s.replace('sin', 'np.sin')).replace('cos', 'np.cos')).replace('sqrt', 'np.sqrt')
        print(s1)
    print(convert(ax))
    print(convert(ay))
elif Judge == 2:
    a = float(input("Input the acceleration (rad/s^2): "))
    o = round(sp.pi/180*float(input("Input the starting angle(degree): ")), 3)
    x = 0.2+0.2*(sp.sqrt(5+sp.cos((a/2)*t**2+o))*(sp.sin((a/2)*t**2+o))/(sp.sqrt(5-4*sp.cos((a/2)*t**2+o))))
    y = 0.2*(sp.sqrt(5+sp.cos((a/2)*t**2+o))*(2-sp.cos((a/2)*t**2+o))/(sp.sqrt(5-4*sp.cos((a/2)*t**2+o))))
    ax = str(sp.diff(x, t, 2))
    ay = str(sp.diff(y, t, 2))
    def convert(s):
        s1 = ((s.replace('sin', 'np.sin')).replace('cos', 'np.cos')).replace('sqrt', 'np.sqrt')
        print(s1)
    print(convert(ax))
    print(convert(ay))
else:
    print("Input error, please only input 1 or 2")






#x = 2+2*(np.sqrt(5+np.cos(theta))*(np.sin(theta))/(np.sqrt(5-4*np.cos(theta))))
#y = 2*(np.sqrt(5+np.cos(theta))*(2-np.cos(theta))/(np.sqrt(5-4*np.cos(theta))))


#x = a + r * np.cos(theta)
#y = b + r * np.sin(theta)
#fig = plt.figure()
#axes = fig.add_subplot(111)
#axes.plot(x, y)
#axes.axis('equal')
#plt.title('Displacement trajectory')
#plt.show()