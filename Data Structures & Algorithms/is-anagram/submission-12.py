class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map_s = {}
        hash_map_t = {}
        for i , j in zip(s,t):
            hash_map_s[i] = 1 + hash_map_s.get(i,0)
            hash_map_t[j] = 1 + hash_map_t.get(j,0)
        return hash_map_s==hash_map_t

        
        