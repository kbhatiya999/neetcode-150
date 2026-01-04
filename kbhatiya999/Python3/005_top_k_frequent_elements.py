"""LeetCode 347: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of unique elements in the array]
    - It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n).
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find the k most frequent elements in the array using bucket sort.
        
        Approach:
        1. Count frequency of each element - O(n)
        2. Create buckets indexed by frequency - O(n)
        3. Collect top k elements from highest frequencies - O(n)
        
        Time Complexity: O(n) - linear time
        Space Complexity: O(n) - for frequency map and buckets
        
        Args:
            nums: List of integers
            k: Number of most frequent elements to return
            
        Returns:
            List of k most frequent elements
        """
        # Step 1: Count frequency of each element
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Create buckets where index = frequency
        # freq[i] = list of numbers that appear i times
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Step 3: Collect top k elements from highest frequencies
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: [1, 2] (order may vary)\n")
    
    # Test Case 2
    nums2 = [1]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: [1]\n")
    
    # Test Case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    result3 = solution.topKFrequent(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: [-1, 2] or [2, -1]")
