
'''
A Discrete Mathematics professor has a class of NN students. Frustrated with their lack of discipline, he decides to cancel class if fewer than KK students are present when class starts.
Given the arrival time of each student, determine if the class is canceled.

Input Format
The first line of input contains TT, the number of test cases.
Each test case consists of two lines. The first line has two space-separated integers, NN (students in the class) and KK (the cancelation threshold). 
The second line contains NN space-separated integers (a1,a2,…,aNa1,a2,…,aN) describing the arrival times for each student.

Note: Non-positive arrival times (ai≤0ai≤0) indicate the student arrived early or on time; positive arrival times (ai>0ai>0) indicate the student arrived aiai minutes late.

Output Format
For each test case, print the word YES if the class is canceled or NO if it is not.
'''

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    p_cnt=0     #To count total present students
    for a_i in a:   #One by one check arrival time of each student
        if a_i <=0:
            p_cnt+=1
            
    if p_cnt>=k:
        print 'NO'
    else:
        print 'YES'
