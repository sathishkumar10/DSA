 def printGfg(self, n):
        # Print name n times with out using loop
        
        if n>0:
            self.printGfg(n-1)
            print("GFG", end = " ")
