class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left=0
        # length_of_string=0
        dic={}
        left=0
        length_of_string=1
        current_longest=0
        for right in range(len(s)):
            if s[right] not in dic:
                length_of_string+=1
                dic[s[right]]=1
            elif right in dic:
                current_longest=max(current_longest,length_of_string)
                left=right
        return current_longest
