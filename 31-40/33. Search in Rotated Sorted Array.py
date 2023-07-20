class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            # left portion
            # equal is for one element case
            if nums[mid] >= nums[l]:
                # out of range [l, mid]
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right portion
            else:
                # out of range [mid, r]
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
