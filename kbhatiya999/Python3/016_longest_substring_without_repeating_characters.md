# Problem 16: Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

## Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

## Approach: Sliding Window

The sliding window technique is the optimal approach for this problem.

### Algorithm

1. Use two pointers (`left` and `right`) to maintain a window
2. Use a dictionary/hashmap to store the last seen index of each character
3. Expand the window by moving `right` pointer
4. When a duplicate character is found, move `left` pointer to skip the previous occurrence
5. Track the maximum window size

### Visualization

```
For s = "abcabcbb"

Window progression:
Left pointer (l): Initially at 0
Right pointer (r): Moves from 0 to end

step 1: [a]       -> length = 1
step 2: [ab]      -> length = 2
step 3: [abc]     -> length = 3 (max)
step 4: When we see 'a' at index 3, move left to 1: [bca]
step 5: [bcab]    -> length = 3
step 6: When we see 'c' at index 5, move left to 3: [abc] -> Wait, it's actually [ab]
step 7: [abc]     -> length = 3
step 8: When we see 'b' at index 7, move left to 5: [cb] -> Skip to 6: [b]
step 9: [bb]      -> Move left to 8: [b]
```

## Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the string
  - Each character is visited at most twice (once by right pointer, once by left pointer)
- **Space Complexity**: O(min(m, n)) where m is the charset size and n is the string length
  - The hashmap stores at most `m` characters
  - For ASCII: O(1) or O(128)
  - For Unicode: O(1) or O(~1M)

## Implementation Details

- The key insight is that we don't need to check if all characters are distinct within the window
- We only need to move the left pointer when we encounter a duplicate
- The dictionary maintains the **last seen index** of each character, allowing us to skip directly to the right position

## Edge Cases

- Empty string: returns 0
- Single character: returns 1
- All unique characters: returns length of string
- All same characters: returns 1

## Related Problems

- Problem 3: Longest Substring Without Repeating Characters (LeetCode 3)
- Problem 159: Longest Substring with At Most Two Distinct Characters (LeetCode 159)
- Problem 340: Longest Substring with At Most K Distinct Characters (LeetCode 340)
