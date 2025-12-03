"""
LeetCode Problem: Contains Duplicate
Problem Number: 217

Problem Description:
Given an integer array nums, return true if any value appears more than once in the array,
otherwise return false.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Detect if array contains duplicates using a hash set.
        
        Solution approach:
        - Track seen numbers in a set
        - Return True if we encounter a number already in the set
        - Return False if we finish the loop (no duplicates)
        """
        # Implementation code
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    test1 = [1, 2, 3, 3]
    result1 = solution.hasDuplicate(test1)
    print(f"Test 1: {test1} -> {result1}")  # Expected output: True
    
    # Example 2
    test2 = [1, 2, 3, 4]
    result2 = solution.hasDuplicate(test2)
    print(f"Test 2: {test2} -> {result2}")  # Expected output: False
    
    # Example 3
    test3 = [1, 1]
    result3 = solution.hasDuplicate(test3)
    print(f"Test 3: {test3} -> {result3}")  # Expected output: True
