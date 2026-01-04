"""LeetCode 49: Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    - 1 <= strs.length <= 10^4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together from an array of strings.
        
        Approach: Use hash map with sorted string as key
        - Anagrams will have the same sorted representation
        - Use sorted string as key to group anagrams together
        
        Time Complexity: O(n * k log k) where n = len(strs), k = max length of string
        Space Complexity: O(n * k) for the hash map
        
        Args:
            strs: List of strings
            
        Returns:
            List of groups where each group contains anagrams
        """
        # Use a hash map to group anagrams
        # Key: sorted string (canonical form)
        # Value: list of strings that are anagrams
        anagram_map = {}
        
        for s in strs:
            # Sort the string to get its canonical form
            # All anagrams will have the same sorted form
            sorted_str = ''.join(sorted(s))
            
            # Add the string to its anagram group
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            anagram_map[sorted_str].append(s)
        
        # Return all the groups
        return list(anagram_map.values())


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    result1 = solution.groupAnagrams(strs1)
    print(f"Input: strs = {strs1}")
    print(f"Output: {result1}")
    print(f"Expected: Groups of anagrams\n")
    
    # Test Case 2
    strs2 = [""]
    result2 = solution.groupAnagrams(strs2)
    print(f"Input: strs = {strs2}")
    print(f"Output: {result2}")
    print(f"Expected: [[\"\"]]\n")
    
    # Test Case 3
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    print(f"Input: strs = {strs3}")
    print(f"Output: {result3}")
    print(f"Expected: [[\"a\"]]")
