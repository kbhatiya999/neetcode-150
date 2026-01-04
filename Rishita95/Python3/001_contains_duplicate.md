# LeetCode 217: Contains Duplicate

## Problem
[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1
- Input: `nums = [1, 2, 3, 3]`
- Output: `true`

### Example 2
- Input: `nums = [1, 2, 3, 4]`
- Output: `false`

### Example 3
- Input: `nums = [1, 1]`
- Output: `true`

## Solution Approach

The most efficient approach is to use a **Hash Set**:

1. Create an empty set to track seen numbers
2. Iterate through the array
3. For each number, check if it's already in the set
4. If found, return `true` (duplicate exists)
5. If not found, add it to the set
6. If we finish the loop without finding duplicates, return `false`

**Why this approach was chosen:**
- Hash Set provides O(1) average time complexity for lookups and insertions
- Simple and intuitive logic
- Optimal for this problem's constraints

## Complexity Analysis

- **Time Complexity**: O(n) - We iterate through the array once, and each set operation (add, lookup) is O(1)
- **Space Complexity**: O(n) - In the worst case (no duplicates), we store all n elements in the set

## Implementation

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Detect if array contains duplicates using a hash set.
        
        Approach:
        - Track seen numbers in a set
        - Return True if we encounter a number already in the set
        - Return False if we finish the loop (no duplicates)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## Alternative Approaches

### Approach 1: Sorting
- Sort the array: O(n log n) time, O(1) or O(n) space (depending on sorting algorithm)
- Check adjacent elements for duplicates
- Pros: No extra space (space complexity O(1) with in-place sort)
- Cons: Slower due to sorting overhead

### Approach 2: Brute Force
- Nested loops to compare every pair: O(n^2) time
- Pros: No extra space
- Cons: Very slow for large inputs

## Key Insights

- Set-based approach is the best balance between time and space complexity
- We can return immediately upon finding the first duplicate (no need to check the entire array)
- The problem asks for existence of duplicate, not counting duplicates or their positions
- Edge cases: Single element (always false), Two elements same (true), Empty array (problem states n >= 1)

## Submission Details

- **Status**: ✅ Accepted
- **Runtime**: 416 ms (Beats 87.63% of Python3 submissions)
- **Memory**: 19.1 MB (Beats 66.22% of Python3 submissions)
- **Date**: 12/04/2025

## Related Problems

- [LeetCode 1: Two Sum](https://leetcode.com/problems/two-sum/) - Uses similar hash set technique
- [LeetCode 219: Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) - Extended version with index constraint
- [LeetCode 220: Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) - Extended version with value constraint

## Tags

**Array**, **Hash Table**, **Sorting**
