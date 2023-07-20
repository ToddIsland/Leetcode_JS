class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]
        minVal = first

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= first:
                l = mid + 1
            elif nums[mid] < first:
                r = mid - 1
                minVal = min(minVal, nums[mid])

        return minVal
