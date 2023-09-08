# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:59:16 2023

@author: serve
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
#import seaborn as sns
districts = {'101912':'Houston ISD',
              '101907':'Cypress Fairbanks ISD',
              '227901':'Austin ISD', 
              '152901':'Lubbock ISD',
              '165901':'Midland ISD',
              '57911':'Highland Park ISD'}

distlist = list(districts.keys())
colors = {distlist[0]:'#cc0017',
        distlist[1]:'#0089f1',
        distlist[2]:'#F78E1E', 
        distlist[3]:'#da6fab', 
        distlist[4]:'#000000', 
        distlist[5]:'#00A875'}
df = pd.read_csv(r'C:\Users\serve\OneDrive\Desktop\TEA-Presentation\Datasummary.csv')
df['District'] = df['District'].astype(str)

g= globals

plt.style.use('ggplot')
filepath = r'C:\Users\serve\OneDrive\Desktop\TEA-Presentation\\'
filenames = [] 
for yr in ['19','20','21','22']:   
    fig, ax = plt.subplots(figsize=(14,12))
    #ax.set_xlim(0, 0.3)
    ax.set_xlabel('enrollment',fontsize=28)
    ax.set_ylim(0.54, 1.06)
    ax.set_ylabel('ADA Ratio',fontsize=24)
    plt.axhline(y = 0.93, color = 'gray', linestyle = '--', label='Statewide average')
    #plt.axhline(y = np.sort(df['ratio'+yr])[10], color = 'gray', linestyle = '--', label='Minimum Ratio')
    plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper right')
    #plt.xticks(np.arange(-0.15, 0.33, 0.03),fontsize = 18) 
    plt.yticks(np.arange(0.55, 1.1, 0.05), fontsize = 18) 
    ax.set_title('School Year' + yr,fontsize=20)
    plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper right')
    plt.rc('legend',fontsize=20)
    ax.scatter(df['enrollment'+yr],df['ratio'+yr],color = 'gray',  s=15, alpha=0.3)
    dist_df = df.loc[df['District'].isin(list(districts.keys())), :]
    flag = dist_df.groupby('District')
    for key, group in flag:
        group.plot(ax=ax, kind='scatter', x='enrollment'+yr,y='ratio'+yr,label=districts[key], color = colors[key], marker='o', s=100)
    filename = yr +'.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()

# This chunk of the code makes the animation        
writer = imageio.get_writer('ADA_analysis.wmv',  fps=0.3, macro_block_size = 1)#The larger the fps, is the faster video
for filename in filenames:
    image = imageio.imread(filename)
    writer.append_data(image)
writer.close()
#This part deletes the unncessary png files after the video is created
#for filename in set(filenames):
#    os.remove(filename)
