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
5. Exponential
6. floor Division
***********************""")

print("Enter two number to add")
first_number = input("first number:")
second_number = input("second number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum}")

#subtraction
print("Enter two number to subtract")

first_number = input("first number:")
second_number = input("second number:")

sub = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {sub}")

#Division
print("Enter two number to divide")

first_number = input("first number:")
second_number = input("second number:")

div = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {div}")

# Exponential
print("Enter two number to Exponent")

first_number = input("first number:")
second_number = input("second number:")

exp = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {exp:.2f}")

# floor division

first_number = input("first number:")
second_number = input("second number:")
floor = float(first_number) // float(second_number)
print(f"{first_number} // {second_number} = {floor}")

