# FAQ & Doubts: LeetCode 36 - Valid Sudoku

## Common Questions

### Q1: Why don't we need to solve the entire Sudoku?
**A:** The problem only asks us to validate the partially filled board. We don't need to complete the solution, just check that what's already there follows the rules.

### Q2: How do we calculate the 3x3 box index?
**A:** For a cell at position (row, col), the box index is `(row // 3, col // 3)`. This divides the 9x9 grid into nine 3x3 boxes. Alternatively, you can use `row // 3 * 3 + col // 3` if using a single number.

### Q3: Why use sets instead of a 2D array?
**A:** Sets provide O(1) lookup time, which is more efficient. A 2D array would work but requires more memory (9x9=81 elements per structure vs. variable size with sets).

### Q4: Can we use the same set for rows, columns, and boxes?
**A:** No, because a digit can appear in the same row at different columns, same column at different rows, and same box multiple times. We need separate tracking for each constraint.

### Q5: What about using tuples as keys in a dictionary instead of sets?
**A:** Yes, you can! Instead of three separate sets, you could use a dictionary with tuples as keys: `{('row', 5, '3'), ('col', 2, '3'), ('box', 1, '3')}`.

### Q6: Why is the time complexity O(1) and not O(81)?
**A:** The board size is always 9x9 (81 cells), which is a constant. O(81) simplifies to O(1) because it's not dependent on input size.

### Q7: Can the board have '.' in every cell?
**A:** Yes, a completely empty board is valid. The loop will just skip all cells and return True.

### Q8: What if we need to find which cell is invalid?
**A:** You would need to return the position instead of just True/False, and track it during validation.

### Q9: Is duplicate checking case-sensitive?
**A:** All digits are numbers ('1'-'9'), so case sensitivity isn't relevant. '.' is used for empty cells.

### Q10: Can we modify the input board?
**A:** Technically yes, but it's not a good practice. Using external data structures (sets) is better.

## Common Mistakes

### Mistake 1: Using the same set for all constraints
```python
# WRONG - can't track row, col, box separately
seen = set()
for r in range(9):
    for c in range(9):
        if board[r][c] != '.':
            seen.add((board[r][c], r, c))  # Not enough info
```

### Mistake 2: Not handling '.' correctly
```python
# WRONG - will cause errors
if board[r][c] in rows[r]:  # '.' might be in set!
```

### Mistake 3: Incorrect box calculation
```python
# WRONG - treats 3x3 boxes incorrectly
box = (r, c)  # This is the cell, not the box!
# CORRECT:
box = (r // 3, c // 3)
```

### Mistake 4: Returning False immediately
```python
# INEFFICIENT - not necessarily wrong
if digit in rows[r]:
    return False  # Could continue checking
# BETTER: Use all checks and return at end
```

## Edge Cases

1. All cells filled validly: `True`
2. All cells empty: `True`
3. Duplicate in row: `False`
4. Duplicate in column: `False`
5. Duplicate in 3x3 box: `False`
6. Valid partial board (single digit): `True`
7. All cells have '.': `True`
8. Mixed valid state: depends on content

## Optimization Tips

1. **Early termination:** Return `False` as soon as invalid digit found
2. **Space optimization:** Use bit masks instead of sets (only 9 bits needed)
3. **Combine structures:** Use a single dict with compound keys
4. **Ignore empty cells:** Skip '.' to avoid processing overhead

## Related Concepts

- **Sudoku Solver:** Uses backtracking to fill in missing numbers
- **Constraint propagation:** Reduces possible values for each cell
- **Bit masking:** Efficient representation of present digits
- **N-Queens problem:** Similar constraint satisfaction
- **Graph coloring:** Similar validation approach
