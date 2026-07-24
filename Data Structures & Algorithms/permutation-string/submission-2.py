class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # left=0
        # k=len(s1)
        if len(s1)>len(s2):
            return False

        need={}
        window={}
        for c in s1:
            need[c]=need.get(c, 0) + 1

        for i in range(len(s1)):
            window[s2[i]]=window.get(s2[i],0)+1
        
        if need==window:
            return True
        
        left=0

        for right in range(len(s1),len(s2)):
            window[s2[right]]=window.get(s2[right], 0) + 1
            window[s2[left]] -= 1
                        
            if window[s2[left]] == 0:
                        del window[s2[left]]
            left+=1
            if need==window:
                return True

        return False


        # for right in range(len(s2)):
        #     while right-1eft+1<=k and s2[right] in need:
        #         need[s2[right]]-1
            
        # left,right=0,len(s1)
        # dic={}
        # # k=len(s1)
        # for right in range(len(s1)):
        #     while s2[right] not in dic:
        #         dic[s2[right]]-=1
        #         k-=1

        #     dic[s1[right]]=dic.get([s1[right]],0)+1
            