class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        #return dict.values().largest(k)
        sorted_val=sorted(dict.keys(), key=lambda x: dict[x], reverse=True)
        return sorted_val[:k]

                

        