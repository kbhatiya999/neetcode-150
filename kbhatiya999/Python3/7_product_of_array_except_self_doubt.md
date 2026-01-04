# Problem 7: Product of Array Except Self - Doubts & FAQs

## Q1: Why can't we use division?

**Answer:**

The constraint specifically forbids division to teach about alternative approaches. Division by zero also becomes problematic if the array contains 0.

---

## Q2: Why does the prefix/postfix approach work?

**Answer:**

For any element at index `i`, the product excluding `i` is:
- (Product of all elements before i) × (Product of all elements after i)

This is exactly what our prefix and suffix products give us!

---

## Q3: Why do we need two passes instead of one?

**Answer:**

First pass builds prefix products (left to right). We can't compute suffix products simultaneously because we haven't seen elements to the right yet. The second pass handles suffix products (right to left).

---

## Q4: What if the array contains zeros?

**Answer:**

The algorithm handles zeros correctly:
- If one zero: All products except at zero's position are 0
- If multiple zeros: All products are 0
- Our algorithm naturally handles this because 0 propagates through multiplication

**Example:** `[2, 0, 4]`
- Index 0: 0 × 4 = 0 ✓
- Index 1: 2 × 4 = 8 ✓
- Index 2: 2 × 0 = 0 ✓

---

## Q5: What about negative numbers?

**Answer:**

Negative numbers are handled correctly. Multiplication rules still apply:
- Negative × Negative = Positive
- Negative × Positive = Negative

Our algorithm inherently preserves signs correctly.

---

## Q6: Why O(n) space excluding output?

**Answer:**

We only use:
- `prefix` and `suffix` variables (O(1))
- The output array (doesn't count per problem statement)

We don't create separate prefix/suffix arrays.

---

## Q7: Can we optimize further?

**Answer:**

No, O(n) time is optimal since we must examine every element at least once. O(1) space (excluding output) is also optimal.

---

## Q8: How does this compare to calculating total product?

**Answer:**

**Naive approach (with division):**
1. Calculate total product
2. Divide total by each element
- Problem: Division by zero breaks this
- Problem: What if no zeros but we want to avoid division?

**Our approach:**
- Works with zeros
- No division needed
- Still O(n) time

---

## Q9: What if array is empty or has one element?

**Answer:**

Constraints guarantee `2 <= nums.length`, so we don't need to handle these cases.

---

## Q10: Common mistakes to avoid

1. **Mistake:** Forgetting to update prefix/suffix in the loop
   - **Fix:** Update AFTER using the current value

2. **Mistake:** Using wrong loop direction for second pass
   - **Fix:** Second pass must be right-to-left

3. **Mistake:** Overwriting output array too early
   - **Fix:** Use intermediate prefix/suffix values

---

## Key Insights

✅ **Prefix-Postfix Pattern:** Useful for many array problems  
✅ **Two-Pass Strategy:** Sometimes problems need multiple passes  
✅ **No Division:** Forces us to think creatively  
✅ **Space-Optimal:** Uses only O(1) extra space  
✅ **Handles Edge Cases:** Works with zeros and negatives  
