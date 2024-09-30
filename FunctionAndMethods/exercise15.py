# Classify identifiers as global, local, built-in 
# Global: multiply, get_numb, first_number, second_number, product 
# Local: left, right, prompt
# Built-in: float, input, print 

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')