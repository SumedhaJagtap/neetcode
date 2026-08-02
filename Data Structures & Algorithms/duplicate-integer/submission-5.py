class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i]=True
            else:
                return True
        return False