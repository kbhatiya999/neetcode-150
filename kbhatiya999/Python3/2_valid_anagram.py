"""LeetCode 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input: s = "rat", t = "car"
    Output: False

Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters.
"""

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.
        
        An anagram contains the same characters with the same frequency,
        just in a different order.
        
        Args:
            s: First string
            t: Second string
            
        Returns:
            True if t is an anagram of s, False otherwise
        """
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


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Input: s = \"{s1}\", t = \"{t1}\"")
    print(f"Output: {solution.isAnagram(s1, t1)}")
    print(f"Expected: True\n")
    
    # Test Case 2
    s2 = "rat"
    t2 = "car"
    print(f"Input: s = \"{s2}\", t = \"{t2}\"")
    print(f"Output: {solution.isAnagram(s2, t2)}")
    print(f"Expected: False\n")
    
    # Test Case 3
    s3 = "a"
    t3 = "a"
    print(f"Input: s = \"{s3}\", t = \"{t3}\"")
    print(f"Output: {solution.isAnagram(s3, t3)}")
    print(f"Expected: True")
