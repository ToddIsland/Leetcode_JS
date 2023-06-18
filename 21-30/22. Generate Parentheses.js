/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    let ans = [];

    // number: remain char number
    // left: left bracket number
    // str: current string
    const iter = (number, left, str) => {
        if (number == 0) {
            if (left == 0) {
                ans.push(str);
            }
            return;
        }
        if (left == 0) {
            iter(number - 1, 1, str + "(");
        } else if (left < n) {
            iter(number - 1, left - 1, str + ")");
            iter(number - 1, left + 1, str + "(");
        } else {
            iter(number - 1, left - 1, str + ")");
        }
    };
    iter(n * 2, 0, "");
    return ans;
};

generateParenthesis(3);
