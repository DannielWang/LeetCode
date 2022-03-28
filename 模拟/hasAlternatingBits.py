class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 2
        while n:
            cur = n % 2
            if cur == prev:
                return False
            prev = cur
            n //= 2
        return True
