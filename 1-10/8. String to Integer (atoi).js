/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
    const MIN = -(2 ** 31);
    const MAX = 2 ** 31 - 1;
    let sign = 1,
        base = 0,
        i = 0;
    while (s[i] == " ") i++;
    if (s[i] == "-") {
        sign = -1;
        i++;
    }
    else if(s[i] == "+"){
        i++;
    }
    console.log('s',s);
    while(s[i] >= '0' && s[i] <= '9') {
        // very important: if dont use braket, it will become string first
        base = base * 10 + (s[i] - '0');
        i++;
    }
    base = base * sign;
    if(base > MAX) return MAX;
    else if(base < MIN) return MIN;
    else return base;
};
