# Identify function names, method names, built-in names
# function name - say
# method name - lower, upper 
# built in - print, input, max

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))