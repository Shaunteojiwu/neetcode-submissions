import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k_largest=k
        self.listnums=nums
        heapq.heapify(self.listnums)

        while len(self.listnums)>k:
            heapq.heappop(self.listnums)


        

    def add(self, val: int) -> int:
        self.value=val
        #self.listnums.append(val)
        heapq.heappush(self.listnums, self.value)
        heapq.heapify(self.listnums)
        return self.listnums[0]
