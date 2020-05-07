class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i,value in enumerate(nums):
            if target-value in dict:
                return dict[target-value],i
            else:
                dict[value] = i 
