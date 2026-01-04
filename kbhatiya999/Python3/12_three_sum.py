class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.
        
        Args:
            nums: List of integers
            
        Returns:
            List of lists containing all unique triplets that sum to 0
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: if smallest sum > 0, break
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            
            # Optimization: if largest sum < 0, continue
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            
            # Two-pointer approach for remaining two numbers
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    assert sol.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert sol.threeSum([0,1,1]) == []
    assert sol.threeSum([0,0,0]) == [[0,0,0]]
    
    print("All tests passed!")
