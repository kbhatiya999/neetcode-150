# 3Sum

## Problem Statement
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

### Example 2:
Input: nums = [0]
Output: []

### Example 3:
Input: nums = [0,0,0,0]
Output: [[0,0,0]]

## Constraints
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Solution Approach

### Algorithm
1. Sort the array first
2. Use a nested loop approach:
   - Fix one element (i) and find two elements using two-pointer technique for remaining part
   - For each fixed element, use left and right pointers to find pairs that sum to -nums[i]
3. Skip duplicates to avoid duplicate triplets in result

### Time Complexity: O(n²)
### Space Complexity: O(1) or O(n) depending on sorting algorithm

## Key Points
- Sort the array to handle duplicates easily and use two-pointer technique
- When nums[i] > 0, no solution exists (since all elements after are also > 0)
- Skip duplicate elements at different loop positions
- Two-pointer technique is crucial for achieving O(n²) time complexity
