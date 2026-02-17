# Longest Substring Without Repeating Characters - Doubt/Clarifications

## Common Questions

### 1. Why do we need a dictionary to track character indices?
- We need to track the **most recent index** of each character, not just whether it exists
- This helps us know exactly where to move the left pointer when we encounter a duplicate
- Example: if "a" appears at index 0 and again at index 5, we move left to 1 (after the first "a")

### 2. What's the difference between this and just using a set?
- A **set** only tells us if a character exists in the current window
- A **dictionary** tells us where (at what index) the character last appeared
- With a set, we'd have to shrink the window one character at a time (inefficient)
- With a dictionary, we can jump the left pointer directly to skip duplicates

### 3. When should we update `left` pointer?
- Only when the character at `s[right]` is already in our current window
- AND it's to the right of our current `left` pointer
- Condition: `s[right] in char_index and char_index[s[right]] >= left`
- This prevents moving `left` backwards

### 4. Why update `max_length` AFTER processing the right pointer?
- The window is valid AFTER we update the left pointer (if needed) and add the current character
- We calculate length as `right - left + 1` where both pointers are within valid bounds
- Example: For "au", left=0, right=1, length=1-0+1=2

### 5. Can there be a duplicate in the current window?
- No. The algorithm ensures no duplicates exist between `left` and `right` (inclusive)
- If a duplicate is found, we immediately move `left` to eliminate it
- Therefore, the window always represents a valid substring

### 6. Time and Space Complexity
- **Time**: O(n) - each character visited at most twice (once by right pointer, once by left pointer)
- **Space**: O(min(m, n)) where m is charset size (at most 26 for lowercase English letters)
- We only store characters that appear in the string

### 7. Edge Cases
- Empty string: returns 0
- Single character: returns 1
- All unique characters: returns length of string
- All same characters: returns 1

### 8. How does the sliding window handle overlapping ranges?
- Example: "abcabcbb"
  - First "abc" found at indices 0-2
  - When we see 'a' at index 3, we move left to 1 (skip first 'a')
  - Window becomes "bca" (indices 1-3)
  - When we see 'b' at index 4, we move left to 2 (skip first 'b')
  - Window becomes "cab" (indices 2-4)
  - The algorithm efficiently handles overlaps by jumping left pointer

## Visual Trace Example

String: "abcabcbb"

```
left=0, right=0: window="a", char_index={'a':0}, max=1
left=0, right=1: window="ab", char_index={'a':0,'b':1}, max=2
left=0, right=2: window="abc", char_index={'a':0,'b':1,'c':2}, max=3
left=1, right=3: window="bca", max=3
left=2, right=4: window="cab", max=3
left=3, right=5: window="abc", max=3
left=4, right=6: window="bc", max=3
left=5, right=7: window="b", max=3
```

Answer: 3

## Key Insights

1. **Sliding window is optimal** - track indices to jump left pointer efficiently
2. **Two-pointer approach** ensures O(n) time complexity
3. **Lazy deletion** - only move left when encountering duplicates
4. **Character index map** is critical for efficiency
