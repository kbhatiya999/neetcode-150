// LeetCode 217 - Contains Duplicate
// Difficulty: Easy
// Time Complexity: O(n)
// Space Complexity: O(n)

import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
