# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

numbers = [numbers1, numbers2, numbers3, numbers4, numbers5]

for n in numbers:
    print(f"{n}:\n{3 in n}")






# Not utilizing the functions I learned from this chapter...
def check_for_3(nums):
    for n in nums:
        if n == 3:
            return True
    return False

def print_results(nums):
    has_three = check_for_3(nums)
    print(f"{nums} contains the number 3.\nTrue" if has_three else f"{nums} does not contain the number 3.\nFalse") 

# for num in numbers:
#     print_results(num)
