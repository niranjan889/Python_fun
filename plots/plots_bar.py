'''
Created on Jun 10, 2016

@author: hadoop
'''

import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

#Takes input as 4 lists, the output is a 2 x 2 grid.
def bar_plot2(data_x,data_y1,data_y2,data_y3,data_y4):
    font = {'family' : 'Serif',
        'weight' : 'normal',
        'size'   : 16}
    rc('font', **font)
    
    c1='#000000'    #set color of the bar in the plot
    
    #To plot
    fig = plt.figure(num=1,figsize=(14,8))
    ax = fig.add_subplot(221)
    list_vals=np.array(data_y1)
            
    N = len(list_vals)      
    ind = np.arange(N)  # the x locations for the groups
    width = 0.4       # the width of the bars
    b=ax.bar(ind, list_vals, width, color=c1)
    
    # add some text for labels, title and axes ticks
#     ax.set_ylabel('Y axis label',fontsize=18)
#     ax.set_xlabel('a). Model 1',fontsize=18)
    ax.set_xticks(ind+width/2)
    ax.set_xticklabels(data_x)

    #2nd plot
    ay = fig.add_subplot(222)
    list_vals=np.array(data_y2)
    
    N = len(list_vals)      
    ind = np.arange(N)  # the x locations for the groups
    width = 0.4       # the width of the bars
    b=ay.bar(ind, list_vals, width, color=c1)
    
#     ay.set_ylim(0,0.6)
    # add some text for labels, title and axes ticks
#     ay.set_ylabel('',fontsize=18)
#     ay.set_xlabel('b). Moscow',fontsize=18)
    ay.set_xticks(ind+width/2)
    ay.set_xticklabels(data_x)
    
    #3rd plot
    ay = fig.add_subplot(223)
    list_vals=np.array(data_y3)
    
    N = len(list_vals)      
    ind = np.arange(N)  # the x locations for the groups
    width = 0.4       # the width of the bars
    b=ay.bar(ind, list_vals, width, color=c1)
    
    # add some text for labels, title and axes ticks
#     ay.set_ylabel('',fontsize=18)
#     ay.set_xlabel('c). Chicago',fontsize=18)
    ay.set_xticks(ind+width/2)
    ay.set_xticklabels(data_x)
    
    #4th plot
    ay = fig.add_subplot(224)
    list_vals=np.array(data_y4)
    
    N = len(list_vals)      
    ind = np.arange(N)  # the x locations for the groups
    width = 0.4       # the width of the bars
    b=ay.bar(ind, list_vals, width, color=c1)
    
    # add some text for labels, title and axes ticks
#     ay.set_ylabel('',fontsize=18)
#     ay.set_xlabel('d). Los Angeles',fontsize=18)
    ay.set_xticks(ind+width/2)
    ay.set_xticklabels(data_x)
    
    plt.subplots_adjust(bottom = 0.1,top = 0.95,wspace = 0.2,hspace = 0.3 )
    plt.show()
    # plt.savefig('path/to/destination',orientation='portrait',bbox_inches='tight',dpi=300)

#Takes input as 4 lists with each list having values for each bar. The output is single graph with 4 bars 
def bar_plot1(data_x, data_y1, data_y2, data_y3, data_y4):
    font = {'family' : 'Serif',
        'weight' : 'normal',
        'size'   : 16}
    rc('font', **font)
    
    c1='#FFFFFF'
    c2='#D1D0CE'
    c3='#777777'
    c4='#000000'
    #To plot
    fig = plt.figure(num=1,figsize=(14,8))
    ay = fig.add_subplot(111)
    
    list_vals=np.array(data_y1)
    list_vals1=np.array(data_y2)
    list_vals2=np.array(data_y3)
    list_vals3=np.array(data_y4)
            
    N = len(list_vals)      
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars
    b=ay.bar(ind, list_vals, width, color=c1)
    b1=ay.bar(ind+0.2, list_vals1, width, color=c2)
    b2=ay.bar(ind+0.4, list_vals2, width, color=c3)
    b3=ay.bar(ind+0.6, list_vals3, width, color=c4)
    
    # add some text for labels, title and axes ticks
#     ay.set_ylabel('',fontsize=18)
#     ay.set_xlabel('',fontsize=18)
    ay.set_xticks(ind+width*2)
    ay.set_xticklabels(data_x)
#     ay.legend((b,b1,b2,b3), ('STM','PBM','MM','RC'),ncol=n_col,prop={'size':10},frameon=True,loc=loc).draggable()
     
    plt.subplots_adjust(bottom = 0.1,top = 0.95,wspace = 0.2,hspace = 0.3 )
    plt.show()
#     plt.savefig('path/to/destination',orientation='portrait',bbox_inches='tight',dpi=300)
    
if __name__=='__main__':
    data_x=['p@2','p@5','p@10','p@20'] # 'names for each group of plots.'
    data_y1=[0.5,0.6,0.75]  
    data_y2=[0.4,0.66,0.7]
    data_y3=[0.23,0.5,0.61]
    data_y4=[0.33,0.4,0.58]
    bar_plot2(data_x, data_y1, data_y2, data_y3, data_y4)
#     bar_plot1(data_x, data_y1, data_y2, data_y3, data_y4)
