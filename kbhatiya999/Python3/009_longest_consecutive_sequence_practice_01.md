# Longest Consecutive Sequence - Practice

## Attempt 1

### Code
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Create a set for O(1) lookup
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # start of a sequence
            if num - 1 in num_set:
                continue
            
            current_num = num
            current_count = 1
            
            # Count Consecutive number
            while current_num + 1 in num_set:
                current_num += 1
                current_count += 1
            
            max_length = max(current_num, max_length)
        
        return max_length
```

### Issue
**Bug**: On line 20, comparing wrong variable with `max_length`

```python
max_length = max(current_num, max_length)  # WRONG!
```

**Problem**: 
- `current_num` is the **last number in the sequence**, not the length
- `max_length` is supposed to track the **length of the longest sequence**
- Example: For sequence [100, 4, 200, 1, 3, 2], when we find sequence [1,2,3,4]:
  - `current_num` = 4 (the last number)
  - `current_count` = 4 (the actual length)
  - `max_length = max(4, 200)` = 200 (comparing number 4 with previous max_length 200)
  - But we should be comparing the length (4) with max_length (200)

**Expected Output**: 4
**Actual Output**: 200 (Wrong!)

### Fix
Should use `current_count` (the length) instead of `current_num`:
```python
max_length = max(current_count, max_length)  # CORRECT
```

---

## Attempt 2

**Status**: TAccepted ✓

### Code
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Create a set for O(1) lookup
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # start of a sequence
            if num - 1 in num_set:
                continue
            
            current_num = num
            current_count = 1
            
            # Count Consecutive number
            while current_num + 1 in num_set:
                current_num += 1
                current_count += 1
            
            max_length = max(current_count, max_length)  # FIXED: Use current_count instead of current_num
        
        return max_length
```

### Fix Applied
**Line 20**: Changed from `max_length = max(current_num, max_length)` to `max_length = max(current_count, max_length)`

This correctly compares the length of the consecutive sequence (`current_count`) with the maximum length found so far, instead of comparing the last number in the sequence (`current_num`).

### Result
- **Status**: Accepted
- **Test Cases**: 84/84 passed
- **Runtime**: 56 ms (Beats 31.60%)
- **Memory**: 36.69 MB (Beats 50.01%)

### Complexity Analysis
- **Time Complexity**: O(n) - Each number is visited at most twice (once in the for loop, once in the while loop)
- **Space Complexity**: O(n) - For the set
