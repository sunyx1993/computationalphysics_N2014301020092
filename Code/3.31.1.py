# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 12:12:46 2016

@author: admin12
"""

import matplotlib.pyplot as plt

class billiard_rectangular:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i] < -1.0):
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                self.x[i],self.y[i] = self.correct('y>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                self.x[i],self.y[i] = self.correct('y<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i] 
            else:
                pass
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
    
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
    
    def reflect(self):
        pass
    
    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(self.x,self.y)
        plt.title('Reflect in square table')
        plt.savefig('chapter3_3.31.png',dpi = 144)
        plt.show()
A = billiard_rectangular(0.5,0.5,0.47,0.323,4000,0.1)
A.motion_calculate()
A.reflect()
A.plot()
