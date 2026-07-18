class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for idx,i in enumerate(numbers):
            if i not in dic:
                dic[i]=idx
        for idx,i in enumerate(numbers):
            complement=target-i
            if complement in dic:
                return [ dic[i]+1,dic[complement]+1]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         map={}
#         for idx,i in enumerate(nums):
#             complement=target-i
#             if complement in map:
#                 return [map[complement],idx]
#             map[i]=idx
        
                



        