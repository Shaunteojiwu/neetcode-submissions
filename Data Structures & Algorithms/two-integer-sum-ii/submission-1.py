class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for idx,i in enumerate(numbers):
            if i not in dic:
                dic[i]=idx
        for idx,i in enumerate(numbers):
            complement=target-i
            if complement in dic:
                return [ dic[i],dic[complement]]
                



        