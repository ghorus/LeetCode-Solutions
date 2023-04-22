# Intuition
# I totally misread the question, I thought I had to do something super extra and weird with the first thing that was said on the prompt:
# MinStack() initializes the stack object. This just means the class object is initialized. The push, pop properties are for 
# lists(can't pop tuples or dictionaries) so it makes sense to put a list in the global/init section

def __init__(self):
        self.minStack = []
        

def push(self, val: int) -> None:
    return self.minStack.append(val)
    #add to list
    

def pop(self) -> None:
    if self.minStack:
        return self.minStack.pop()
    #pop off top of list if there are elements in list

def top(self) -> int:
    return self.minStack[-1]
    #return top value

def getMin(self) -> int:
    if self.minStack:
        return min(self.minStack)
    #retrieve minimum value if not empty list
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()