# LeetCode 217: Contains Duplicate

## Problem Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```

### Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```

### Example 3:
```
Input: nums = [1,1,3,3,4,3,2,4,2]
Output: true
```

## Solution Approach

### Approach: Using a Set
We use a set to track numbers we've already seen. As we iterate through the array:
1. If we encounter a number that's already in the set, we found a duplicate
2. Otherwise, we add the number to the set
3. If we complete the loop without finding duplicates, return False

### Complexity Analysis
- **Time Complexity**: O(n) - We iterate through the array once
- **Space Complexity**: O(min(n, m)) - Where m is the number of unique elements, at most O(n) space for the set

## Implementation

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Detect if the array contains duplicate elements.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## Alternative Approaches

### 1. Sorting Approach
Sort the array and check adjacent elements:
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
```
- Time Complexity: O(n log n)
- Space Complexity: O(1) or O(n) depending on sorting algorithm

### 2. HashSet (Dictionary/Frequency Map)
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```
- Time Complexity: O(n)
- Space Complexity: O(n)

## Key Insights

1. **HashSet is optimal** - O(n) time complexity with straightforward logic
2. **Duplicates detection** - If set size < array size, duplicates exist
3. **Early termination** - Our solution returns True immediately upon finding first duplicate
4. **Space-Time Tradeoff** - Using extra space (set) saves time vs sorting approach

## Submission Details

- **Status**: ✅ Accepted
- **Testcases Passed**: 77 / 77
- **Runtime**: 16 ms (Beats 44.41%)
- **Memory**: 31.63 MB (Beats 29.43%)
- **Language**: Python3
- **Date**: December 4, 2025

## Related Problems

- LeetCode 217: Contains Duplicate
- LeetCode 219: Contains Duplicate II
- LeetCode 220: Contains Duplicate III
- LeetCode 1: Two Sum

## Tags

`#array` `#hash-table` `#set` `#easy`
