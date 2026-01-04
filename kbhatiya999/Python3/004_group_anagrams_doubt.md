# Doubts and Questions: Group Anagrams (LeetCode 49)

## Common Questions and Clarifications

### 1. Why does sorting work to identify anagrams?

**Question:** How does sorting help us group anagrams together?

**Answer:** All anagrams contain the exact same characters with the same frequencies. When you sort any anagram, you get the same canonical representation.

**Example:**
```
"eat" → sorted: "aet"
"tea" → sorted: "aet"
"ate" → sorted: "aet"

All produce "aet" when sorted! ✓
```

**Key Insight:** Sorted string acts as a unique fingerprint for anagram groups.

---

### 2. Can we use something other than sorting?

**Question:** Is there a faster way than sorting each string?

**Answer:** Yes! Use character frequency counting:

```python
# Instead of sorting (O(k log k)):
sorted_str = ''.join(sorted(s))

# Use character counting (O(k)):
count = [0] * 26
for char in s:
    count[ord(char) - ord('a')] += 1
key = tuple(count)  # Use as hash map key
```

**Comparison:**
- Sorting: O(k log k) per string
- Counting: O(k) per string
- Character counting is faster!

---

### 3. Why use tuple(count) instead of list?

**Question:** Why convert the character count array to a tuple?

**Answer:** Lists are mutable and cannot be used as dictionary keys in Python. Tuples are immutable and hashable.

```python
# This FAILS:
count = [1, 0, 0, ...]  # list
anagram_map[count] = ...  # ERROR! Lists aren't hashable

# This WORKS:
count = tuple([1, 0, 0, ...])  # tuple
anagram_map[count] = ...  # ✓ Tuples are hashable
```

---

### 4. What's the time complexity?

**Question:** How do we calculate the overall time complexity?

**Answer:** 

**With Sorting:**
- n strings
- Each string has at most k characters
- Sorting each string: O(k log k)
- Total: **O(n * k log k)**

**With Character Counting:**
- n strings
- Each string has at most k characters
- Counting characters: O(k)
- Total: **O(n * k)**

---

### 5. Why return `list(anagram_map.values())`?

**Question:** What does `.values()` do?

**Answer:** `.values()` returns all the values (lists of anagrams) from the hash map.

**Example:**
```python
anagram_map = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}

anagram_map.values()  # dict_values(...)
list(anagram_map.values())  # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

We convert to list because the problem expects a list, not a dict_values object.

---

### 6. Does the order of groups matter?

**Question:** Can we return groups in any order?

**Answer:** Yes! The problem says "you can return the answer in any order."

**Both valid:**
```python
[["eat", "tea"], ["tan", "nat"], ["bat"]]
[["bat"], ["eat", "tea"], ["tan", "nat"]]
```

**Within each group:** Order also doesn't matter
```python
["eat", "tea", "ate"]
["tea", "ate", "eat"]
```

Both are correct!

---

### 7. How do we handle empty strings?

**Question:** What if strs = ["", "", "a"]?

**Answer:** Empty strings are anagrams of each other!

```python
strs = ["", "", "a"]

Iteration 1: s = ""
  sorted = ""
  anagram_map = {"": [""]}

Iteration 2: s = ""
  sorted = ""
  anagram_map = {"": ["", ""]}

Iteration 3: s = "a"
  sorted = "a"
  anagram_map = {"": ["", ""], "a": ["a"]}

Result: [["", ""], ["a"]]
```

---

### 8. Can strings have different lengths and still be anagrams?

**Question:** Are "abc" and "ab" anagrams?

**Answer:** **NO!** Anagrams must:
1. Have the same length
2. Have the same characters
3. With the same frequencies

"abc" and "ab" have different lengths, so they cannot be anagrams.

```python
sorted("abc") = "abc"
sorted("ab") = "ab"

"abc" ≠ "ab" → Different groups
```

---

### 9. What if all strings are unique (no anagrams)?

**Question:** What if strs = ["a", "b", "c"]?

**Answer:** Each string forms its own group.

```python
strs = ["a", "b", "c"]

anagram_map = {
    "a": ["a"],
    "b": ["b"],
    "c": ["c"]
}

Result: [["a"], ["b"], ["c"]]
```

Each group has only one element.

---

### 10. Why not compare every pair of strings?

**Question:** Can't we just check if each pair is an anagram?

**Answer:** That would be O(n² * k) which is too slow!

**Naive Approach:**
```python
for i in range(len(strs)):
    for j in range(i+1, len(strs)):
        if is_anagram(strs[i], strs[j]):  # O(k)
            # Group them
```

**Time:** O(n² * k) - very slow for large inputs

**Hash Map Approach:**
- O(n * k log k) with sorting
- O(n * k) with character counting

Much faster!

---

## Advanced Questions

### 11. How much space does the hash map use?

**Question:** What's the space complexity?

**Answer:** O(n * k)

**Explanation:**
- We store all n strings
- Each string has at most k characters
- Total space: n strings × k characters = O(n * k)

The hash map itself uses O(n) keys (at most n groups), but the strings stored are what dominate.

---

### 12. What if strings contain uppercase or special characters?

**Question:** Does our solution work for "Eat" and "Tea"?

**Answer:** No! The problem specifies lowercase only.

If we needed to handle mixed case:
```python
sorted_str = ''.join(sorted(s.lower()))
```

For special characters:
```python
# Only count letters
count = {}
for char in s:
    if char.isalpha():
        count[char] = count.get(char, 0) + 1
```

---

### 13. Can we modify the input array?

**Question:** Can we sort the input array in place?

**Answer:** Generally avoid modifying input unless explicitly allowed. In this problem, we don't need to - we create new data structures.

---

## Key Takeaways

1. **Sorting creates canonical form** - All anagrams → same sorted string
2. **Character counting is faster** - O(k) vs O(k log k)
3. **Hash maps group efficiently** - O(1) lookup and insertion
4. **Tuples are hashable** - Use for character count keys
5. **Order doesn't matter** - Groups and within groups
6. **Empty strings are anagrams** - Of each other
7. **Length must match** - Different lengths ≠ anagrams
8. **Space = O(n * k)** - Storing all strings
