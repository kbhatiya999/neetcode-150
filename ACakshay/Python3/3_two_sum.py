class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        hmap=defaultdict(list)
        for i,v in enumerate(nums):
            if target-v in hmap:
                return sorted([hmap[target-v][-1],i])
            else:
                hmap[v].append(i)
            
        
