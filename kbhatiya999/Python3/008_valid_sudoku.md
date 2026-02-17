# LeetCode 36: Valid Sudoku

## Problem Statement
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition
2. Each column must contain the digits `1-9` without repetition
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition

**Note:** A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated according to the mentioned rules.

## Examples

### Example 1
**Input:** A valid Sudoku board
**Output:** `true`

### Example 2
**Input:** An invalid Sudoku board (e.g., duplicate in a row)
**Output:** `false`

## Approach

### Algorithm: Hash Set Validation
The key is to check each constraint as we iterate through the board:

1. Create three hash sets to track what we've seen:
   - Row tracker: tracks digits in each row
   - Column tracker: tracks digits in each column
   - Box tracker: tracks digits in each 3x3 box

2. For each cell:
   - If it's empty ("."), skip it
   - Check if the digit is already in row, column, or box
   - If yes, return False
   - Otherwise, add it to all three sets

3. If we complete the loop without conflicts, return True

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time | O(1) |
| Space | O(1) |

**Note:** Time and space are O(1) because the board size is fixed at 9x9

## Key Insights

- We don't need to solve the Sudoku, just validate it
- Box index can be calculated as `(row // 3, col // 3)` or `row // 3 * 3 + col // 3`
-   - **Box Index Explanation**: The 3x3 box index divides the 9x9 grid into 9 boxes (3 rows and 3 columns of boxes). For any cell at position (row, col):
    -     - Box row: `row // 3` (0-2 representing top, middle, bottom rows of boxes)
    -     - Box col: `col // 3` (0-2 representing left, middle, right columns of boxes)
    -     - Combined index: `row // 3 * 3 + col // 3` gives a unique number 0-8 for each box
- Using sets makes lookup O(1)
- We can optimize space by using a 2D set or dictionary

## Submission Details
- **Status:** Accepted
- **LeetCode:** Problem #36
- **Difficulty:** Medium
- **Acceptance Rate:** ~70%

## Related Topics
- Array
- Hash Table
- Matrix
