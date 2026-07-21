class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        left=0
        longest=0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            longest=max(longest,right-left+1)
#         # left=0
#         # length_of_string=0
#         dic={}
#         left=0
#         length_of_string=1
#         current_longest=0
#         for right in range(len(s)):
#             if s[right] not in dic:
#                 length_of_string+=1
#                 dic[s[right]]=1
#                 current_longest=length_of_string
#             elif s[right] in dic:
#                 length_of_string=right-left
#                 current_longest=max(current_longest,length_of_string)
#                 #left=right
#                 left+=1
#         return current_longest

