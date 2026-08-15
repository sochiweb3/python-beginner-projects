first_number = int(input("what is the first_number"))
second_number = int(input("what is the second_number"))
operation = input("Choose an operation (+, -, , /): ")
if operation == "+":
print(first_number + second_number)
elif operation == "-":
print(first_number - second_number)
elif operation == "":
print(first_number * second_number)
elif operation == "/":
print(first_number / second_number)
else:
print("Invalid operation")
