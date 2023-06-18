/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x<0)return false;
    let X = String(x);
    return X == X.split('').reverse().join('');
};