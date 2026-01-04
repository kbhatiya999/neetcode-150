# LeetCode 128: Longest Consecutive Sequence

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time.

## Examples

### Example 1
**Input:** `nums = [100, 4, 200, 1, 3, 2]`
**Output:** `4`
**Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

### Example 2
**Input:** `nums = [0, 3, 2, 5, 4, 6, 1, 1]`
**Output:** `7`
**Explanation:** The longest consecutive elements sequence is `[0, 1, 2, 3, 4, 5, 6]`. Therefore its length is 7.

## Approach

### Algorithm: Set-Based Approach
The key insight is to use a set to achieve O(1) lookup time:

1. Convert the array to a set for constant-time lookups
2. For each number, check if it's the start of a sequence (i.e., num-1 is not in the set)
3. If it's the start, count how many consecutive numbers follow
4. Track the maximum length found

### Why O(n)?
- Converting to set: O(n)
- Iterating through each number: O(n)
- While loop total iterations: O(n) (each element is visited at most twice)
- Overall: O(n)

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time | O(n) |
| Space | O(n) |

## Key Points
- The set allows us to skip over duplicates automatically
- We only start counting from the beginning of sequences
- This avoids recounting the same consecutive sequence multiple times

## Submission Details
- **Status:** Accepted ✓
- **LeetCode:** Problem #128
- **Difficulty:** Medium
- **Acceptance Rate:** 47.0%

## Related Topics
- Array
- Hash Table
- Union Find
