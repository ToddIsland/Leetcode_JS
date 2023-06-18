/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
    if (digits.length == 0) return [];
    let map = [
        [],
        [],
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"],
    ];

    let ans = [];
    let len = digits.length;
    //DFS
    const iter = (str, index) => {
        if (index == len) {
            ans.push(str);
            return;
        }

        let current = digits[index] - "0";
        let chars = map[current];
        for (let i = 0; i < chars.length; i++) {
            iter(str + chars[i], index + 1);
        }
    };

    iter("", 0);
    return ans;
};

letterCombinations("23");
