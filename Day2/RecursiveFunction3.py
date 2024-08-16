def printNos(self, n):
        # Print N to 1 with out loop
        if(n>0):
            print(n,end =" ")
            self.printNos(n-1)
