/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let leftMulti = 1;
    let rightMulti = 1;
    let res = [];

    for(let i = 0; i <nums.length;i++){
        res[i] = leftMulti;
        leftMulti *= nums[i];
    }

    for(let i = nums.length-1;i>=0;i--){
        res[i] *= rightMulti;
        rightMulti *= nums[i];
    }
    return res;
};