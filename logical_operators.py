# first logical operator to deal with "or" 
# Addition in Arithmetic operator
'''
first_number = 5
second_number = 4
sum = first_number + second_number
mul = first_number * second_number
Subtraction = first_number - second_number
division = first_number / second_number
exponential 
print(mul)
'''

# a simple calculator App

print("""***************** 1. Additiom
2. Subtraction
3. Mulitiplication
4. Division
***********************""")

print("Enter two number to add")
first_number = input("first number:")
second_number = input("second number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum}")

sub = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {sub}")

#Division
div = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {div}")

# Exponential
exp = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {exp:.2f}")




