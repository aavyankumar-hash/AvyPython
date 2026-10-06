a = int(input("Enter your first number to multiply by: "))
print(a)
answer = input("Is that correct? (yes/no): ").strip().lower()

if answer == "yes":
    print("OK great")
elif answer == "no":
    print("Let's try that again")
else:
    print("Please answer yes or no.")