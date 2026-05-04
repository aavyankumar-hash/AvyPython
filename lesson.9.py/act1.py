med=input("were you away due to med reasons ").strip().upper()
if med=='Y':
    print("You are allowed to sit for the exam.")
else:
    atten=int(input("enter your attendance percentage"))
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")