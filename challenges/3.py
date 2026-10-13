valid = False
while not valid:
    try:
        number = int(input("Enter a number: "))
        valid = True
        print("You entered: ", number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")