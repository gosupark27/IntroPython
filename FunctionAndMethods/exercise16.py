def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Identify all function names, parameters, line number
# Line 1 - multiply, left, right
# Line 2 - left, right used as local variables 
# Line 4 - get_num, prompt
# Line 5 - prompt used a local variable 
# line 5 - float, input 
# line 7, 8 - used get_num
# line 9 - used multiply 
# line 10 - print 