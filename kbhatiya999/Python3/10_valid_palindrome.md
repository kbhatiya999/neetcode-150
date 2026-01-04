# Problem 10: Valid Palindrome

## Problem Statement
Given a string `s`, determine if it is a **valid palindrome**.

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

## Constraints
- 1 <= s.length <= 2 × 10^5
- s consists of printable ASCII characters.

## Examples

### Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.
```

## Approach

### Two-Pointer Method
Use two pointers starting from both ends of the string and move towards the center:
1. Initialize left pointer at the beginning and right pointer at the end
2. Skip non-alphanumeric characters from both sides
3. Compare characters (case-insensitive) at both pointers
4. If they don't match, return False
5. Continue until pointers meet

**Time Complexity:** O(n) - single pass through the string
**Space Complexity:** O(1) - only using two pointers

## LeetCode Problem
[Valid Palindrome - LeetCode #125](https://leetcode.com/problems/valid-palindrome/)

## Solution Details

### Key Points:
- Use `isalnum()` to check if a character is alphanumeric
- Use `lower()` for case-insensitive comparison
- Two-pointer technique efficiently handles the problem in O(n) time and O(1) space

### Implementation Notes:
- No need to create a new cleaned string (space-efficient)
- Skip non-alphanumeric characters dynamically
- Compare only alphanumeric characters

## Submission Status
- **Status:** Accepted
- **Runtime:** 11 ms (Beats 36.57%)
- **Memory:** 17.68 MB (Beats 91.00%)
- **Test Cases Passed:** 487/487
