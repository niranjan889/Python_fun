import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    p_cnt=0
    for a_i in a:
        if a_i <=0:
            p_cnt+=1
            
    if p_cnt>=k:
        print 'NO'
    else:
        print 'YES'
