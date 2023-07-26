class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def iter(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            iter(i + 1)

            subset.pop()
            iter(i + 1)

        iter(0)

        return res
