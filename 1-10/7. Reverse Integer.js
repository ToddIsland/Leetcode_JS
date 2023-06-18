/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    const MIN = -(2 ** 31);
    const MAX = 2 ** 31 - 1;

    let str = String(x);
    let negative = false;
    if (str[0] == "-") {
        negative = true;
        str = str.slice(1);
    }
    let reversX = str.split("").reverse().join("");
    let ans = negative ? -Number(reversX) : Number(reversX);
    if (ans >= MAX || ans <= MIN) {
        return 0;
    } else {
        return ans;
    }
};
