class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low < high:
            mid = low + (high - low + 1) // 2
            if matrix[mid][0] < target:
                low = mid
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                return True

        l, r = 0, len(matrix[0]) - 1

        while l < r:
            mid = l + (r - l + 1) // 2
            if matrix[low][mid] < target:
                l = mid
            elif matrix[low][mid] > target:
                r = mid - 1
            else:
                return True

        return True if matrix[low][l] == target else False
