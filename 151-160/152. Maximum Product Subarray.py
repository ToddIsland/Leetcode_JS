class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(tmp, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)
        return res
