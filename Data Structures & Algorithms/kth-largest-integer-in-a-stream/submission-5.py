import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k_largest=k
        self.listnums=nums
        heapq.heapify(self.listnums)

        while len(self.listnums)>k:
            heapq.push(self.listnums)


        

    def add(self, val: int) -> int:
        self.value=val
        self.listnums.append(val)
        heapq.heapify(self.listnums)
        return self.listnums[0]
