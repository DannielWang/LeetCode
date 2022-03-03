class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        if num >= 1000:
            for i in range(int(num / 1000)):
                ans = ans + "M"
                num = num - 1000
        if num >= 900:
            ans = ans + "CM"
            num = num - 900
        if num >= 500:
            for i in range(int(num / 500)):
                ans = ans + "D"
                num = num - 500
        if num >= 400:
            ans = ans + "CD"
            num = num - 400
        if num >= 100:
            for i in range(int(num / 100)):
                ans = ans + "C"
                num = num - 100
        if num >= 90:
            ans = ans + "XC"
            num = num - 90
        if num >= 50:
            for i in range(int(num / 50)):
                ans = ans + "L"
                num = num - 50
        if num >= 40:
            ans = ans + "XL"
            num = num - 40
        if num >= 10:
            for i in range(int(num / 10)):
                ans = ans + "X"
                num = num - 10
        if num >= 9:
            ans = ans + "IX"
            num = num - 9
        if num >= 5:
            for i in range(int(num / 5)):
                ans = ans + "V"
                num = num - 5
        if num >= 4:
            ans = ans + "IV"
            num = num - 4
        for i in range(num):
            ans = ans + "I"
        return ans