class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for idx,i in enumerate(nums):
            complement=target-i
            if complement in map:
                return [map[complement],idx]
            map[i]=idx
        