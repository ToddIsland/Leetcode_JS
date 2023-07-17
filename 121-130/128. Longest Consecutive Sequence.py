from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums.sort()
        maxNum = 0
        curMax = 1
        for i in range(len(nums)):
            if i == 0:
                continue

            if nums[i] - nums[i - 1] == 1:
                curMax += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                maxNum = max(maxNum, curMax)
                curMax = 1
        
        maxNum = max(maxNum, curMax)

        return maxNum