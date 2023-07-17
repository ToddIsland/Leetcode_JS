class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in map:
                return [map[remain], i]
            else:
                map[nums[i]] = i
