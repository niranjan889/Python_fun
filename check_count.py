'''
Created on 2016-05-05

@author: Niranjan
'''
import csv
import json
import operator

filename='newyork'
def count():
    cnt=0
    dict_v_chk={}
    path=path='/home/anand/Documents/Niranjan/4Sqaure/Collaborator/'
    with open(path+filename+'_venues.csv','r') as fp:
        reader=csv.reader(fp)
        for row in reader:
            chk=row[7]
            v=row[0]
            if v not in dict_v_chk:
                dict_v_chk[v]=int(chk)
    
    to_combs = sorted(dict_v_chk.items(), key=operator.itemgetter(1),reverse=False)
    cnt=100
    dict_new={}
    #Take last 100 tuples
    for tup in to_combs[-100:]:
        dict_new[cnt]=tup[0]
        cnt-=1
        
    with open(path+'hypothesis_testing/'+filename+'_chkinCnt.json','w') as fp1:
        json.dump(dict_new,fp1)
            
if __name__=='__main__':
    count()            
