m1 = int(input("marks: "))
m2 = int(input("marks: "))
m3 = int(input("marks: "))
m4 = int(input("marks: "))
m5 = int(input("marks: "))

avg = (m1 + m2 + m3 + m4 + m5) /5

if avg >= 75:
    
    print("your grade is a")

elif avg >= 60:
    
    print("your grade is b")


elif avg >= 40:
    
    print("your grade is c")

else:
    print("your grade is a d")