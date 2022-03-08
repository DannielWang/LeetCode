class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                ch = chr(ord(ch) | 32)
            ans = ans + ch
        return ans