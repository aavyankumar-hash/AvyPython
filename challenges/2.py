try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    result=num1/num2
    print("The result of division is: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter valid integers.")
except:
    print("An unexpected error occurred.")
else:
    print("Division completed successfully.")
finally:
    print("Execution of the program is complete.")