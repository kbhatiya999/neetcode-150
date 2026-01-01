# LeetCode 49: Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

### Example 2:
```
Input: strs = [""]
Output: [[""]]
```

### Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Approach

### Hash Map with Sorted String as Key - Optimal Solution

The key insight is that all anagrams will produce the same string when sorted. We can use this sorted string as a key to group anagrams together.

**Algorithm:**
1. Create a hash map where:
   - Key: sorted version of the string (canonical form)
   - Value: list of strings that are anagrams
2. Iterate through each string:
   - Sort the string to get its canonical form
   - Add the original string to the list for that canonical form
3. Return all the groups (values of the hash map)

**Time Complexity:** O(n * k log k) where n is the number of strings and k is the maximum length of a string (due to sorting)
**Space Complexity:** O(n * k) for storing all strings in the hash map

## Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a hash map to group anagrams
        # Key: sorted string (canonical form)
        # Value: list of strings that are anagrams
        anagram_map = {}
        
        for s in strs:
            # Sort the string to get its canonical form
            # All anagrams will have the same sorted string
            sorted_str = ''.join(sorted(s))
            
            # Add this string to the group of its anagrams
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            anagram_map[sorted_str].append(s)
        
        # Return all groups as a list
        return list(anagram_map.values())
```

## Alternative Solution: Character Count Array

### Using Character Frequency as Key

Instead of sorting, we can use character frequency counts as the key. This is more efficient.

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a character count array (26 letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as key (lists aren't hashable)
            key = tuple(count)
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
```

**Time Complexity:** O(n * k) where n is number of strings, k is max string length
**Space Complexity:** O(n * k)

This is better than sorting because:
- Sorting: O(k log k) per string
- Character counting: O(k) per string

## Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sorted String as Key | O(n * k log k) | O(n * k) | Simple and intuitive |
| Character Count as Key | O(n * k) | O(n * k) | **Optimal** - faster than sorting |
| Naive (Compare all pairs) | O(n² * k) | O(n * k) | Too slow |

## Key Insights

1. **Canonical form:** All anagrams map to the same canonical representation
2. **Sorted string works:** "eat", "tea", "ate" all become "aet" when sorted
3. **Hash map for grouping:** Efficiently groups strings by their canonical form
4. **Character counting is faster:** O(k) vs O(k log k) for each string
5. **Tuples as keys:** Character count arrays need to be tuples (immutable) to be hashable

## Edge Cases

1. **Empty string:** strs = [""] → [[""]]
2. **Single character:** strs = ["a"] → [["a"]]
3. **No anagrams:** strs = ["a", "b", "c"] → [["a"], ["b"], ["c"]]
4. **All anagrams:** strs = ["abc", "bca", "cab"] → [["abc", "bca", "cab"]]
5. **Mixed lengths:** strs = ["a", "ab", "abc"] → [["a"], ["ab"], ["abc"]]

## Why This Works

**Anagram Property:** Two strings are anagrams if and only if:
- They have the same length
- They contain the same characters
- Each character appears the same number of times

**Sorting Preserves This:**
- "eat" sorted = "aet"
- "tea" sorted = "aet"
- "ate" sorted = "aet"

All anagrams produce the same sorted string!

## Example Walkthrough

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

```
Iteration 1: s = "eat"
  sorted = "aet"
  anagram_map = {"aet": ["eat"]}

Iteration 2: s = "tea"
  sorted = "aet"
  anagram_map = {"aet": ["eat", "tea"]}

Iteration 3: s = "tan"
  sorted = "ant"
  anagram_map = {"aet": ["eat", "tea"], "ant": ["tan"]}

Iteration 4: s = "ate"
  sorted = "aet"
  anagram_map = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}

Iteration 5: s = "nat"
  sorted = "ant"
  anagram_map = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}

Iteration 6: s = "bat"
  sorted = "abt"
  anagram_map = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
  }

Result: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## Related Problems

- LeetCode 242: Valid Anagram
- LeetCode 438: Find All Anagrams in a String
- LeetCode 249: Group Shifted Strings
- LeetCode 1347: Minimum Number of Steps to Make Two Strings Anagram
