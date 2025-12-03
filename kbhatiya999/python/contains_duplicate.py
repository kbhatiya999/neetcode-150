# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for current_number in nums:
            if current_number in seen_numbers:
                return True
            seen_numbers.add(current_number)
        return False
