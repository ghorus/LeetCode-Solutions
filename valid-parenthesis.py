# Intuition
# My first thought was having 2 pointers, but under Neetcode, it's supposed to be a stack problem. So how can i implement the stack data structure to get the answer i need? I'm sure this is how debuggers work when they detect and tell you you're missing a parentheses. The actual solution is to:
# -iterate through the string
# -stack it onto a list,
# -if the iteration comes across a closing bracket, pop it if it's the last thing on the list
# note: this works because you HAVE to always come across at least 1 closing and open bracket that are right next to each other, in a valid bracket. After coming across that, it'll pop off everything in the list if it's a valid bracket.
# So with this implementation, let's say we have the following bracket:
# [ ( ){ } ]
# With our method, we'd go all the way up to the first closing parenthesis, and pop off the opening from the list.

# Approach
# iterate through the string and add each string to the list one by one,opening bracket if the current iteration is a closing bracket.

stack = []
for i in s:
    if not stack:
        stack.append(i)
    elif stack[-1] == "(" and i ==")":
        stack.pop()
    elif stack[-1] == "[" and i =="]":
        stack.pop()
    elif stack[-1] == "{" and i =="}":
        stack.pop()
    else:
        stack.append(i)
return len(stack) == 0