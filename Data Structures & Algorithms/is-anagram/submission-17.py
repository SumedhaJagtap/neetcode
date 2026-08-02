class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cords = [0]*26

        for i in s:
            cords[ord(i)-ord('a')]+=1
        for i in t:
            cords[ord(i)-ord('a')]-=1
        return all(i==0 for i in cords)
        