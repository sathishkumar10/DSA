import math
class Solution:
    def print_divisors(self, N):
        # code here
        a = []
        # instead of sqrt we can try i*i < n also
        for i in range(1,int(math.sqrt(N)+1)):
            if N % i == 0:
                a.append(i)
                if int(N/i) != i:
                    a.append(int(N/i))
            
        a.sort()
        for i in a:
            print(i,end = ' ')
