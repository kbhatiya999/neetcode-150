class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_map, t_map =defaultdict(int),defaultdict(int)
        if len(s)!=len(t):
            return False
        for i,j in zip(s,t):
            s_map[i]+=1
            t_map[j]+=1

        for key in s_map.keys():
            if s_map[key]!=t_map[key]:
                return False
        return True
            
        
