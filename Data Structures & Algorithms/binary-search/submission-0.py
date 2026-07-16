class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx,i in enumerate(nums):
            if i==target:
                return idx
        return -1
        