# What will this code do?
# It will print out 42, 3.141592 and 2. It will print out 2 because no argument was given for the third parameter so the default value was used 

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)