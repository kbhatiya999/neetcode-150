# Problem 5: Top K Frequent Elements

## LeetCode Link
[LeetCode 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem Statement

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

You must write an algorithm that runs in better than O(n log n) time complexity.

### Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= number of unique elements in nums
- It is **guaranteed** that the answer is **unique**

### Example

**Input:** nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

**Input:** nums = [4,1,1,1,2,2,3], k = 2
**Output:** [1,2]

---

## Approach: Bucket Sort (O(n) Time Complexity)

### Key Insight
Instead of using a heap or sorting (which would be O(n log n)), we can use **bucket sort** since the frequency of any element is bounded by the array length. Elements with the same frequency are grouped in buckets indexed by their frequency.

### Algorithm Steps

1. **Count Frequencies:** Use a dictionary to count how many times each unique element appears
2. **Create Buckets:** Create an array of buckets where bucket[i] contains all elements with frequency i
3. **Collect Results:** Iterate from the highest frequency buckets downward and collect elements until we have k elements

### Why This Works
- Maximum frequency any element can have is `n` (array length)
- We can create buckets indexed 0 to n to hold elements by frequency
- By collecting from highest frequency buckets first, we efficiently find the k most frequent elements

---

## Solution Code

```python
from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using bucket sort.
    
    Time Complexity: O(n) - single pass to count + single pass through buckets
    Space Complexity: O(n) - for frequency counter and buckets
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    
    # Step 1: Count frequencies of each element
    freq_count = Counter(nums)
    
    # Step 2: Create buckets where bucket[i] contains elements with frequency i
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in freq_count.items():
        buckets[freq].append(num)
    
    # Step 3: Collect k elements from highest frequency buckets
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result
```

---

## Complexity Analysis

### Time Complexity: O(n)
- Counting frequencies: O(n) - single iteration through array
- Creating buckets and distributing elements: O(n) - iterate through unique elements
- Collecting results: O(n) - worst case iterate through all buckets
- **Total: O(n)** ✓ (Meets follow-up requirement of better than O(n log n))

### Space Complexity: O(n)
- Frequency counter: O(unique elements) ≤ O(n)
- Buckets array: O(n + 1) for indices 0 to n
- Result list: O(k) ≤ O(n)

---

## Example Walkthrough

### Example 1: nums = [1,1,1,2,2,3], k = 2

**Step 1 - Count frequencies:**
```
freq_count = {1: 3, 2: 2, 3: 1}
```

**Step 2 - Create buckets:**
```
buckets[0] = []
buckets[1] = [3]
buckets[2] = [2]
buckets[3] = [1]
buckets[4] = []
buckets[5] = []
buckets[6] = []
```

**Step 3 - Collect from highest frequency:**
- From buckets[3]: collect 1 → result = [1]
- From buckets[2]: collect 2 → result = [1, 2]
- k = 2 reached, return [1, 2]

---

## Alternative Approaches

### 1. Heap Approach (O(n log k))
```python
from heapq import heappush, heappop
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_count = Counter(nums)
    
    # Min heap of size k
    heap = []
    for num, freq in freq_count.items():
        heappush(heap, (freq, num))
        if len(heap) > k:
            heappop(heap)
    
    return [num for freq, num in heap]
```
- **Time:** O(n log k) - better for small k
- **Space:** O(k)
- Less optimal than bucket sort but acceptable

### 2. QuickSelect Approach (O(n) average)
```python
def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_count = Counter(nums)
    unique = list(freq_count.keys())
    
    def quickSelect(left, right, k_smallest):
        if left == right:
            return
        
        # Partition logic here...
        pivot_index = partition(left, right)
        
        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            quickSelect(left, pivot_index - 1, k_smallest)
        else:
            quickSelect(pivot_index + 1, right, k_smallest)
    
    quickSelect(0, len(unique) - 1, len(unique) - k)
    return unique[len(unique) - k:]
```
- **Time:** O(n) average, O(n²) worst case
- **Space:** O(1) if not counting result

---

## Key Insights

1. **Frequency Constraint:** The maximum frequency is limited to array length, making bucket sort ideal
2. **No Sorting Needed:** By using frequency as index, we avoid comparison-based sorting
3. **Early Termination:** We can stop as soon as we collect k elements
4. **Order Independence:** Return order doesn't matter, so we don't need to sort results

---

## Related Problems

- **LeetCode 1:** Two Sum
- **LeetCode 242:** Valid Anagram
- **LeetCode 49:** Group Anagrams
- **LeetCode 355:** Design Twitter (uses frequency concept)
- **LeetCode 692:** Top K Frequent Words (similar approach)
- **LeetCode 503:** Next Greater Element II (frequency usage)

---

## Tips for Interview

✅ **Do:**
- Clearly explain the frequency constraint (max frequency = array length)
- Start with a brute force approach, then optimize
- Mention the O(n) time complexity and how it beats the O(n log n) requirement
- Test with edge cases (all same frequency, k=1, etc.)
- Explain trade-offs between bucket sort vs heap vs quickselect

❌ **Avoid:**
- Using sorting without justification
- Forgetting about the follow-up requirement
- Not handling edge cases properly
- Assuming elements are unique (they're not)

---

## Edge Cases

1. **k equals number of unique elements:** Return all unique elements
2. **All elements have same frequency:** Return any k elements
3. **Single element array:** Return that element
4. **k = 1:** Return the most frequent element
5. **Negative numbers:** Handled naturally by Counter and buckets
