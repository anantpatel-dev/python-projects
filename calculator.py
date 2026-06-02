print("Simple Calculator")
print("------------------")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = input("Enter choice (1/2/3/4/5): ")

if choice == "1":
    result = num1 + num2
    print("Answer:", result)
elif choice == "2":
    result = num1 - num2
    print("Answer:", result)
elif choice == "3":
    result = num1 * num2
    print("Answer:", result)
elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        print("Answer:", result)
elif choice == "5":
    result = num1 % num2
    print("Answer:", result)
else:
    print("Invalid choice")
