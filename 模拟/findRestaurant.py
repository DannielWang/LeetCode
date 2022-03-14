class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = defaultdict(list)
        for char in set(list1) & set(list2):
            res[list1.index(char) + list2.index(char)].append(char)
        return sorted(res.items(),key=lambda x: x[0])[0][1]
