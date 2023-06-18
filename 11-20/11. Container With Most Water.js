/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    let length = height.length;
    let i = 0,
        j = length - 1;
    let maxArea = 0;
    while (i < j) {
        maxArea = Math.max(
            maxArea,
            Math.min(height[i], height[j]) * (j - i)
        );
        if (height[i] <= height[j]) {
            i++;
        } else {
            j--;
        }
    }
    return maxArea;
};
