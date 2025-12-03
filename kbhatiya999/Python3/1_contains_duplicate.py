"""LeetCode 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Detect if the array contains duplicate elements.
        
        Approach: Use a set to track seen numbers. If we encounter a number
        that's already in the set, we found a duplicate.
        
        Args:
            nums: List of integers
            
        Returns:
            True if duplicates exist, False otherwise
        """
        # Use a set to track seen numbers
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Contains duplicate
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.containsDuplicate(nums1)}")
    print(f"Expected: True\n")
    
    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2}")
    print(f"Output: {solution.containsDuplicate(nums2)}")
    print(f"Expected: False\n")
    
    # Test case 3: Complex case
    nums3 = [1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3}")
    print(f"Output: {solution.containsDuplicate(nums3)}")
    print(f"Expected: True")
