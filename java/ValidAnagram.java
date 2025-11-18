/**
 * LeetCode 242: Valid Anagram
 * Difficulty: Easy
 * 
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * 
 * Time Complexity: O(n) where n is the length of the strings
 * Space Complexity: O(1) - fixed size array of 26 elements
 * 
 * @author kbhatiya999
 */

class Solution {
    public boolean isAnagram(String s, String t) {
        // If lengths are different, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Count frequency of each character
        int[] charCount = new int[26]; // For lowercase English letters
        
        // Increment for s, decrement for t
        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;
            charCount[t.charAt(i) - 'a']--;
        }
        
        // Check if all counts are zero
        for (int count : charCount) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }
}
