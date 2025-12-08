"""LeetCode 1: Two Sum

Given an array of integers nums and an integer target, return the indices of the two
numbers such that they add up to target. You may assume that each input would have exactly
one solution, and you may not use the same element twice. You can return the answer in
any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to target.
        Return the indices of the two numbers.
        
        Approach: Hash Map (Single Pass)
        - Iterate through the array
        - For each number, calculate the complement (target - current)
        - Check if complement exists in our hash map
        - If found, return indices of complement and current number
        - Otherwise, store current number and its index in hash map
        
        Time Complexity: O(n)
        Space Complexity: O(n) - hash map can store up to n elements
        
        Args:
            nums: List of integers
            target: The target sum
            
        Returns:
            List of two indices [i, j] where nums[i] + nums[j] == target
        """
        # Hash map to store value: index pairs
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in our hash map, we found our pair
            if complement in seen:
                return [seen[complement], i]
            
            # Store the current number and its index
            seen[num] = i
        
        # No solution found (should not happen based on problem constraints)
        return []


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Explanation: nums[{result1[0]}] + nums[{result1[1]}] = {nums1[result1[0]]} + {nums1[result1[1]]} = {target1}\n")
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Explanation: nums[{result2[0]}] + nums[{result2[1]}] = {nums2[result2[0]]} + {nums2[result2[1]]} = {target2}\n")
    
    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Explanation: nums[{result3[0]}] + nums[{result3[1]}] = {nums3[result3[0]]} + {nums3[result3[1]]} = {target3}")
