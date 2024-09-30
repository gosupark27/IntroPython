# Identify all identifiers in the code
# multiply, left, right, get_num, prompt, firrst_number, second_number, product, float, input, print 

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')