class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ''
        if num == 0:
            return "0"
        while num:
            if int(num % 7) == 0:
                ans = str(abs(num) % 7) + ans
                num = int(num / 7)
                continue
            if int(num / 7) == 0:
                ans = str(num) + ans
                num = int(num / 7)
                continue
            else:
                res = str(abs(num) % 7)
                num = int(num / 7)
                ans = res + ans
                continue
        return ans