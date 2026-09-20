class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        maximum=1
        maxval=nums[0]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            if freq[i]>=maximum:
                maximum=freq[i]
                maxval=i
        return maxval
        