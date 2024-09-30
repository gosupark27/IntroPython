# What will the code do? 
# An error because there is one parameter that does not have a default value so at least one argument needs to be used

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()