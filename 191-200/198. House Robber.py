class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        r1, r2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(nums[i] + r1, r2)
            r1 = r2
            r2 = temp

        return r2
