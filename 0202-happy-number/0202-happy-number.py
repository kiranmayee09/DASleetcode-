class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_number(n):
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit 
                n //= 10

            return total

        slow = n
        fast = next_number(n)

        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1