my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for ol in my_list:
    for num in ol:
        if num % 2 == 0:
            print(num)