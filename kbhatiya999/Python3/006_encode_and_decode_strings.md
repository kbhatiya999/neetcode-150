# Problem 6: Encode and Decode Strings

## LeetCode Link
[LeetCode 659: Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

## Problem Statement

Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and decoded back to the original list of strings.

**Machine 1 (sender)** has the function:
```cpp
string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
```

**Machine 2 (receiver)** has the function:
```cpp
vector<string> decode(string s) {
    // ... your code
    return strs;
}
```

**Machine 1 does:**
```cpp
string encoded_string = encode(strs);
```

**Machine 2 does:**
```cpp
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

## Example 1

**Input:** `dummy_input = ["Hello","World"]`

**Output:** `["Hello","World"]`

## Example 2

**Input:** `dummy_input = [""]`

**Output:** `[""]`

## Constraints

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters

## Approach: Length-Prefix Encoding

### Key Insight

Instead of using a delimiter character that might appear in the actual strings, we use **length-prefix encoding**. We prepend each string with its length followed by a special delimiter (like '#'). This uniquely identifies where each string begins and ends.

**Format:** `length#string`

**Example:** `["Hello", "World"]` → `"5#Hello5#World"`

### Algorithm Steps

#### Encode
1. For each string in the list
2. Append the length of the string followed by '#' and the string itself
3. Concatenate all encoded strings

#### Decode
1. Initialize pointer at the beginning of the encoded string
2. While we haven't reached the end:
   - Read characters until we encounter '#' - this is the length
   - Parse the length as an integer
   - Extract exactly that many characters as the string
   - Move pointer forward by (length + delimiter positions)
3. Return the list of decoded strings

### Why This Works

- **Handles any character:** The '#' delimiter is only used to separate the length from the string, not to delimit strings themselves
- **Handles empty strings:** A string of length 0 is encoded as "0#" followed immediately by the next length
- **Unambiguous parsing:** Knowing the exact length of each string allows us to extract it precisely
- **Efficient:** Both encoding and decoding are linear time operations

### Visual Example

```
Input:  ["Hello", "World"]
Step 1: "5#" + "Hello" = "5#Hello"
Step 2: "5#Hello" + "5#" + "World" = "5#Hello5#World"

Decoding "5#Hello5#World":
Step 1: Read "5", then extract 5 chars → "Hello"
Step 2: Read "5", then extract 5 chars → "World"
Result: ["Hello", "World"]
```

### Special Cases

1. **Empty list:** Return empty string from encode, empty list from decode
2. **Empty string in list:** Encoded as "0#" with nothing after it
3. **Strings with special characters:** "a#b", "x:y", etc. are handled correctly because we rely on length, not characters
4. **Strings with digits:** "123" is encoded as "3#123", unambiguous

## Solution Code

```python
class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        
        return "".join(encoded)
    
    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        
        result = []
        i = 0
        
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            # Extract length
            length = int(s[i:j])
            
            # Extract the string
            result.append(s[j+1:j+1+length])
            
            # Move to next length prefix
            i = j + 1 + length
        
        return result
```

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|-----------|-------------|
| **Time - Encode** | O(n*m) | n = number of strings, m = avg string length; we concatenate all strings |
| **Time - Decode** | O(n) | n = length of encoded string; we parse each character once |
| **Space - Encode** | O(n*m) | Store the encoded string result |
| **Space - Decode** | O(n*m) | Store all decoded strings |

## Follow-up

**Could you write a generalized algorithm to work on any possible set of characters?**

Yes! The length-prefix approach already works with any character set:
- For binary data, use the same encoding (binary length + binary data)
- For Unicode strings, use UTF-8 byte length, not character count
- The delimiter '#' could be replaced with a special byte sequence if needed

## Key Takeaways

1. **Length-prefix encoding** is a robust serialization technique
2. Don't rely on delimiters that might appear in the data
3. Knowing the exact length allows unambiguous parsing
4. This approach generalizes well to any character set or binary data
