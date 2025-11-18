"""
LeetCode 242: Valid Anagram
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(1) - fixed size dictionary of 26 elements at most

@author kbhatiya999
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Count frequency of each character
        char_count = {}
        
        # Increment for s, decrement for t
        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            char_count[t[i]] = char_count.get(t[i], 0) - 1
        
        # Check if all counts are zero
        for count in char_count.values():
            if count != 0:
                return False
        
        return True
