/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let len = nums.length;
    let left = 0,
        right = len - 1;

    while (left < right) {
        let mid = left + Math.floor((right - left + 1) / 2);
        if(nums[mid] == target) return mid;
        // left side is sorted
        if (nums[left] < nums[mid]) {
            if (nums[left] <= target && target <= nums[mid]) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        // right side is sorted
        else {
            // target can equal to nums value
            if (nums[mid] <= target && target <= nums[right]) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
    }

    return nums[left] == target ? left : -1;
};
