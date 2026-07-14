class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapping={}
        for i in s:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1

        for i in t:
            if i not in mapping or mapping[i]==0:
                return False
            else:
                mapping[i]-=1
        return True


        