# import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
regionpop = pd.read_csv("regionpop.csv", header=None)

#defined a function to calculate the population
def cal_pop(num):
    country = regionpop.iloc[num][0]
    init_pop = regionpop.iloc[num][1]
    each_pop = [init_pop]
    for i in range(2,18):
        each_pop.append( each_pop[-1] * (1 + regionpop.iloc[num][i]))
    return country, each_pop

# subplot each region's population
fig, figax = plt.subplots(6,1, figsize = (10,20))    
for i in range(len(regionpop)):
    time = np.arange(2020,2101,5)
    figax[i].plot(time, cal_pop(i)[1])
    figax[i].set_title(cal_pop(i)[0],fontsize=15)
    figax[i].set_xlabel('time')
    figax[i].set_ylabel('Population')
    figax[i].grid(True)
    plt.tight_layout()
    
plt.savefig("region population.jpg")
