# Two Sum II - Input Array Is Sorted - FAQs & Doubts

## Frequently Asked Questions

### Q1: Why do we return 1-indexed instead of 0-indexed?
**A:** This is LeetCode's specific requirement for this problem. The problem statement explicitly states "Return the indices (1-indexed)". Always check the problem requirements carefully.

### Q2: Why is the two-pointer approach optimal for sorted arrays?
**A:** In a sorted array:
- If the sum is too small, all smaller numbers won't help (they're on the left)
- We need a larger number, which exists only to the right
- If the sum is too large, all larger numbers won't help (they're on the right)
- We need a smaller number, which exists only to the left

This property allows us to eliminate elements without revisiting them, giving O(n) time and O(1) space.

### Q3: Can we use a hash map approach like Two Sum I?
**A:** Yes, we could use a hash map (O(n) time, O(n) space), but the problem specifically requires O(1) additional space. The two-pointer approach satisfies this constraint.

### Q4: What if there are duplicate numbers in the array?
**A:** The two-pointer approach still works correctly. We just move the pointers based on the sum comparison, not based on duplicates. Duplicates don't affect the logic.

### Q5: Can both pointers point to the same element?
**A:** No. The problem states "index1 and index2 cannot be equal". Our algorithm naturally prevents this because:
- We start with left = 0 and right = n-1
- We only stop when left == right (which won't happen because exactly one solution exists)
- If we reach the condition where left == right, we would have already found the solution

### Q6: What if the array has only 2 elements?
**A:** The algorithm works fine. We calculate the sum and check if it equals the target. If yes, return [1, 2]. This is a valid edge case.

### Q7: Can negative numbers be in the array?
**A:** Yes, the constraints say -1000 <= numbers[i] <= 1000. Negative numbers don't affect the two-pointer logic because the array is sorted in non-decreasing order.

### Q8: Is the solution guaranteed to exist?
**A:** Yes, the problem states "There will always be exactly one valid solution". We don't need to handle cases where no solution exists.

### Q9: Why do we use left < right instead of left <= right?
**A:** Because we need two different indices. When left == right, there's only one element, so we can't form a pair. Also, the problem guarantees exactly one solution exists, so we'll find it before left == right.

### Q10: What's the difference between this and Two Sum I?
**A:**
- **Two Sum I**: Unsorted array, can use hash map, return indices
- **Two Sum II**: Sorted array, must use O(1) space, return 1-indexed

The sorted constraint allows the efficient two-pointer approach.

### Q11: What are common mistakes when solving this problem?
**A:**
1. **Off-by-one error**: Forgetting to add 1 for 1-indexing
2. **Wrong pointer movement**: Moving pointers incorrectly based on sum comparison
3. **Checking isalnum()**: This problem uses simple integer comparison, not alphanumeric
4. **Infinite loop**: Wrong loop condition or pointer movement
5. **Using extra space**: Using hash map when O(1) is required

### Q12: Can we solve this problem recursively?
**A:** Technically yes, but it's unnecessary and uses O(n) space for the recursion stack, violating the O(1) space requirement. The iterative two-pointer approach is optimal.

### Q13: What's the time complexity again and why?
**A:** O(n) because:
- We start with two pointers at opposite ends
- Each iteration moves one pointer
- Each element is visited at most once
- We stop when we find the answer or pointers meet

Not O(log n) because we're not eliminating half the search space each time (that would be binary search).

### Q14: What if there are multiple valid pairs (theoretically)?
**A:** The problem guarantees exactly one solution exists, so this won't happen. But if it did, our algorithm would return the first pair found.

### Q15: How do we verify our solution is correct?
**A:** Check:
1. Sum equals target: numbers[i] + numbers[j] == target ✓
2. Indices are different: i < j ✓
3. Indices are 1-based: return [i+1, j+1] ✓
4. Array is sorted: exploited for efficiency ✓

## Edge Cases to Test

1. **Minimum size array**: [1, 2], target = 3 → [1, 2]
2. **Negative numbers**: [-1, 0], target = -1 → [1, 2]
3. **Large numbers**: [999, 1000], target = 1999 → [1, 2]
4. **All same value**: [5, 5, 5], target = 10 → [1, 2]
5. **Target at extremes**: [1, 2, 3], target = 4 → [1, 3]

## Time Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Map | O(n) | O(n) | Extra space not allowed |
| Binary Search | O(n log n) | O(1) | Slower than two-pointer |
| Two-Pointer | O(n) | O(1) | **Optimal** |
| Brute Force | O(n²) | O(1) | Too slow |

## Related Problems
- Two Sum (LeetCode 1)
- 3Sum (LeetCode 15)
- Two Sum III (LeetCode 170)
- Two Sum IV (LeetCode 653)
