# LeetCode 1: Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## Examples

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Approach

### Hash Map (Single Pass) - Optimal Solution

The key insight is to use a hash map to store previously seen numbers and their indices. As we iterate through the array, for each number, we calculate the complement (target - current number) and check if it exists in our hash map.

**Algorithm:**
1. Create an empty hash map to store `value: index` pairs
2. Iterate through the array with index
3. For each number, calculate complement = target - number
4. If complement exists in hash map, return the indices
5. Otherwise, store the current number and its index in the hash map
6. Continue to the next number

**Time Complexity:** O(n) - single pass through the array
**Space Complexity:** O(n) - hash map stores up to n elements

## Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store value: index pairs
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in our hash map, we found our pair
            if complement in seen:
                return [seen[complement], i]
            
            # Store the current number and its index
            seen[num] = i
        
        # No solution found (should not happen based on problem constraints)
        return []
```

## Alternative Solutions

### 1. Brute Force (Two Nested Loops)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```
**Time Complexity:** O(n²) - nested loops
**Space Complexity:** O(1) - no extra space

### 2. Sorting with Two Pointers
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create array of (value, original_index) tuples
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Sort by value
        indexed_nums.sort()
        
        left, right = 0, len(indexed_nums) - 1
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
```
**Time Complexity:** O(n log n) - due to sorting
**Space Complexity:** O(n) - for indexed array

## Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Map | O(n) | O(n) | **Optimal** - single pass, linear time |
| Brute Force | O(n²) | O(1) | Simple but inefficient |
| Two Pointers | O(n log n) | O(n) | Requires sorting |

## Key Insights

1. **Use complement approach** - Instead of checking all pairs, calculate what number we need
2. **Hash map for O(1) lookups** - Checking if complement exists is constant time
3. **Single pass sufficient** - We don't need to pre-process or sort the array
4. **Early termination** - As soon as we find the pair, we return
5. **No duplicate numbers** - Each element can only be used once, but we're using indices anyway

## Edge Cases

1. **Minimum array size:** [2, 7] with target 9 → [0, 1]
2. **Negative numbers:** [-1, -2, -3, 5, 6] with target 0 → [-1, 1] (if they exist)
3. **Large numbers:** Ensure overflow/underflow isn't an issue (Python handles this)
4. **Same number twice:** [3, 3] with target 6 → [0, 1]
5. **Zero in array:** [0, 0, 3, 4] with target 0 → [0, 1]

## Related Problems

- LeetCode 15: 3Sum
- LeetCode 16: 3Sum Closest
- LeetCode 18: 4Sum
- LeetCode 167: Two Sum II - Input Array Is Sorted
- LeetCode 1099: Two Sum Less Than K
