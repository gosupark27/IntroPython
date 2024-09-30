def capitalize_all_longstring(string):
    return string.upper() if len(string) > 10 else string

def print_string(string):
    print(capitalize_all_longstring(string))

print_string('abcd')
print_string('abcdefghij')
print_string('hello world')
print_string('goodbye')
