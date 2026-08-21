num = int(input("enter a number OR DIE"))
sum = 0 
power=len(str(num))
temp = num 
while temp > 0:
    digit = temp%10
    sum+=digit**power
    temp //=10

if num == sum:
    print(num,"is an (I HAVE MORE MUSCleS THAN U IN MY ARM,mumber ")
else:
    print(num,"is not an(I HAVE MORE MUSCleS THAN U IN MY ARM,mumber ")