def calculator():
    print("Simple Calculator")

    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, / or 'q' to quit): ")

        if operation == '+':
            print("Result:", num1 + num2)
        elif operation == '-':
            print("Result:", num1 - num2)
        elif operation == '*':
            print("Result:", num1 * num2)
        elif operation == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")
        elif operation.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid operation!")

calculator()
