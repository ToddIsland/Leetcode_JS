class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()

        for interval in intervals:
            if not res:
                res.append(interval)
                continue

            cur = res[-1]
            if interval[0] >= cur[0] and interval[0] <= cur[1]:
                res.pop()
                res.append([min(cur[0], interval[0]), max(cur[1], interval[1])])
            else:
                res.append(interval)

        return res
