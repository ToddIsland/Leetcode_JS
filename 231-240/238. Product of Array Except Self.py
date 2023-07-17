class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMulti = 1
        rightMulti = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = leftMulti
            leftMulti *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightMulti
            rightMulti *= nums[i]

        return res
