# Trapping Rain Water

## Problem Statement
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples
### Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The bars [0,1] store 1 unit, [2,1] store 1 unit, [3,2,1,2,1] store 3 units.

### Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

## Constraints
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

## Solution Approach: Two Pointers

### Algorithm
1. Use two pointers from both ends of the array
2. Track max height from left and right sides
3. At each position, water trapped = max_height - current_bar_height
4. Move the pointer with smaller height inward

### Why Two Pointers?
- Water at any position is determined by min(left_max, right_max)
- Move the side with smaller max height first

### Time Complexity: O(n)
### Space Complexity: O(1)
