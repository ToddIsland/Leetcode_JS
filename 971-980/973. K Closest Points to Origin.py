class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[p[0] * p[0] + p[1] * p[1], p[0], p[1]] for p in points]
        heapq.heapify(points)
        res = []
        for i in range(k):
            val = heapq.heappop(points)
            res.append([val[1], val[2]])
        return res
