class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            cords = [0]*26
            for letter in word:
                cords[ord(letter)-ord('a')]+=1
            print(cords)
            joined_cords = "#".join(map(str,cords))
            if joined_cords not in hash_map:
                hash_map[joined_cords] = []
            hash_map[joined_cords].append(word)
        print(hash_map)
        return list(hash_map.values())