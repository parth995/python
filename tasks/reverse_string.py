from stack import Stack

def reverse_str(stack, string):
    for i in range(len(string)):
        stack.push(string[i])
        # print(string[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str = rev_str + stack.pop()
    return rev_str

s = Stack()
print(reverse_str(s, "Hackzz"))