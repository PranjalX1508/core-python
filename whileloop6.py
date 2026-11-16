num = int(input('num = '))   #456
rem = 0
a=num
reversed = 0

while num > 0:
    rem = num % 10
    reversed = reversed * 10 + rem
    num //= 10


    

print(reversed)

if reversed==a:
    print("Paliron")
else:
    print(" not Prio")