/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    let n = s.length;
    let ans = [0, 0];
    let dp = new Array(n);
    for (let i = 0; i < n; i++) {
        dp[i] = new Array(n).fill(false);
        dp[i][i] = true;
    }
    // iterate all pairs
    for (let i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            ans = [i, i+1];
        }
    }
    // populate dp table
    for (let diff = 2; diff <= n - 1; diff++) {
        for (let i = 0; i <= n - diff; i++) {
            let j = i + diff;
            if (s[i] == s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                ans = [i, j];
            }
        }
    }
    return s.slice(ans[0], ans[1] + 1);
};
