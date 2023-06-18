/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
// two pointers
var fourSum = function (nums, target) {
    const kSum = (nums, target, k) => {
        let res = [];
        let len = nums.length;
        if (!nums.length) return res;
        if (target < nums[0] * k || target > nums[len - 1] * k) return res;
        if (k == 2) return twoSum(nums, target);
        for (let i = 0; i < len; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            let sets = kSum(nums.slice(i + 1), target - nums[i], k - 1);
            for (let j = 0; j < sets.length; j++) {
                res.push([nums[i], ...sets[j]]);
            }
        }
        return res;
    };

    const twoSum = (nums, target) => {
        let ans = [];
        let len = nums.length;
        let i = 0,
            j = len - 1;
        while (i < j) {
            let sum = nums[i] + nums[j];
            // problem is here
            if (sum == target) {
                ans.push([nums[i], nums[j]]);
                while (i < j && nums[i] == nums[i + 1]) i++;
                while (i < j && nums[j] == nums[j - 1]) j--;
                i++;
                j--;
            } else if (sum < target) {
                i++;
            } else if (sum > target) {
                j--;
            }
        }
        return ans;
    };
    nums.sort((a, b) => a - b);
    let ans = kSum(nums, target, 4);
    return ans;
};

// Hash Set
var fourSum = function (nums, target) {
    const kSum = (nums, target, k) => {
        let res = [];
        let len = nums.length;
        if (!nums.length) return res;
        if (target < nums[0] * k || target > nums[len - 1] * k) return res;
        if (k == 2) return twoSum(nums, target);
        for (let i = 0; i < len; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            let sets = kSum(nums.slice(i + 1), target - nums[i], k - 1);
            for (let j = 0; j < sets.length; j++) {
                res.push([nums[i], ...sets[j]]);
            }
        }
        return res;
    };

    const twoSum = (nums, target) => {
        let ans = [];
        let s = new Set();
        let len = nums.length;
        for (let i = 0; i < len; i++) {
            if (
                (ans.length == 0 || ans[ans.length - 1][1] != nums[i]) &&
                s.has(target - nums[i])
            ) {
                ans.push([target - nums[i], nums[i]]);
            }
            s.add(nums[i]);
        }
        return ans;
    };
    nums.sort((a, b) => a - b);
    let ans = kSum(nums, target, 4);
    return ans;
};
