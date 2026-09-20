class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i in freq:
                return True
            freq[i]=0
        return False