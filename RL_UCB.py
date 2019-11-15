# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:33:36 2019

@author: sridhar
"""

#Importing the Libararies
import pandas as pd
import matplotlib.pyplot as plt
import math

#Importing the Dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#UCB
N=10000
d= 10
ads_selected = []
total_reward = 0
numbers_of_selection =[0]*d
sum_of_rewards = [0]*d
for n in range(0, N):
    ad  = 0
    max_upper_bound = 0
    for i in range(0,d):
        if (numbers_of_selection[i] > 0):
            average_reward = sum_of_rewards[i] / numbers_of_selection[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selection[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selection[ad] = numbers_of_selection[ad] + 1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
        
