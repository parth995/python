from stack import Stack

def convert_int_to_bin(dec_num):

    if dec_num == 0:
        return 0

    while dec_num != 0:
        reminder = dec_num % 2 # store in stack
        stack.push(reminder)
        dec_num = dec_num // 2

    bin_num = ""
    while not stack.is_empty():
        bin_num = bin_num + str(stack.pop())
    return bin_num

stack = Stack()
print(convert_int_to_bin(15))
print(convert_int_to_bin(10))