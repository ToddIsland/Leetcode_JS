class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # remember to sort
        nums.sort()

        def iter(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            iter(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            iter(i + 1)

        iter(0)
        return res
