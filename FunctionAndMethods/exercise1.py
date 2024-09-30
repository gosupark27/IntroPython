# After running the program, will get a NameError: foo is not defined. 
# Since variable foo is initialized at the function level, and the call for foo happens outside of the function scope,
# foo is not accessible. 

def set_foo():
    foo = 'bar'

set_foo()
print(foo)