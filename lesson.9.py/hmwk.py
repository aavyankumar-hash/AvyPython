number = int(input("Enter a number: "))
indices = int(input("Enter the power: "))

ans = 1 
for i in range(indices):
    ans = ans * number
print("The answer is:", ans) 