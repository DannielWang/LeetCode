class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s) - 1
        ans = ""
        hashtable = {}
        words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                "w", "x", "y", "z"]
        for i in range(1, 27):
            hashtable[i] = words[i - 1]
        while n >= 0:
            if s[n] == "#":
                ans = hashtable[int(int(s[n - 2]) * 10 + int(s[n - 1]))] + ans
                n = n - 3
            else:
                ans = hashtable[int(s[n])] + ans
                n = n - 1
        return ans