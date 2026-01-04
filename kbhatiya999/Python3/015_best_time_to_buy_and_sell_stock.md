# Best Time to Buy and Sell Stock

## Problem Statement
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a `single day` to buy one stock and choosing a `different day in the future` to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Examples

### Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

### Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Solution Approach

The optimal approach uses a single pass through the array with a greedy strategy:

1. Track the minimum price seen so far (`min_price`)
2. For each price, calculate the profit if we sold at that price
3. Keep track of the maximum profit seen
4. Update the minimum price as we go

**Time Complexity:** O(n) - single pass through the array
**Space Complexity:** O(1) - only using constant extra space

## Key Points
- We must buy before we sell (buy index < sell index)
- We can choose to not make any transaction (profit = 0)
- The greedy approach works because we want to buy as low as possible and then sell as high as possible after that low point
