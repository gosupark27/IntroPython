# What will the code do? 
# An error will be raised because any parameters that follows a default parameter must also be given a default value 

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)