def armstrongNumber (self, n):
        # code here 
        sum = 0
        temp = n
        while n > 0:
            ld = n % 10
            sum += ld * ld * ld
            n = int (n / 10)
        if sum == temp:
            return "true"
        else:
            return "false"
