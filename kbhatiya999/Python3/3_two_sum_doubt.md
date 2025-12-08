# Doubts and Questions: Two Sum (LeetCode 1)

## Common Questions and Clarifications

### 1. Why do we need a hash map? Can't we just use a sorted array?

**Question:** If we sort the array and use two pointers, wouldn't that work?

**Answer:** Yes, it would work, but it has drawbacks:
- Sorting takes O(n log n) time, while hash map takes O(n)
- We need to track original indices, which adds complexity with sorting
- Hash map is optimal for this problem

**Comparison:**
```python
# Hash Map (Optimal) - O(n) time
for i, num in enumerate(nums):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i

# Sorted Two Pointers - O(n log n) time
# Plus complexity of maintaining original indices
```

---

### 2. What does the hash map store? Why store index?

**Question:** Why not just store whether we've seen a number?

**Answer:** We need both value AND index because:
- We need to return the indices, not just the values
- Multiple instances of the same value might exist
- We need to know WHERE we saw it

**Example:**
```
nums = [1, 2, 3, 4, 2]
target = 4

When we reach the last 2 (index 4):
- complement = 4 - 2 = 2
- We need to return [1, 4] (the indices)
- Hash map has {1: 0, 2: 1, 3: 2, 4: 3}
- We return [seen[2], 4] = [1, 4]
```

---

### 3. Why don't we store the current number before checking?

**Question:** Why check for complement BEFORE storing the current number?

**Answer:** This is crucial for avoiding using the same element twice:
```python
WRONG:
for i, num in enumerate(nums):
    seen[num] = i  # Store first
    if target - num in seen:  # Then check
        return [seen[target - num], i]  # Could be wrong!

CORRECT:
for i, num in enumerate(nums):
    if target - num in seen:  # Check first
        return [seen[target - num], i]  # Safe!
    seen[num] = i  # Then store
```

**Example of the problem:**
```
nums = [3], target = 6

WRONG approach:
- i=0, num=3
- Store: seen[3] = 0
- Check: 6 - 3 = 3 in seen? YES!
- Return [seen[3], 0] = [0, 0] ← WRONG! Using same element twice

CORRECT approach:
- i=0, num=3
- Check: 6 - 3 = 3 in seen? NO (not yet stored)
- Store: seen[3] = 0
- No pair found (correct, can't use same element twice)
```

---

### 4. What if the same number appears twice?

**Question:** nums = [3, 3], target = 6. How does it work?

**Answer:** Perfect scenario for the hash map:
```python
- i=0, num=3
  - Check: 6 - 3 = 3 in seen? NO
  - Store: seen[3] = 0

- i=1, num=3
  - Check: 6 - 3 = 3 in seen? YES! (from index 0)
  - Return [seen[3], 1] = [0, 1] ✓
```

This is elegant! We don't need special handling.

---

### 5. Why doesn't it work with negative numbers?

**Question:** Does the algorithm handle negative numbers?

**Answer:** YES! The complement approach works perfectly:
```python
nums = [-1, -2, -3, 5, 6], target = 4

- i=0, num=-1
  - complement = 4 - (-1) = 5
  - 5 not in seen, store: seen[-1] = 0

- i=1, num=-2
  - complement = 4 - (-2) = 6
  - 6 not in seen, store: seen[-2] = 1

- i=2, num=-3
  - complement = 4 - (-3) = 7
  - 7 not in seen, store: seen[-3] = 2

- i=3, num=5
  - complement = 4 - 5 = -1
  - -1 in seen? YES! (from index 0)
  - Return [seen[-1], 3] = [0, 3]
  - Verify: nums[0] + nums[3] = -1 + 5 = 4 ✓
```

---

### 6. What's the space complexity exactly?

**Question:** Is it O(n) space for the hash map?

**Answer:** Technically O(min(n, m)) where:
- n = number of elements
- m = number of unique elements

But in worst case (all unique), it's O(n).

For the Two Sum problem specifically: **O(n)**

---

### 7. Can we solve it without extra space?

**Question:** Is there an O(1) space solution?

**Answer:** For finding indices, NO. But for just checking if a pair exists:
```python
# Two pointer approach (requires sorting)
nums.sort()  # O(n log n) time
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        return True  # Only checking existence, not indices
    elif total < target:
        left += 1
    else:
        right -= 1
return False
```

But this:
- Doesn't return indices
- Takes O(n log n) time
- Only saves space if we don't need indices

---

### 8. How do we know a solution exists?

**Question:** What if no two numbers add up to target?

**Answer:** The problem guarantees exactly one solution exists. But if we wanted to handle no solution:
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []  # No solution found
```

---

### 9. Does order of return matter?

**Question:** Can we return [i, j] where i > j?

**Answer:** The problem says "you can return the answer in any order", so both [0, 1] and [1, 0] are valid.

Our solution naturally returns in order because we check earlier elements first.

---

### 10. Why use enumerate() instead of range(len()?)?

**Question:** Is `enumerate` just style preference?

**Answer:** It's more than style:
```python
# Using enumerate (Pythonic)
for i, num in enumerate(nums):
    ...

# Using range (Less clean)
for i in range(len(nums)):
    num = nums[i]
    ...

# Why enumerate?
- More readable
- Slightly more efficient
- Works with any iterable
- No risk of index out of bounds
```

---

## Key Takeaways

1. **Hash Map is optimal** - O(n) time, required for indices
2. **Store before checking** - Avoid... wait, check BEFORE store
3. **Works with all numbers** - Positive, negative, duplicates
4. **Single pass efficient** - Don't sort or preprocess
5. **Index matters** - That's why we can't just use a set
6. **Complement approach** - The core insight of the solution
