def printNos(self,N):
        #Print 1 to N with out loop
        if N<1:
            return
        self.printNos(N-1)
        print(N, end=" ")
