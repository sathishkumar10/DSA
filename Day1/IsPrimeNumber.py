def isPrime (self, N):
        # code here
        cnt =0
        for i in range(1, int(N ** 0.5)+1):
            if N % i == 0:
                cnt += 1
                if i != N//i:
                    cnt += 1
        if cnt == 2:
            return 1
        else:
            return 0
