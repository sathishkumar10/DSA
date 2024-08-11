def reverse_digit(self, n):
		# Reverse a given number 7896, Output = 6987
		rev = 0
        while (n > 0):
            lastDigit = n % 10
            n = int(n / 10); # Converting float to int
            rev = (rev * 10) + lastDigit
        
        return rev
