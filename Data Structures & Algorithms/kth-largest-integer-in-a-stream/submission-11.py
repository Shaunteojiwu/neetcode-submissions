import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k_largest=k
        self.listnums=nums
        heapq.heapify(self.listnums)

        while len(self.listnums)>self.k_largest:
            heapq.heappop(self.listnums)


        

    def add(self, val: int) -> int:
        self.value=val
        #self.listnums.append(val)
        heapq.heappush(self.listnums, self.value)
        #heapq.heapify(self.listnums)
        # If the heap exceeds size k, pop the smallest element off the top
        if len(self.listnums) > self.k_largest:
            heapq.heappop(self.listnums)

        return self.listnums[0]
