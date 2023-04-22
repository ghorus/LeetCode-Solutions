import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #keep stacking, pop off last two if come across operator
        #add back to list, that's how notation works, so even if you keep
        #going across a bunch of numbers, you're supposed to operate from right to
        #left
        stack = []
        for i in tokens:
            #if i is an operator, get the last 2 number in the stack and perform operation
            if i in "+-/*":
                a, b = stack.pop(), stack.pop()
            if i == "+":
                stack.append(b+a)
            elif i == "-":
                stack.append(b-a)
            elif i =="/":
                if b/a > 0:
                    stack.append(math.floor(b/a))
                else:
                    stack.append(math.ceil(b/a))
            elif i =="*":
                stack.append(b*a)
            else:
                stack.append(int(i))
        return stack[0]