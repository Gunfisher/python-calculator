print("Welcome to Vinayak's Calculator!")
print("----------------------------------")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thanks for using Vinayak's Calculator! Goodbye! 👋")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} x {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid choice! Please enter 1-5 only.")