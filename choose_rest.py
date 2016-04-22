'''
Created on 2016-04-02
@author: Niranjan
'''
import numpy as np
import sys

class choose_rest():
    
    def __init__(self):
        self.choices=[] #Initialize an empty list
    
    def get_rest(self,choices):
        if type(choices)==type(self.choices):   #check if the input type is list
            self.choices=choices
            choice=np.random.choice(self.choices)   #Select a restaurant randomly
            return choice
        else:
            print 'Error! Incorrect input type: {}\nInput type must be a {}'.format(type(choices),type(self.choices))
            sys.exit()

if __name__=='__main__':
    my_choices=['Italian','Indian','Chinese','Thai']    #A list of places to choose from
    my_rest=choose_rest()   #Cretae a class object
    ch=my_rest.get_rest(my_choices)     #Call the function with input list as argument
    print 'Congrats! You are going to have {} today.'.format(ch)
    
