# determine which of the following lists do not contain any numbers that are divisible by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

def isNotDivisible(list):
    isDivisible = all(remainders_5(list))
    print(f"{list} does not contain any number that is divisible by 5: {isDivisible}")

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

isNotDivisible(numbers_1)
isNotDivisible(numbers_2)
isNotDivisible(numbers_3)
isNotDivisible(numbers_4)

