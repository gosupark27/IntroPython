my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

list_comp = [num 
             for ol in my_list
             for num in ol
             if num % 2 == 0]
print(list_comp)

outer_loop_index = 0
even_list = list()
while outer_loop_index < len(my_list):
    nested_list_index = 0
    while nested_list_index < len(my_list[outer_loop_index]):
        num = my_list[outer_loop_index][nested_list_index]
        if num % 2 == 0:
            even_list.append(num)
        nested_list_index += 1
    outer_loop_index +=1

print(even_list)