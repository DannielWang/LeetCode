class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - nums[i] in nums:
                return [hashtable[target - num[i]], i]
            hashtable[num] = i
        return []
