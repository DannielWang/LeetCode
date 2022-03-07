class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # counter
        c = Counter(s)
        d = Counter(t)
        for (ans, value) in (d - c).items():
            return ans
