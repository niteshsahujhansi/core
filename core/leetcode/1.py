nums = [3,2,4]
target = 6
Output: []
class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in nums:
                if i + j == target:
                    print(i)



Solution.twoSum(nums, target)