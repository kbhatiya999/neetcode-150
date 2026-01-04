# FAQ & Doubts: LeetCode 128 - Longest Consecutive Sequence

## Common Questions

### Q1: Why do we use a set instead of sorting the array?
**A:** Using a set gives us O(n) time complexity, while sorting would give us O(n log n). The key insight is that we don't need the elements to be in order; we only need to check if consecutive numbers exist.

### Q2: Why do we only start counting from the beginning of a sequence?
**A:** If we start counting from every number, we'd recount the same consecutive sequence multiple times. By checking if `num - 1` is in the set, we ensure we only start from the first number in each sequence.

### Q3: What happens with duplicate numbers in the array?
**A:** Duplicates are automatically handled when we convert to a set. Each unique number appears only once in the set.

### Q4: Why is this O(n) and not O(n²)?
**A:** Although we have nested loops (outer for each number, inner while for consecutive count), each number is visited at most twice across all iterations. The total work is still O(n).

### Q5: Can we use this approach if elements can be negative?
**A:** Yes! The algorithm works with negative numbers too. The set lookup is O(1) regardless of the value.

### Q6: What's the space complexity and why?
**A:** O(n) because we store all unique numbers in a set. In the worst case, all numbers are unique.

### Q7: What if the array is empty?
**A:** The algorithm returns 0, which is correct. An empty array has no consecutive sequence.

### Q8: Can we modify the array in-place to save space?
**A:** Not easily with this approach. You could use indices as a marking mechanism, but it would be more complex and not necessarily faster.

### Q9: How do we handle the case where all numbers form one sequence?
**A:** The algorithm naturally handles this. The max_length will be updated to the length of the entire sequence.

### Q10: What if we have numbers like [1, 1, 1, 1, 1]?
**A:** The set becomes {1}, and the longest consecutive sequence is [1] with length 1. Correct!

## Common Mistakes

### Mistake 1: Starting count from every number
```python
# WRONG - counts [1,2,3] three times
for num in num_set:
    current_num = num
    while current_num + 1 in num_set:
        current_num += 1
        current_length += 1
```

### Mistake 2: Not converting to set
```python
# INEFFICIENT - O(n²) due to 'in' operator on list
for num in nums:  # O(n)
    if num - 1 not in nums:  # O(n) - linear search in list
        ...
```

### Mistake 3: Not handling empty array
```python
# WRONG - will crash on empty array
num_set = set(nums)
for num in num_set:  # OK, but...
    # Missing check for empty set
```

## Edge Cases to Test

1. Empty array: `[]` → 0
2. Single element: `[5]` → 1
3. All duplicates: `[1, 1, 1, 1]` → 1
4. Consecutive sequence: `[1, 2, 3, 4, 5]` → 5
5. Non-consecutive: `[100, 200, 300]` → 1
6. Mixed order: `[5, 1, 3, 4, 2]` → 5
7. Negative numbers: `[-3, -1, -2, 0, 1]` → 5
8. Large gaps: `[1, 1000000]` → 1

## Optimization Tips

1. **Early termination:** If `max_length == len(num_set)`, you can break early
2. **Space-time tradeoff:** Use a different approach (like Union-Find) for different constraints
3. **Consider the problem constraints:** If numbers are in a small range, counting sort might be better

## Related Concepts

- **Union-Find:** Alternative approach with O(n α(n)) complexity
- **Hash Map:** Similar to set but can store additional metadata
- **Sorting:** O(n log n) alternative that's simpler to understand
- **Bit Set:** Space-efficient if numbers are in a known range
