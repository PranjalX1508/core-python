num = int(input("enter any Number:" ))
sum = 0
while num != 0:
    Digit=num % 10
    sum= sum + Digit
    num = num // 10
print (f"Number of Digits is:{sum}")