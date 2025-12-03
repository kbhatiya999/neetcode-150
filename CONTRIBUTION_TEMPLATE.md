# Contributing to NeetCode 150 Solutions

Thank you for your interest in contributing to this repository! This guide explains the expectations and structure for adding your solutions.

## Repository Organization

Solutions are organized by **username** and **programming language** in the following structure:

```
username/
├── Python3/
│   ├── 1_contains_duplicate.py
│   ├── 1_contains_duplicate.md
│   ├── 2_valid_anagram.py
│   ├── 2_valid_anagram.md
│   └── ...
├── Java/
│   ├── 1_contains_duplicate.java
│   ├── 1_contains_duplicate.md
│   └── ...
└── ...
```

## File Naming Convention

All files must follow this naming pattern:
- **Python files**: `<problem_number>_<problem_name>.py`
- **Documentation files**: `<problem_number>_<problem_name>.md`
- - **Doubt/Questions files**: `<problem_number>_<problem_name>_doubt.md` (optional)

**Examples:**
- `1_contains_duplicate.py` and `1_contains_duplicate.md`
- `2_valid_anagram.py` and `2_valid_anagram.md`
- `217_contains_duplicate.py` (if using LeetCode problem numbers)

## Python Solution File Requirements

Each Python solution file should include:

1. **Docstring** - Problem description and approach
2. **Function signature** - Clear and well-defined
3. **Solution code** - Well-commented and optimized
4. **Test cases** - Examples showing usage

**Template:**

```python
"""
LeetCode Problem: <Problem Title>
Problem Number: <Number>

Problem Description:
<Brief description of the problem>

Time Complexity: O(...)
Space Complexity: O(...)
"""

def solution_function(input_param):
    """
    Solution approach:
    - <Step 1>
    - <Step 2>
    - <Step 3>
    """
    # Implementation code
    pass

# Test cases
if __name__ == "__main__":
    # Example 1
    print(solution_function(input1))  # Expected output
    
    # Example 2
    print(solution_function(input2))  # Expected output
```

## Markdown Documentation File Requirements

Each markdown file should provide comprehensive documentation including:

### Required Sections

1. **Problem Title & Link**
   - Problem name and LeetCode link

2. **Problem Description**
   - Complete problem statement

3. **Constraints**
   - Input/output constraints and limitations

4. **Examples**
   - At least 3 test case examples with input and output

5. **Solution Approach**
   - Explanation of the algorithm/approach
   - Step-by-step breakdown
   - Why this approach was chosen

6. **Complexity Analysis**
   - Time Complexity analysis
   - Space Complexity analysis

7. **Implementation**
   - Full code implementation

8. **Alternative Approaches** (Optional)
   - Other ways to solve the problem
   - Pros and cons of each approach

9. **Key Insights** (Optional)
   - Important observations about the problem
   - Edge cases to consider

10. **Submission Details**
    - LeetCode submission status (Accepted, Runtime, Memory)
    - Date of submission

11. **Related Problems** (Optional)
    - Similar or related problems

12. **Tags**
    - Problem tags (e.g., Array, Hash Table, String)

**Example markdown structure:**

```markdown
# LeetCode XXX: Problem Title

## Problem
[Link to LeetCode problem]

Complete problem description...

## Constraints
- Constraint 1
- Constraint 2

## Examples
### Example 1
- Input: ...
- Output: ...

### Example 2
- Input: ...
- Output: ...

### Example 3
- Input: ...
- Output: ...

## Solution Approach
Explanation of the approach...

## Complexity Analysis
- **Time Complexity**: O(...)
- **Space Complexity**: O(...)

## Implementation
\`\`\`python
# Your code here
\`\`\`

## Alternative Approaches
### Approach 1: ...
...

### Approach 2: ...
...

## Key Insights
- Insight 1
- Insight 2

## Submission Details
- **Status**: ✅ Accepted
- **Runtime**: XXX ms
- **Memory**: XXX MB
- **Date**: YYYY-MM-DD

## Related Problems
- LeetCode XXX: Problem Name
- LeetCode XXX: Problem Name

## Tags
Array, Hash Table, String
```


## Doubt/Questions File Requirements

For each problem, you can optionally create a `*_doubt.md` file to document any doubts, questions, or challenging aspects of the problem.

**File Naming:**
- `<problem_number>_<problem_name>_doubt.md`
- **Example:** `1_contains_duplicate_doubt.md`

**File Content:**

Each doubt file should contain:

### Purpose
This file is for documenting:
- Confusing aspects of the problem statement
- Edge cases that were difficult to identify
- Common mistakes and pitfalls
- Questions about the optimal approach
- Insights learned while solving

### Recommended Structure

```markdown
# Problem XXX: Problem Name - Doubts & Questions

## Questions I Had
1. **Question 1**: Description of the question
   - How I resolved it
   - Key learning

2. **Question 2**: Description of the question
   - How I resolved it
   - Key learning

## Confusing Parts
- **Confusion 1**: What was confusing
  - Clarification
  - Why it matters

- **Confusion 2**: What was confusing
  - Clarification
  - Why it matters

## Edge Cases I Missed
- Edge case 1 and how to handle it
- Edge case 2 and how to handle it

## Common Mistakes to Avoid
1. Mistake 1 - how to avoid it
2. Mistake 2 - how to avoid it

## Resources That Helped
- Resource 1 and why it was useful
- Resource 2 and why it was useful
```

### Optional but Recommended
This file is **optional** for each problem, but highly recommended for:
- Complex problems where multiple approaches exist
- Problems where the solution wasn't immediately obvious
- Problems where you struggled initially
- Problems with tricky edge cases

### Quality Standards
- Honest documentation of your learning process
- Clear explanation of what was confusing and why
- Practical solutions to resolve doubts
- Helpful for others facing similar challenges


## How to Contribute

1. **Create a new directory** under your username and language:
   ```
   username/Python3/
   ```

2. **Create solution file** with the correct naming convention:
   ```
   1_problem_name.py
   ```

3. **Create corresponding markdown** documentation:
   ```
   1_problem_name.md
   ```

4. **Commit with a descriptive message:**
   ```
   git commit -m "Add LeetCode XXX: Problem Title solution in Python3"
   ```

5. **Create a pull request** with details about your solution

## Quality Standards

- ✅ Solutions must be **accepted on LeetCode** (all test cases pass)
- ✅ Code must be **well-commented** and easy to understand
- ✅ Both `.py` and `.md` files must be created together
- ✅ File names must follow the naming convention
- ✅ Markdown documentation must be comprehensive
- ✅ Include complexity analysis
- ✅ No plagiarism - solutions must be your own work

## Tips for Better Contributions

- Run your solution against the test cases before submitting
- Optimize your solution for time and space complexity
- Explain your approach clearly in the markdown
- Consider edge cases and mention them in insights
- Include multiple examples in documentation
- Keep code readable with proper formatting and comments

## Contact & Support

If you have questions about the contribution process, please:
- Open an issue on GitHub
- Check existing contributions for examples
- Review the repository structure

Thank you for contributing! 🚀
