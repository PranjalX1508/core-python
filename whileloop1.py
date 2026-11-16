from random import randint

ran_num = randint(1,1000)
print(f"Random number: {ran_num}")
while True:
    num= int(input("numbr"))
    if ran_num > num:
        print("Numbr is smallr")
    elif ran_num < num:
        print("numbr is greater")
    elif ran_num == num:
        print("numbr is equal")
        break
print(ran_num)