num = int(input("Numb:"))
min = 9
max =0 
while num != 0:
    rem=num % 10
    num = num // 10
    if rem > max:
        max = rem
        print(f"Numbr is gratr{max}")
    if rem < min:
        min = rem
        print(f"Numbr is smallr{min}")
        num = num // 10
