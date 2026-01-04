"""LeetCode 659: Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string.
The encoded string is then sent over the network and decoded back to the original list.

Approach: Length-prefix encoding
- Use format: "length#string" for each string
- Example: ["Hello", "World"] -> "5#Hello5#World"
- This handles strings with any ASCII characters including special characters

Time Complexity:
  encode: O(n*m) where n=number of strings, m=avg string length
  decode: O(n) where n=length of encoded string
Space Complexity: O(n*m) for the result
"""

class Solution:
    """Encode and Decode Strings using length-prefix encoding."""
    
    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings into a single string.
        
        Approach: Length-Prefix Encoding
        - For each string in the list, prepend its length and a delimiter
        - Format: "length#string" for each string
        - Example: ["Hello", "World"] -> "5#Hello5#World"
        
        Time Complexity: O(n * m) where n is the number of strings and m is avg length
        Space Complexity: O(n * m) for the encoded result
        
        Args:
            strs: List of strings to encode
            
        Returns:
            Encoded string with length-prefix format
        """
        if not strs:
            return ""
        
        encoded = []
        for s in strs:
            # Use length and # as delimiter: "5#Hello"
            encoded.append(str(len(s)) + "#" + s)
        
        return "".join(encoded)
    
    def decode(self, s: str) -> list[str]:
        """Decode a length-prefixed encoded string back to list of strings.
        
        Approach: Parse the length-prefix format
        - Read the length prefix until we hit '#'
        - Extract that many characters as the string
        - Continue until we've parsed the entire encoded string
        
        Time Complexity: O(n) where n is the length of encoded string
        Space Complexity: O(m) where m is total length of all original strings
        
        Args:
            s: Encoded string in length-prefix format
            
        Returns:
            List of original strings
        """
        if not s:
            return []
        
        result = []
        i = 0
        
        while i < len(s):
            # Find the '#' delimiter to get the length
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            # Extract length
            length = int(s[i:j])
            
            # Extract the string of the given length
            # j+1 to skip the '#', then take 'length' characters
            result.append(s[j+1:j+1+length])
            
            # Move pointer to next length prefix
            i = j + 1 + length
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal strings
    test1 = ["Hello", "World"]
    encoded1 = solution.encode(test1)
    decoded1 = solution.decode(encoded1)
    print(f"Test 1: {test1}")
    print(f"Encoded: {encoded1}")
    print(f"Decoded: {decoded1}")
    print(f"Match: {decoded1 == test1}\n")
    
    # Test case 2: Empty list
    test2 = []
    encoded2 = solution.encode(test2)
    decoded2 = solution.decode(encoded2)
    print(f"Test 2 (empty list): {test2}")
    print(f"Encoded: '{encoded2}'")
    print(f"Decoded: {decoded2}")
    print(f"Match: {decoded2 == test2}\n")
    
    # Test case 3: Single empty string
    test3 = [""]
    encoded3 = solution.encode(test3)
    decoded3 = solution.decode(encoded3)
    print(f"Test 3 (empty string): {test3}")
    print(f"Encoded: {encoded3}")
    print(f"Decoded: {decoded3}")
    print(f"Match: {decoded3 == test3}\n")
    
    # Test case 4: String with special characters
    test4 = ["a#b", "x:y", "123"]
    encoded4 = solution.encode(test4)
    decoded4 = solution.decode(encoded4)
    print(f"Test 4 (special chars): {test4}")
    print(f"Encoded: {encoded4}")
    print(f"Decoded: {decoded4}")
    print(f"Match: {decoded4 == test4}\n")
    
    # Test case 5: Single string
    test5 = ["OnlyOne"]
    encoded5 = solution.encode(test5)
    decoded5 = solution.decode(encoded5)
    print(f"Test 5 (single string): {test5}")
    print(f"Encoded: {encoded5}")
    print(f"Decoded: {decoded5}")
    print(f"Match: {decoded5 == test5}\n")
    
    print("All tests passed!" if all([
        decoded1 == test1,
        decoded2 == test2,
        decoded3 == test3,
        decoded4 == test4,
        decoded5 == test5
    ]) else "Some tests failed!")
