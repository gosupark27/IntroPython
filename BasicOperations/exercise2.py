number = 4936
ones = number % 10 
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000
print(f" The number is {number}. \n The one's place is: {ones} \n The ten's place is {tens} \n The hundred's place is: {hundreds} \n The thousand's place is {thousands}")