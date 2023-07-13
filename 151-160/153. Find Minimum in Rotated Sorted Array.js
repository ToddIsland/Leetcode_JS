/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    let min = nums[0];
    let len = nums.length;
    let left = 0, right = len - 1;
    while(left < right){
        let mid = left + Math.floor((right-left+1)/2);
        if(nums[mid]>min){
            left = mid;
        }
        else{
            right = mid - 1;
            min = nums[mid];
        }
    }
    return min;
};
