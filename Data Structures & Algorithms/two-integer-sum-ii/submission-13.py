# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         dic={}
#         for idx,i in enumerate(numbers):
#             if i not in dic:
#                 dic[i]=idx
#         for idx,i in enumerate(numbers):
#             complement=target-i
#             if complement in dic:
#                 return [dic[i]+1,dic[complement]+1]

# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         left,right=0,len(numbers)-1
#         while left<right:
#             if numbers[left]+numbers[right]==target:
#                return [left+1,right+1]
#             elif numbers[left]+numbers[right]<target:
#                 left+=1
#             else:
#                 right-=1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map={}
        for idx,i in enumerate(numbers):
            complement=target-i
            if complement in map:
                return [map[complement]+1,idx+1]
            map[i]=idx
        
                



        