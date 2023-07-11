/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min = prices[0],
    profit = 0;

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < min) min = prices[i];

    profit = prices[i] - min > profit ? prices[i] - min : profit;
  }
  return profit;
};
