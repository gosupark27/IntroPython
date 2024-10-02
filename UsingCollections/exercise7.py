# Write code to replace all : characters with +

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_list = list(info)


def modify_string(string):
    old_string = string.split(':')
    new_string = '+'.join(old_string)
    return new_string
# Older version of modify_string 
    index = 0
    for c in my_list:
        if c == ':':
            my_list[index] = '+'
        index += 1
    return my_list

# info = ''.join(modify_string(info_list)) - Using the older version of modify_string()
print(f"modified info\n{modify_string(info)}")

new_info = info.replace(":", "+")
print(f"Using the replace method\n{new_info}")