'''
Little Bob loves chocolate, and he goes to a store with $N$N in his pocket. The price of each chocolate is $C$C. The store offers a discount: for every MM wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?

Input Format: 
The first line contains the number of test cases, TT. 
TT lines follow, each of which contains three integers, NN, CC, and MM.

Output Format: 
Print the total number of chocolates Bob eats.
'''

import sys

t = int(raw_input().strip())    #Get total number of lines to read
for a0 in xrange(t):
    tot=0   #To store the total number of chocolates bought
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    m11 = n/c    #Find number of chocolates which can be purchased
    tot+=m1     #Update total
    while m11 >= m:
        m22 = m11/m     #Find how many chocolates can be bought using wrappers
        tot+=m22        
        m11= (m11%m) + m22  #Update the number of wrappers
    print tot
