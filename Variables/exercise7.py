# What happens when you run the following code? Why?
# The program prints out a greeting three times for Victor and then an additional three greetings for Nina. 
# Python does not support true constants, so it is up to the progammer to ensure that a constant, like NAME does not
# have its value changed. 


NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)