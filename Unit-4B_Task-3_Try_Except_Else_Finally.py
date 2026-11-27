# Unit - 4B Task - 3: Try Except Else Finally
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

else:
    print("Division Result:", result)
    print("No error occurred.")

finally:
    print("Program execution completed.")