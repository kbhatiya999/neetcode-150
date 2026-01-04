# FAQ / Doubts: 3Sum

## Q1: Why do we need to sort the array first?
**A:** Sorting allows us to:
1. Handle duplicates efficiently by checking if the current element is same as the previous one
2. Use the two-pointer approach which requires sorted order
3. Skip redundant work when nums[i] > 0 (all subsequent elements will be positive)

## Q2: What's the time complexity and why?
**A:** O(n²) because:
- Outer loop: O(n)
- For each element, two-pointer search: O(n)
- Overall: O(n) + O(n log n) sorting ≈ O(n²)

## Q3: How do we avoid duplicate triplets in the result?
**A:** By:
1. Sorting the array first
2. Skipping duplicate values at all three loop levels:
   - Skip duplicate values for the fixed element (i)
   - Skip duplicate values for left pointer
   - Skip duplicate values for right pointer
3. Once we find a valid triplet, we move both pointers to avoid processing the same pair again

## Q4: When should we move left and right pointers?
**A:**
- If current_sum == 0: We found a triplet! Move left pointer (or right) to find more triplets
- If current_sum < 0: We need a larger sum, so move left pointer right
- If current_sum > 0: We need a smaller sum, so move right pointer left

## Q5: What if the array has all zeros?
**A:** The algorithm will still work correctly. It will return [[0,0,0]] because:
- When nums[i] = 0, we need nums[j] + nums[k] = 0
- All zeros satisfy this
- Duplicate-skipping logic ensures we add only one [0,0,0] triplet

## Q6: What's the space complexity?
**A:** O(1) or O(n) depending on:
- If we count only the output space (excluding the result list): O(1)
- If we count sorting space: O(n) for merge sort or O(log n) for quicksort
- Typically considered O(1) for the algorithm itself

## Q7: Can we solve this without sorting?
**A:** Yes, using a hash set approach with O(n²) time and O(n) space, but sorting + two-pointer is more efficient and widely preferred for interviews

## Q8: Edge cases to consider
- All positive numbers: return []
- All negative numbers: return []
- Array with only 3 elements
- Array with duplicates
- Array with zeros
- Array smaller than 3 elements
