num = int(input("enter any Number:" ))
count = 0
while num != 0:
    num = num //10
    count +=1
print (f"Number of Digits is:{count}")