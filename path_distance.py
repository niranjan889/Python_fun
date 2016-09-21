'''
Created on 2016-09-17

@author: Niranjan
'''

import os
import csv
import sys
from geopy.distance import vincenty

class path_distance():
    
    def __init__(self):
        self.tot_dist = 0
        self.path = os.getcwd()
        
    def traverse(self):
        with open(self.path+'/Path_output.csv','w') as fp2:
            writer=csv.writer(fp2)
            with open(self.path+'/Path distance.csv','r') as fp:
                reader=csv.reader(fp)
                next(reader, None)
                cnt=0
                for row in reader:
                    self.tot_dist = 0
                    for i in range(1, len(row)-2, 2):
                        if row[i+2] in (None,""):
                            continue
                        else:
                            self.find_distance( (float(row[i]),float(row[i+1])), (float(row[i+2]),float(row[i+3])) )
                    cnt+=1
                    print self.tot_dist
                    writer.writerow([self.tot_dist])

        fp2.close()
        fp.close()
        
    def find_distance(self,p1,p2):
        
        self.tot_dist += vincenty(p1,p2).miles
 
def google_distance():
    orig_coord = -84.75950132, 43.60729635
    dest_coord = -84.75946273, 43.60729638

    print vincenty(orig_coord,dest_coord).miles
    sys.exit()   
    
if __name__== '__main__':
#     google_distance()
    obj = path_distance()
    obj.path = os.getcwd()+'/data'
    
    obj.traverse()