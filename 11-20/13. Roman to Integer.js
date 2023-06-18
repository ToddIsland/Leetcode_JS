/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    let translation = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };
    let ans = 0;
    s = s.replace("IV", "IIII").replace("IX", "VIIII");
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX");
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC");
    for (let i = 0; i < s.length; i++) {
        ans += translation[s[i]];
    }
    return ans;
};
