class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            cords = [0]*26
            for letter in word:
                cords[ord(letter)-ord('a')]+=1
            sorted_key = "".join(sorted(word))
            if sorted_key not in hash_map:
                hash_map[sorted_key] = []
            hash_map[sorted_key].append(word)
        return list(hash_map.values())