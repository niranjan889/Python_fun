'''
Created on 2015-11-20
@author: Niranjan
'''
import copy
import multiprocessing as mp
from datetime import datetime        

#Function to compare 2 sets and return their intersection
def matches(params):
    
    param1, param2 = params
    inter = set(param1) & set(param2)
    #If there are more than 1 common items
    if len(inter)>1:
        return inter

#Function to count number of occurrences of each unique intersection
def incr(cmn_ven):
    
    if tuple(cmn_ven) not in dict_cnt:
        dict_cnt[tuple(cmn_ven)]=1
    else:
        dict_cnt[tuple(cmn_ven)]+=1
    
    return 0
    
if __name__ == '__main__':
    num_proc=4
    list1=[(1,2)]*3     #list1, l11, l22 are concatenated to form a single input list 
    # l11=[(2,3)]*50
    l11=[]
    l12=[(1,2,3)]*3
    dict_cnt=dict()
    dict_com=dict()
    list1+=l11+l12
    list2=copy.deepcopy(list1)
    
    #Create processes 
    pool = mp.Pool(processes=num_proc)
    t1=datetime.now()
    #Traverse through each set and compare that set with rest of the sets
    for item in list1:
        #Remove the current set from list
        list2.remove(item)
        #Check if there is at least 1 set to compare to
        if len(list2)>0:
            #Only 1 iterable can be passed to pool.map function.
            #So, zip the current set and sets to be compared with it
            l_temp=[item]*len(list2)
            params=zip(l_temp,list2)
            
            #Compare the sets and store the intersections in list
            results = pool.map(matches,params)
#             f_res+=[match for match in results if match is not None]
            #Count the number of occurrences of each intersection
            map(incr,[match for match in results if match is not None])

    pool.close()
    pool.join()
    t2=datetime.now()
    print 'Total time taken:',t2-t1
    print 'The final counts are:\n',dict_cnt
