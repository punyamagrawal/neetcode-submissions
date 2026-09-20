class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(0,l):
            nums.append(nums[i])

        return nums