class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        minVal = max(piles) + 1

        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time <= h:
                minVal = min(minVal, mid)
                r = mid - 1
            elif time > h:
                l = mid + 1
        return minVal
