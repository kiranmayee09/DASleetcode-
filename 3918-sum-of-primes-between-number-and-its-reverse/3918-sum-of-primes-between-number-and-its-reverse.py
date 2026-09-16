class Solution:
    def sumOfPrimesInRange(self, n):
        
        # Reverse n
        r = int(str(n)[::-1])
        
        # Find range
        start = min(n, r)
        end = max(n, r)
        
        total = 0
        
        # Check every number in the range
        for num in range(start, end + 1):
            
            if num < 2:
                continue
            
            prime = True
            
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            
            if prime:
                total += num
        
        return total