class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        hash_map = defaultdict(list)

        for word in strs:
            cords = [0]*26
            for letter in word:
                cords[ord(letter)-ord('a')]+=1
            sorted_key = tuple(cords)
            hash_map[sorted_key].append(word)
        return list(hash_map.values())