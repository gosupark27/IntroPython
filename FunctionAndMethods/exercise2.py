# What does this program print? Why? 
# The program prints out bar because the reassignment of foo happens at the function level 
# and when foo is called at the main/global scope, it will find that foo is assigned the value of bar


foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)