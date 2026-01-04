# Container With Most Water

## Problem Statement
You are given an integer array `height` where `height[i]` represents the height of the ith bar. You may choose any two bars to form a container such that the container contains the most water.

Return the maximum amount of water a container can store.

## Examples

### Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2:
Input: height = [1,1]
Output: 1

## Constraints
- 2 <= height.length <= 10^5
- 0 <= height[i] <= 10^4

## Solution Approach

### Algorithm: Two Pointers
1. Initialize left pointer at start and right pointer at end
2. Calculate area with current pointers: width * min(height[left], height[right])
3. Move the pointer pointing to smaller height inward (because height is limited by shorter bar)
4. Keep track of maximum area found

### Why move the shorter pointer?
The area is determined by: `(right - left) * min(height[left], height[right])`
If we move the taller pointer:
- Width decreases
- Height is still limited by the shorter bar
- Area will definitely decrease

If we move the shorter pointer:
- Width decreases
- Height might increase (since we're moving away from the current shorter bar)
- Area might increase, and we must check it

### Time Complexity: O(n)
### Space Complexity: O(1)
