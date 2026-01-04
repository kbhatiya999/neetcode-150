class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a valid palindrome.
        
        A palindrome reads the same forward and backward, ignoring
        non-alphanumeric characters and case differences.
        
        Args:
            s: Input string
            
        Returns:
            True if s is a palindrome, False otherwise
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Valid palindrome with special characters
    assert sol.isPalindrome("Was it a car or a cat I saw?") == True
    
    # Test case 2: Invalid palindrome
    assert sol.isPalindrome("tab a cat") == False
    
    # Test case 3: Empty string
    assert sol.isPalindrome(" ") == True
    
    # Test case 4: Single character
    assert sol.isPalindrome("a") == True
    
    # Test case 5: All special characters
    assert sol.isPalindrome(".,") == True
    
    print("All tests passed!")
