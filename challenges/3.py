valid = False
while not valid:
    try:
        number = int(input("Enter a number: "))
        while number % 2 == 0:
            print("The number is even.")
            number = int(input("Enter an odd number: "))
        valid = True
        print("You entered: ", number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")