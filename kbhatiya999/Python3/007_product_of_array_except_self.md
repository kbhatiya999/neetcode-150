# Problem 7: Product of Array Except Self

## LeetCode Link
[LeetCode 238: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## Problem Statement

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all elements except `nums[i]`.

**Important:** Must solve in O(n) time without using the division operation.

## Examples

### Example 1
- **Input:** `nums = [1,2,4,6]`
- **Output:** `[48,24,12,8]`
- **Explanation:** For index 0: 2×4×6=48, For index 1: 1×4×6=24, etc.

### Example 2
- **Input:** `nums = [-1,0,1,2,3]`
- **Output:** `[0,-6,0,0,0]`
- **Explanation:** The zero at index 1 makes many products zero.

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- All elements are guaranteed to fit in a 32-bit integer

## Solution Approach: Prefix and Postfix Products

### Key Insight
Instead of computing the total product and dividing, we can:
1. Build a prefix product array (product of all elements to the left)
2. Build a postfix product array (product of all elements to the right)
3. Multiply prefix × postfix for each position

### Algorithm Steps
1. **First Pass (Left-to-Right):** 
   - `output[i]` = product of all elements to the left of `i`
   - Start with prefix = 1
   - For each element, store current prefix, then update prefix

2. **Second Pass (Right-to-Left):**
   - Multiply `output[i]` by the product of all elements to the right
   - Start with suffix = 1
   - For each element, multiply by suffix, then update suffix

### Visual Example
```
Input: [1, 2, 4, 6]

First Pass (Prefix):
output = [1, 1, 2, 8]
(left of each element)

Second Pass (Suffix):
output = [1×48, 1×24, 2×12, 8×1]
       = [48, 24, 24, 8]
```

## Implementation

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # First pass: prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Second pass: multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
```

## Complexity Analysis

| Metric | Complexity | Notes |
|--------|-----------|-------|
| **Time** | O(n) | Two linear passes through array |
| **Space** | O(1) | Only output array (not counting result) |

## Submission Details

- **Status:** ✅ Accepted
- **Date:** January 4, 2026
- **Runtime:** 21 ms (Beats 69.27% of Python3 submissions)
- **Memory:** 23.44 MB (Beats 48.53% of Python3 submissions)
- **Test Cases Passed:** 24 / 24

## Key Insights

1. **No Division Needed:** By using prefix/suffix, we avoid division completely
2. **Space Efficient:** Uses O(1) extra space (output array doesn't count)
3. **Two-Pass Strategy:** Elegant solution splitting the problem into manageable parts
4. **Handles Zeros:** Works correctly even with zero values in array
5. **Negative Numbers:** Works with negative integers as well

## Related Problems

- [LeetCode 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [LeetCode 152: Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [LeetCode 238: Product of Array Except Self (Duplicate Check)](https://leetcode.com/problems/product-of-array-except-self/)

## Tags
- Array
- Prefix Sum
- Dynamic Programming
