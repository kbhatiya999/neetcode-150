"""LeetCode 36: Valid Sudoku

Determine if a 9x9 Sudoku board is valid.
Only the filled cells need to be validated.

Rules:
1. Each row must contain digits 1-9 without duplicates
2. Each column must contain digits 1-9 without duplicates
3. Each 3x3 sub-box must contain digits 1-9 without duplicates

Approach: Use sets to track seen digits in rows, columns, and boxes

Time Complexity: O(1) - Fixed 9x9 grid
Space Complexity: O(1) - Fixed number of sets
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                
                box_idx = (i // 3) * 3 + (j // 3)
                if cell in boxes[box_idx]:
                    return False
                boxes[box_idx].add(cell)
        
        return True
