/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
  let left = 0,
    right = s.length - 1;
  while (left <= right) {
    if (s[left] == s[right]) {
      left++;
      right--;
    } else {
      return (
        isPalindorme(s, left + 1, right) || isPalindorme(s, left, right - 1)
      );
    }
  }
  return true;
};

function isPalindorme(s, left, right) {
  while (left <= right) {
    if (s[left] == s[right]) {
      left++;
      right--;
    } else {
      return false;
    }
  }
  return true;
}
