class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        # push index into q
        # monotonically decrease
        q = collections.deque()

        l = r = 0

        while r < len(nums):
            # pop elements smaller than nums[r]
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # move left end
            if l > q[0]:
                q.popleft()

            # record max val
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
