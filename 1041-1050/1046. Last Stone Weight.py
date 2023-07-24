class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -1 * heapq.heappop(stones)
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 == s2:
                continue
            elif s1 < s2:
                heapq.heappush(stones, s1 - s2)
        return 0
            