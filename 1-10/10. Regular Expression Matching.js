/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
    if (p == null || p.length == 0) return s == null || s.length == 0;
    let lens = s.length;
    let lenp = p.length;
    let dp = [];
    for (let i = 0; i <= lens; i++) {
        dp[i] = new Array(lenp + 1).fill(false);
    }
    dp[0][0] = true;
    for (let j = 1; j <= lenp; j++) {
        dp[0][j] = p[j - 1] == "*" && dp[0][j - 2];
    }

    for (let j = 1; j <= lenp; j++) {
        for (let i = 1; i <= lens; i++) {
            if (p[j - 1] == s[i - 1] || p[j - 1] == ".") {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] == "*") {
                dp[i][j] =
                    dp[i][j - 2] ||
                    ((s[i - 1] == p[j - 2] || p[j - 2] == ".") && dp[i - 1][j]);
            }
        }
    }
    return dp[lens][lenp];
};