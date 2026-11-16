num = int(input("Num:"))
flag = False 
i=2
while i< num:
    if num % i== 0:
        flag = True
        break

    i +=1
if flag :
    print(f"{num} is omposite")
else:
    print(f"{num} is prime")
