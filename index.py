num1= input("Enter the first number: ")
num2= input("Enter the second number: ")
operation= input("Enter an operation(+,-,*,/): ")

if operation == '+':
  result = num1 + num2
  print({num1} + {num2} = {result})

elif operation == '-'
  result = num1 - num2
  print({num1} - {num2} = {result})

elif operation == '*'
  result = num1 * num2
  print( {num1} * {num2} = {result})

elif operation == '/'
if num2 != 0:
  result = num1 / num2
  print( {num1} / {num2} = {result})
else:
  print("Error: division by zero is not allowed.")  

#invalid operation check
else:
  print(" Invalid operatioon. please choose +, -, *, or /.")