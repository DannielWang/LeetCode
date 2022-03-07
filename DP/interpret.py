class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == "(":
                if command[i+1] == ")":
                    ans = ans + "o"
                    i = i + 2
                    continue
                else:
                    ans = ans + "al"
                    i = i + 4
                    continue
            ans = ans + "G"
            i = i + 1
        return ans