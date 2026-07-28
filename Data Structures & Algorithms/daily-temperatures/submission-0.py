class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack=[]
        # output=[]
        # while not stack or stack[i]>temperatures[i+1]:
        #     stack.append(temperatures[i])
        #     for i in range(len(temperatures)):
        #         output.append(len(stack))
        #     for i in len(stack):
        #         stack.pop()
            # if stack and stack[i]<temperatures[i+1]:
            #     output.append(len(stack))
            #     stack.pop(temperature[1])
            #     #output.append(len(stack)-1)
            res=[0]*len(temperatures)
            stack=[]

            for i,t in enumerate(temperatures):
                while stack and t>temperatures[stack[-1]]:
                    prev_i=stack.pop()
                    res[prev_i]=i-prev_i

                stack.append(i)
            return res

             
        