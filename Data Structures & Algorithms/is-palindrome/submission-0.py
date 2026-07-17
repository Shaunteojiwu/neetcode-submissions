class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(str)
        while left<right:
            if str[left]==str[right]:
                left+=1
                right-=1
            return False

        