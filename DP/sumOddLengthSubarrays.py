class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        k = 1
        m = 0
        total_sum = 0
        while k <= n:
            for i in range(n - m):
                total_sum = total_sum + sum(arr[i:i + k])
            if k <= n:
                k += 2
                m += 2
        return total_sum