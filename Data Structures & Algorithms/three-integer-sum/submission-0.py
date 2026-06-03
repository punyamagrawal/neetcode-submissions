class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        for k in range(len(nums)):
            i=k+1
            j=len(nums)-1
            while i<j:
                if (nums[i]+nums[j]+nums[k]==0) and (k==0 or nums[k]!=nums[k-1]):
                        ans=[nums[k],nums[i],nums[j]]
                        result.append(ans)
                        i+=1
                        j-=1
                        while i<j and nums[i] == nums[i-1]:
                             i+=1
                        while i<j and nums[j] == nums[j+1]:
                             j-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    i+=1
                else:
                    j-=1
        return result