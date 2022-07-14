# for _ in range(4):
#     print("Hello !!")

def addWithCarry(num1,num2): # Adding two numbers
  sum=num1+num2
  carry=0
  return sum,carry
s, _ = addWithCarry(1,5) # Calling function in two variables
print(s)

# Creating 3x3 field for Tic Tac Toe

field = [[' '] * 3 for _ in range(3)]
print(field)

