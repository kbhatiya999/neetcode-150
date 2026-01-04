from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Create a set for O(1) lookups
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 20, 4, 10, 3, 4, 5]
    assert solution.longestConsecutive(nums1) == 4
    print("Test case 1 passed: [2,20,4,10,3,4,5] -> 4")
    
    # Test case 2
    nums2 = [0, 3, 2, 5, 4, 6, 1, 1]
    assert solution.longestConsecutive(nums2) == 7
    print("Test case 2 passed: [0,3,2,5,4,6,1,1] -> 7")
    
    # Test case 3 - Empty array
    nums3 = []
    assert solution.longestConsecutive(nums3) == 0
    print("Test case 3 passed: [] -> 0")
    
    print("\nAll test cases passed!")
