class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=[-s for s in stones]
        heapq.heapify(s)
        while len(s)>1:
            y=-heapq.heappop(s)
            x=-heapq.heappop(s)

            if y!=x:
                heapq.heappush(s,-(y-x))
        return -s[0] if s else 0


        