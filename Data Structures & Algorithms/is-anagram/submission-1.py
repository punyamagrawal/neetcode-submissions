class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sfreq = {}
        for i in s:
            if i in sfreq:
                sfreq[i]+=1
            else:
                sfreq[i]=1
        for i in t:
            if i in sfreq:
                sfreq[i]-=1
            else:
                return False
        for i in sfreq:
            if sfreq[i]!=0:
                return False
            continue
        return True
        