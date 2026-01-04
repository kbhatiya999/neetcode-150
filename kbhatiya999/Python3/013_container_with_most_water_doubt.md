# FAQ / Doubts: Container With Most Water

## Q1: Why do we use two pointers instead of brute force?
**A:** Two pointer approach:
- Time: O(n)
- Space: O(1)
Brute force (checking all pairs):
- Time: O(n²)
- Space: O(1)
Two pointers is more efficient.

## Q2: Why do we move the pointer pointing to the smaller height?
**A:** The area formula is: `width * min(height[left], height[right])`
If we move the taller pointer:
- Width decreases
- min() is still limited by the shorter bar
- Area will definitely decrease
If we move the shorter pointer:
- Width decreases
- min() might increase (could find a taller bar)
- Area might increase, so we must check

## Q3: Why does moving the shorter pointer guarantee we won't miss the optimal solution?
**A:** Proof by contradiction:
- Suppose we have pointers at left and right
- Optimal solution has pointers at i and j where i < j
- If left < i, the max area with left as left-bound is at right
- If right > j, the max area with right as right-bound is at left
- By always moving the shorter pointer, we explore all meaningful positions

## Q4: What's the key insight of the two-pointer technique?
**A:** The area is limited by the shorter bar. Moving the taller pointer can never improve the area because:
1. Width decreases
2. The limiting bar is already the shorter one
Moving the shorter pointer gives a chance to find a taller bar.

## Q5: How do we know when to stop?
**A:** We stop when `left >= right` because:
- We've explored all possible pairs starting from opposite ends
- The two pointers have met or crossed

## Q6: Can we have duplicate heights?
**A:** Yes, the algorithm works with duplicates. Example:
- heights = [2,2,2]
- Area = (3-0) * min(2,2) = 6
No special handling needed.

## Q7: What if all heights are 0?
**A:** Area would be 0. The algorithm correctly returns 0.

## Q8: Edge cases to consider
- Array with 2 elements: we calculate area once
- All same heights: return (n-1) * height[0]
- Strictly increasing: answer is at edges
- Strictly decreasing: answer is at edges
