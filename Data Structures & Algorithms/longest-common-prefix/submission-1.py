class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        minlen=len(strs[0])
        for i in strs:
            if len(i)<minlen:
                minlen=len(i)
        for i in range(minlen):
            count=0
            for s in strs:
                if s[i] == strs[0][i]:
                    count+=1
            if count==len(strs):
                ans+=s[i]
            else:
                return ans
        return ans
