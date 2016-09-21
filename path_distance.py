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
        #Open a file to write the outputs to
        with open(self.path+'/Path_output.csv','w') as fp2:
            writer=csv.writer(fp2)
            writer.writerow(['Total Distance'])
            #Open the file to read the data
            with open(self.path+'/Path distance.csv','r') as fp:
                reader=csv.reader(fp)
                next(reader, None)  #Skip the header
                
                #Traverse through each row
                for row in reader:
                    self.tot_dist = 0   #Initialize the distance to 0
                    #Skipping the 1st column traverse the columns with a step of 2
                    for i in range(1, len(row)-2, 2):
                        if row[i+2] in (None,""):   #Check if there are any more columns to read
                            continue
                        else:
                            #Pass the coordinates of 2 consecutive points in the sequence
                            self.find_distance( (float(row[i]),float(row[i+1])), (float(row[i+2]),float(row[i+3])) )
                    print self.tot_dist
                    writer.writerow([self.tot_dist])

        fp2.close()
        fp.close()
    
    #Function to calculate distance between 2 coordinates given as input
    def find_distance(self,p1,p2):
        self.tot_dist += vincenty(p1,p2).miles
    
if __name__== '__main__':
    obj = path_distance()
    obj.path = os.getcwd()+'/data'
    #This function traverses through the data and writes the distance between coordinates to a new file
    obj.traverse()
