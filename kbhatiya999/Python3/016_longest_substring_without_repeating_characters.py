"""016. Longest Substring Without Repeating Characters

URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m, n)) where m is the charset size
"""

from typing import Dict

def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Uses sliding window approach with a hashmap to track character indices.
    """
    # Dictionary to store the last seen index of each character
    char_index: Dict[str, int] = {}
    
    max_length = 0
    left = 0  # Start of the sliding window
    
    for right in range(len(s)):
        # If character is already in the current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move left pointer to skip the duplicate
            left = char_index[s[right]] + 1
        
        # Update the last seen index of current character
        char_index[s[right]] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),          # empty string
        ("au", 2),        # "au"
        ("dvdf", 3),      # "vdf"
    ]
    
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {s!r} -> Output: {result} (Expected: {expected})")
