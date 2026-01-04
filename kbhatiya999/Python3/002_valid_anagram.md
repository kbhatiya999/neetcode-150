# LeetCode 242: Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

### Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Approach

### Hash Map / Character Frequency Counting

The key insight is that two strings are anagrams if and only if they contain exactly the same characters with the same frequencies.

**Algorithm:**
1. If the strings have different lengths, they cannot be anagrams
2. Count the frequency of each character in the first string
3. For each character in the second string, decrement its count
4. If any character's count goes negative or if a character in the second string is not in the map, return False
5. If all checks pass, return True

**Time Complexity:** O(n) where n is the length of the strings
**Space Complexity:** O(1) since we have at most 26 lowercase letters (constant space)

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Count character frequencies in both strings
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        return True
```

## Alternative Solutions

### 1. Sorting Approach
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
**Time Complexity:** O(n log n) due to sorting
**Space Complexity:** O(n) for the sorted arrays

### 2. Using Counter from Collections
```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```
**Time Complexity:** O(n)
**Space Complexity:** O(1) - at most 26 characters

## Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Map | O(n) | O(1) | Best for this problem |
| Sorting | O(n log n) | O(n) | Simpler but slower |
| Counter | O(n) | O(1) | Most Pythonic |

## Test Cases

1. **Basic anagram:** s = "anagram", t = "nagaram" → true
2. **Not anagram:** s = "rat", t = "car" → false
3. **Single character:** s = "a", t = "a" → true
4. **Empty-like:** s = "ab", t = "ba" → true
5. **Different lengths:** s = "a", t = "ab" → false

## Key Insights

1. Length check is crucial - anagrams must have the same length
2. Character frequency must be identical
3. The order doesn't matter, only the characters and their counts
4. Works only with lowercase English letters as per constraints

## Related Problems

- LeetCode 49: Group Anagrams
- LeetCode 438: Find All Anagrams in a String
- LeetCode 383: Ransom Note
