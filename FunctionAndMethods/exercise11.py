# What will the code do? 
# It will print out 42, 3, 2. 3 and 2 because only one argument was passed so the default values were used for the other two parameters

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)