# Unit - 4B Task - 2: Multiple Except Blocks
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Division Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter only numbers!")

except TypeError:
    print("Error: Invalid data type!")

except Exception:
    print("Error: Something went wrong!")

finally:
    print("Program execution completed.")