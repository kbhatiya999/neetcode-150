class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target in a sorted array.
        
        Args:
            numbers: Sorted array of integers in non-decreasing order
            target: Target sum
            
        Returns:
            1-indexed indices of two numbers that sum to target
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed
            elif current_sum < target:
                left += 1  # Need larger sum, move left pointer right
            else:
                right -= 1  # Need smaller sum, move right pointer left
        
        return []  # Should never reach here as solution always exists


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    assert sol.twoSum([2,7,11,15], 9) == [1, 2]
    
    # Test case 2
    assert sol.twoSum([2,3,4], 6) == [1, 3]
    
    # Test case 3
    assert sol.twoSum([-1,0], -1) == [1, 2]
    
    print("All tests passed!")
