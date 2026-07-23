class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char=set()
        left=0
        max_length=0
        replacement=k
        for right in range(len(s)):
            while s[right] not in char:
                left=right
                if replacement!=0:
                    replacement-=1
                    max_length+=1
               
                # if replacement==0:
                #     left+=1
                   
            set.add(s[right])
            max_length=max(max_length,right-left+1)

        