class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxnum = float('-inf')
        for i in accounts:
            maxnum = max(maxnum, sum(i))
        return maxnum