class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        k=[]
        #while
        for p,s in cars:
            time=(target-p)/s
            if not k or time>k[-1]:
                    k.append(time)
        return len(k)

        #k.append(cars)

    
        