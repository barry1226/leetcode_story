class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, value in enumerate(nums):
            if value in dic.keys():
                return [dic[value], index]
            dic[target - value] = index
