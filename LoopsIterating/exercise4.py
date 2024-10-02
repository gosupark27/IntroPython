my_list = [6, 3, 0, 11, 20, 4, 17]

# while loop prints even
index = 0
while index < len(my_list):
    num = my_list[index]
    if num % 2 == 0: 
        print(num)
    index += 1

# for loop prints odd 
for num in my_list:
    if num % 2 != 0: 
        print(num)