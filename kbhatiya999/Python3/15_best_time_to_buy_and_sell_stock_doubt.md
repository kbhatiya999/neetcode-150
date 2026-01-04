# FAQ / Doubts: Best Time to Buy and Sell Stock

## Q1: Why use a greedy approach?
**A:** The greedy approach works because:
- To maximize profit, we want to buy at the lowest price and sell at the highest price after that point
- As we traverse the array, we keep track of the minimum price seen so far
- For each new price, we calculate the profit if we sold at that price, using the minimum price so far
- This guarantees we find the optimal buy-sell pair with just one pass

## Q2: What if prices are strictly decreasing?
**A:** If prices only decrease, there's no profitable transaction possible, so we return 0. The algorithm handles this correctly because:
- `max_profit` starts at 0
- Each new price would be less than `min_price`, resulting in negative profit
- `max()` ensures negative profits don't update `max_profit`
- Final answer remains 0

## Q3: Can we buy and sell on the same day?
**A:** No. The problem requires:
- "a single day to buy... and a different day in the future to sell"
- Our algorithm enforces this by only calculating profit for prices after the minimum

## Q4: What is the time complexity?
**A:** O(n) where n is the length of prices array
- Single pass through the array
- Constant operations in each iteration (comparison and assignment)
- No nested loops or recursive calls

## Q5: What is the space complexity?
**A:** O(1) - constant space
- Only two variables: `min_price` and `max_profit`
- Regardless of input size, space usage remains constant

## Q6: Why not use a two-pointer approach?
**A:** A two-pointer approach would be less efficient:
- Two pointers would require nested comparisons or backward traversal
- Would be O(n²) in worst case (comparing all pairs)
- Single pass greedy is O(n) and is optimal

## Q7: What if there are negative prices?
**A:** Based on constraints, prices are >= 0, so this won't occur. But if it did:
- Algorithm would still work correctly
- Minimum would be the most negative value
- Profit calculation would still be accurate

## Q8: Can this problem have multiple correct answers?
**A:** Yes, in terms of which days to buy/sell:
- Example: [1, 2, 3, 4, 5] could buy on day 1 and sell on day 5 OR buy on day 4 and sell on day 5 (both profit 4)
- But there's only ONE maximum profit value
- Our algorithm correctly returns the maximum profit value, not the specific days
