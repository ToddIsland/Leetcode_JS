/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1 = [1, 3], nums2 = [2]) {
    let ans = [];
    let i = 0,
        j = 0;
    while (i < nums1.length || j < nums2.length) {
        if (i == nums1.length) {
            ans = ans.concat(nums2.slice(j));
            break;
        }
        if (j == nums2.length) {
            ans = ans.concat(nums1.slice(i));
            break;
        }
        if (nums1[i] < nums2[j]) {
            ans.push(nums1[i]);
            i++;
        } else {
            ans.push(nums2[j]);
            j++;
        }
    }
    let len = ans.length;
    if (len % 2 == 0) {
        return (ans[len / 2 - 1] + ans[len / 2]) / 2;
    } else {
        return ans[len / 2 - 0.5];
    }
};
