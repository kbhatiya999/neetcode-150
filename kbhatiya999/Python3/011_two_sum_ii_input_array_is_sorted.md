# Problem 11: Two Sum II - Input Array Is Sorted

## Problem Statement
Given an array of integers `numbers` that is sorted in **non-decreasing order**.

Return the indices (**1-indexed**) of two numbers, `[index1, index2]`, such that they add up to a given `target` number and `index1 < index2`. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be **exactly one valid solution**.

Your solution must use **O(1) additional space**.

## Constraints
- 2 <= numbers.length <= 1000
- -1000 <= numbers[i] <= 1000
- -1000 <= target <= 1000
- Tests are generated such that there is exactly one solution.

## Examples

### Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

### Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].
```

### Example 3:
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

## Approach

### Two-Pointer Method (Optimal)
Since the array is sorted, we can use two pointers starting from both ends:
1. Initialize left pointer at start (0) and right pointer at end (n-1)
2. Calculate sum of elements at both pointers
3. If sum equals target, return the 1-indexed positions
4. If sum is less than target, increment left pointer (need larger sum)
5. If sum is greater than target, decrement right pointer (need smaller sum)

**Time Complexity:** O(n) - Single pass with two pointers
**Space Complexity:** O(1) - Only using two pointers, no extra data structures

## LeetCode Problem
[Two Sum II - Input Array Is Sorted - LeetCode #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Solution Details

### Key Points:
- Array is guaranteed to be sorted in non-decreasing order
- Indices are 1-based, not 0-based
- Exactly one valid solution exists
- Must use O(1) additional space
- Cannot use the same element twice

### Why Two-Pointer Works:
- In a sorted array, if sum is too small, we need a larger number (move left pointer right)
- If sum is too large, we need a smaller number (move right pointer left)
- This property of sorted arrays allows us to solve in O(1) space and O(n) time

## Submission Status
- **Status:** Accepted
- **Runtime:** 4 ms (Beats 46.36%)
- **Memory:** 18.75 MB (Beats 8.07%)
- **Test Cases Passed:** 24/24
