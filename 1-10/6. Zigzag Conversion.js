/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
    let n = s.length;
    let width = Math.ceil(n / 2);
    if (numRows == 1) return s;

    let times = -1;
    const direct = [
        [1, 0],
        [-1, 1],
    ];

    let zig = new Array(numRows);
    for (let i = 0; i < numRows; i++) {
        zig[i] = new Array(width);
    }

    let m = 0,
        i = 0,
        j = 0,
        x = 1,
        y = 0;
    while (m < n) {
        if (i == 0 || i == numRows - 1) {
            times++;
            [x, y] = direct[times % 2];
        }
        zig[i][j] = s[m];
        i += x;
        j += y;
        m++;
    }
    let ans = [];
    for(let a = 0; a<numRows;a++){
        for(let b =0;b<=j;b++){
            if(zig[a][b])ans.push(zig[a][b]);
        }
    }
    return ans.join('');
};
