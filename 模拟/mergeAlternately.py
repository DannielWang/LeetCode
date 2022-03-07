class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        res = ""
        n = len(word1)
        m = len(word2)
        if n > m:
            res = word1[m:-1] + word1[-1:]
            word1 = word1[:m]
            for i in range(m):
                ans = ans + word1[i] + word2[i]
        elif n == m:
            for i in range(n):
                ans = ans + word1[i] + word2[i]
        else:
            res = word2[n:-1] + word2[-1:]
            word2 = word2[:n]
            for i in range(n):
                ans = ans + word1[i] + word2[i]

        ans = ans + res
        return ans