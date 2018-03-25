# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:25:42 2017

@author: Administrator
"""

import math  
import time  
import numpy as np  
import matplotlib.pylab as plt  
import random  
class Samples:  
    def __init__(self):  
        pass  
    def mh(self, epsilon_0, num_iteration, fpdf):  
        #Metropolis–Hastings algorithm  
        normal_randoms = np.zeros(num_iteration)  
        uniform_randoms = np.zeros(num_iteration)  
        for i in range(0, num_iteration):  
            uniform_randoms[i] = random.uniform(0, 1)  
            normal_randoms[i] = random.normalvariate(0, 1)  
        fig = plt.figure()  
        ax = fig.add_subplot(211)  
        ax.plot(normal_randoms, '.')  
        ax1 = fig.add_subplot(212)  
        ax1.plot(uniform_randoms, '.')  
        plt.show()  
          
        epsilon = np.zeros(num_iteration)  
        previous_epsilon = epsilon_0  
        for i in range(0, num_iteration):#0到 num_iteration 
            epsilon_tilde = previous_epsilon + normal_randoms[i]  
            if(fpdf(epsilon_tilde) > fpdf(previous_epsilon)):  
                epsilon[i] = epsilon_tilde  
            else:  
                if(uniform_randoms[i] <= fpdf(epsilon_tilde) / fpdf(previous_epsilon)):  
                    epsilon[i] = epsilon_tilde  
                else:  
                    epsilon[i] = previous_epsilon  
            previous_epsilon = epsilon[i]  
        return epsilon  
      
    def mh1(self, epsilon_0, num_iteration, fpdf):  
        #Metropolis–Hastings algorithm  
        normal_randoms = np.zeros(num_iteration)  
        uniform_randoms = np.zeros(num_iteration)  
        for i in range(0, num_iteration):  
            uniform_randoms[i] = random.uniform(0, 1)  
            normal_randoms[i] = random.normalvariate(0, 1)  
          
        epsilon = np.zeros(num_iteration)  
        previous_epsilon = epsilon_0  
        for i in range(0, num_iteration):  
            epsilon_tilde = previous_epsilon + normal_randoms[i]  
            rate = fpdf(epsilon_tilde) / fpdf(previous_epsilon)  
            alfa = min(rate, 1.0)  
            if(uniform_randoms[i] < alfa):  
                epsilon[i] = epsilon_tilde  
            else:  
                epsilon[i] = previous_epsilon  
            previous_epsilon = epsilon[i]  
        return epsilon  
def nor(x):  
    return (1.0/np.sqrt(2.0*np.pi))*np.exp(-np.power(x,2)/2)  
if __name__=='__main__':  
    s = Samples()  
    x0 = s.mh(0, 5000, nor)  
    x = s.mh1(0, 5000, nor)  
    fig = plt.figure()  
    ax = fig.add_subplot(211)  
    ax.hist(x0,200)  
    ax = fig.add_subplot(212)  
    ax.hist(x, 200)  
    plt.show()  
    #s.acceptanceRejection('normal')  