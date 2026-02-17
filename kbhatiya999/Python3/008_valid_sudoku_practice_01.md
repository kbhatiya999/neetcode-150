# LeetCode 36: Valid Sudoku - Practice Attempt 1

## Problem Understanding
Validate a 9x9 Sudoku board by checking:
1. Each row contains digits 1-9 without repetition
2. Each column contains digits 1-9 without repetition
3. Each 3x3 sub-box contains digits 1-9 without repetition

Note: Only filled cells (not '.') need validation

## Attempt 1: Initial Solution

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        
        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        
        # Check 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        cell = board[row][col]
                        if cell != '.':
                            if cell in seen:
                                return False
                            seen.add(cell)
        
        return True
```

## AI Comment on Attempt 1

**Strengths:**
- Correct logic: The solution properly validates all three constraints (rows, columns, boxes)
- Clear structure: Each constraint is checked separately, making the code readable
- Efficient approach: Uses sets for O(1) lookup, achieving O(1) time complexity overall (fixed 9x9 board)

**Potential Improvements:**
- **Inefficient approach**: The current solution makes 3 separate passes through the board (one for rows, one for columns, one for boxes)
- **Can be optimized**: Instead of making 3 passes, we can iterate through the board once and track all three constraints simultaneously
- **More Pythonic**: Could use 3 hash tables (dictionaries or sets) to track row/col/box violations in a single pass

**Optimization Note:**
A more optimized version would use 3 dictionaries of sets to track:
- `rows`: dict mapping row_index -> set of seen digits
- `cols`: dict mapping col_index -> set of seen digits  
- `boxes`: dict mapping box_index -> set of seen digits

Then iterate once through the board, checking and updating all three simultaneously.

## Attempt 2


**Optimized Solution - Single Pass**

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # matrix for 9 rows, 9 columns and 9 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                # cell value
                cell = board[i][j]
                if cell == '.':
                    continue
                
                # Check cell row
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                
                # Check cell column
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                
                # 3x3 boxes. Box row: i //3 | Box col: j // 3.
                # Each row skipped is 3 boxes (i // 3) * 3 + (j // 3)
                if cell in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                boxes[(i // 3) * 3 + (j // 3)].add(cell)
        
        return True
```

## Results

- **Status:** ✅ Accepted
- **Runtime:** 0 ms (Beats 100.00%!)
- **Memory:** 19.48 MB (Beats 27.86%)

## Key Improvements from Attempt 1

1. **Single Pass:** Instead of 3 separate iterations (rows, columns, boxes), we now iterate through the board only once
2. **Efficient Data Structures:** Used 3 lists of sets (one for each constraint type) that are indexed directly
3. **Time Complexity:** Still O(1) due to fixed 9x9 board, but with better constant factors
4. **Cleaner Code:** More Pythonic and easier to understand

## What I Learned

- Combining multiple validation checks in a single pass can significantly improve performance
- Pre-allocating data structures (list comprehension with sets) is more efficient than creating them on-the-fly
- The box index formula `(i // 3) * 3 + (j // 3)` elegantly maps 2D coordinates to a box number
- Even when Big-O complexity is the same (O(1)), reducing the number of passes makes a real difference (0ms vs multiple ms)
