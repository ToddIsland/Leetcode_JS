/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
    nums.sort((a, b) => a - b);

    let diff = 100000;
    let ans;

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        let j = i + 1;
        let k = nums.length - 1;

        while (j < k) {
            let sum = nums[i] + nums[j] + nums[k];
            if (sum == target) {
                return sum;
            } else if (sum > target) {
                k--;
            } else {
                j++;
            }
            if (diff > Math.abs(sum-target)){
                diff = Math.abs(sum-target);
                ans = sum;
            }
        }
    }
    return ans;
};
