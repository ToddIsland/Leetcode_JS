class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def iter(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or sum > target:
                return

            subset.append(candidates[i])
            iter(i + 1, sum + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            iter(i + 1, sum)

        iter(0, 0)

        return res
