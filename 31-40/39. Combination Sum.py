class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def iter(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            iter(i, cur, total + candidates[i])

            cur.pop()
            iter(i + 1, cur, total)

        iter(0, [], 0)

        return res
