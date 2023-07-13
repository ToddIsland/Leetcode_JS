/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    let result = nums[0];
    let preMax = nums[0];
    let preMin = nums[0];

    for (let i = 1; i < nums.length; i++) {
        let curMax = Math.max(nums[i]*preMax, nums[i]*preMin, nums[i]);
        let curMin = Math.min(nums[i]*preMax, nums[i]*preMin, nums[i]);

        preMax = curMax;
        preMin = curMin;

        result = Math.max(result, preMax);
    }
    
    return result;
};
