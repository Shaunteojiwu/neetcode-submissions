class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        nums=sorted(nums)
        target=0
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==target:
                    dic[tuple([nums[i],nums[left],nums[right]])]=0
                # elif nums[i]+nums[left]+nums[right]<target:
                    left+=1
                # else:
                    right-=1
        return list(dic.keys())
            
        