/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
// 100
// 011
// 111(xor)

// 001
// 101
// 001(and)
// 010(<<)
var getSum = function (a, b) {
  while ((a & b) != 0) {
    let carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }
  return a ^ b;
};
