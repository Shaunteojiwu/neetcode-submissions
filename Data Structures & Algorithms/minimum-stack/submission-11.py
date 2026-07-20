class MinStack:

    def __init__(self):     
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.value=val
        self.stack.append(self.value)
        if not self.minstack or self.value<=self.minstack[-1]:
            self.minstack.append(self.value)
        

    def pop(self) -> None:
        last_value=self.stack.pop()
        if last_value==self.minstack[-1]:
            self.minstack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
