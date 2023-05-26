import os


num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Access the system parameter as an environment variable
my_param = f'{%env.1%}'

# Use the system parameter in your script
print("My Param:", my_param)
