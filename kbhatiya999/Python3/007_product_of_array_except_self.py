"""LeetCode 238: Product of Array Except Self

Given an integer array nums, return an array output where output[i] is the product
of all elements of nums except nums[i].

Must be solved in O(n) time without using division.

Approach: Prefix and Postfix Products
- First pass: Calculate prefix products (product of all elements to the left)
- Second pass: Calculate postfix products (product of all elements to the right)
- Multiply prefix and postfix for each position

Time Complexity: O(n)
Space Complexity: O(1) excluding output array
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Product of Array Except Self using prefix/postfix approach.
        
        Approach: Two-pass solution
        - First pass: Calculate prefix products (product of all elements to the left)
        - Second pass: Calculate suffix products (product of all elements to the right)
        
        For each position i, multiply the prefix product with suffix product.
        
        Time: O(n)
        Space: O(1) excluding output array
        """
        n = len(nums)
        output = [1] * n
        
        # First pass: calculate prefix products
        # output[i] = product of all elements to the left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Second pass: calculate suffix products and multiply
        # Multiply output[i] by the product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,4,6] -> [48,24,12,8]
    test1 = [1, 2, 4, 6]
    result1 = solution.productExceptSelf(test1)
    print(f"Test 1: {test1} -> {result1}")
    assert result1 == [48, 24, 12, 8], f"Expected [48, 24, 12, 8], got {result1}"
    
    # Test case 2: [-1,0,1,2,3] -> [0,-6,0,0,0]
    test2 = [-1, 0, 1, 2, 3]
    result2 = solution.productExceptSelf(test2)
    print(f"Test 2: {test2} -> {result2}")
    assert result2 == [0, -6, 0, 0, 0], f"Expected [0, -6, 0, 0, 0], got {result2}"
    
    # Test case 3: [2,3,4,5] -> [60,40,30,24]
    test3 = [2, 3, 4, 5]
    result3 = solution.productExceptSelf(test3)
    print(f"Test 3: {test3} -> {result3}")
    assert result3 == [60, 40, 30, 24], f"Expected [60, 40, 30, 24], got {result3}"
    
    # Test case 4: [1,1] -> [1,1]
    test4 = [1, 1]
    result4 = solution.productExceptSelf(test4)
    print(f"Test 4: {test4} -> {result4}")
    assert result4 == [1, 1], f"Expected [1, 1], got {result4}"
    
    print("\nAll tests passed!")
