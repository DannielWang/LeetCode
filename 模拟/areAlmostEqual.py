class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        conut = 0
        dict1 = collections.Counter(s1)
        dict2 = collections.Counter(s2)
        if dict1 != dict2:
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                conut += 1
        if conut <= 2:
            return True
        return False
