  def is_palindrome(self, n):
		# Code here
        temp = n
        rev = 0
        while n > 0:
            lastDigit = n % 10
            n = int(n / 10)
            rev = rev * 10 + lastDigit
        if rev == temp:
            return "Yes"
        else:
            return "No"
