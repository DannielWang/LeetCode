class Solution:
    def addDigits(self, num: int) -> int:
        total_sum = 0
        if num == 0:
            return 0
        while num:
            total_sum += int(num % 10)
            num = int(num / 10)
            if num == 0 and total_sum < 10:
                return total_sum
            if num == 0:
                num = total_sum
                total_sum = 0
