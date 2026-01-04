class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while left < right:
            # Calculate width and length of current container
            width = right - left
            length = min(height[left], height[right])
            
            # Calculate current area and update max
            currArea = length * width
            maxArea = max(maxArea, currArea)
            
            # Move the pointer pointing to the smaller height
            # because the area is limited by the shorter bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
