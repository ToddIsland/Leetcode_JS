/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let l = 0,
        r = 0,
        ans = 0;
    let n = s.length;
    let map = new Array(256).fill(-1);
    while (r < n) {
        if (map[s.charCodeAt(r)] != -1) {
            l = Math.max(map[s.charCodeAt(r)] + 1, l);
        }
        map[s.charCodeAt(r)] = r;
        ans = Math.max(ans, r - l + 1);
        r++;
    }
    return ans;
};
