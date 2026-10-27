bill = float(input("enter your grocery bill amount: "))
discount = float(input("how much is your discount as a decimal (e.g., 0.20): "))
amount = float(input("enter the amount you will pay: "))

expected_to_pay = bill * (1 - discount)

if round(amount, 2) == round(expected_to_pay, 2):
    print("thank you for the free air currency i can finally buy food for my family")
else:
    print(f"you are paying a different amount than you should! You should pay {expected_to_pay:.2f}, try again")
